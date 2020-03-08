# -*- coding: utf-8 -*-
import requests,json,math,operator
apiurl ="http://api.izmirhackathon.com/"



def CalculateDuration(id_start,id_finish):
    s = requests.session()
    apiurl ="http://api.izmirhackathon.com/distance"
    if(id_start>id_finish):
        temp = id_finish
        id_finish = id_start
        id_start = temp

    isCalculate = False
    duration = 0
    r = s.get(apiurl)
    #starttan başla end i bulana kadar topla
    for data in r.json():
        if(int(data['id_st']) == id_start):
            isCalculate = True
        if(isCalculate):
            duration += int(data['duration'])
            if(int(data['id_end']) == id_finish):
                break
    return duration


def CalculateDistance(id_start,id_finish):
    s = requests.session()
    apiurl ="http://api.izmirhackathon.com/distance"
    if(id_start>id_finish):
        temp = id_finish
        id_finish = id_start
        id_start = temp

    isCalculate = False
    distance = 0
    r = s.get(apiurl)
    #starttan başla end i bulana kadar topla
    for data in r.json():
        if(int(data['id_st']) == id_start):
            isCalculate = True
        if(isCalculate):
            distance += int(data['distance'])
            if(int(data['id_end']) == id_finish):
                break

    return distance


def GetTotalPassengers(s_id,time,time2=-1): #station ID TODO
    s = requests.session()
    
    passCount = 0

    if(time2==-1 or time2==time):
        time2=time+1
    
    if(time>time2):
        temp = time
        time = time2
        time2 = temp

    
    if(time<0 or time>24 or time2<0 or time2>24):
        print(time," ",time2)
        return "ERROR: Invalid Time"
    


    timeIndex = time-5
    timeIndex2 = time2 -5
    
    apiurl ="http://api.izmirhackathon.com/passengers"
    r = s.get(apiurl)
    r = r.json()

    
    for i in range(timeIndex,timeIndex2):
        s = r[0]["passenger_information"][i]["passengerByStation"]
        for data in s:
            if(int(data["station_id"]) == s_id):
                passCount+= int(data["passenger_count"])
    data = math.floor(passCount/12)
    return data



def GetBAStations(s_id):
    s = requests.session()
    s_id = s_id-1
    apiurl ="http://api.izmirhackathon.com/stations"
    r = s.get(apiurl)
    r = r.json()
  
    if s_id != 0:
        stationBefore = r[s_id-1]["station"]
    else:
        stationBefore = "none"
    if s_id != 16:
        stationAfter = r[s_id+1]["station"]
    else:
        stationAfter = "none"

    data = {"stationbefore": stationBefore,
            "stationafter":stationAfter
            }
            
    return data

def GetStationNames():
    s = requests.session()
    apiurl ="http://api.izmirhackathon.com/stations"
    r = s.get(apiurl)
    i = 1
    data = {}
    for x in r.json():
        data[i] = {"station":x["station"]}
        i+=1
        
    return json.dumps(data)   


def GetStationData(s_id):
    s = requests.session()
    apiurl ="http://api.izmirhackathon.com/stations"
    r = s.get(apiurl)
    #print(r.json()[s_id-1])
    return r.json()[s_id-1]


def get_ddData(origin,destination,mode):

    url = "https://maps.googleapis.com/maps/api/distancematrix/json?mode="+ mode +"&origins="+ origin +"&destinations="+ destination +"&key=[GOOGLE_API_KEY]"
    r = requests.get(url)
    destination = destination.replace(" ","")
    origin = origin.replace(" ","")
    distance = r.json()["rows"][0]["elements"][0]["distance"]["text"]
    duration = r.json()["rows"][0]["elements"][0]["duration"]["text"]
    data = {"distance": distance,"duration":duration}
    return data

def GetNearestStations(origin):
    data = GetStationsLocations()
    minDistance = 0
    distances = {}
    a = 1
    i = 1
    for line in data:
        enlem = str(data[i]["enlem"])
        boylam =str( data[i]["boylam"])
        dest = enlem + ", " + boylam
        response = get_ddData(origin,dest,"walking")
        try:
            distance = float(response["distance"].replace(" km",""))
        except Exception as e:
            distance = float(response["distance"].replace(" m",""))
        distances[str(i)] = distance
        i += 1
    sorted_data = sorted(distances.items(), key=operator.itemgetter(1))
    x = 0
    last_data = []
    """    
        while x<3:
            last_data[x] = (sorted_data[x][0],GetStationLocation(int(sorted_data[x][0])))
            x += 1
    """
    while x<3:
        last_data.append((GetStationLocation(int(sorted_data[x][0]))))
        x += 1
    return last_data

def GetStationsLocations():
    s = requests.session()
    apiurl ="http://api.izmirhackathon.com/locations"
    r = s.get(apiurl)
    i = 1
    data = {}
    for x in r.json():
        data[i] = {"enlem":x["lat"],"boylam":x["long"]}
        i+=1
    return data


def GetStationLocation(s_id):
    s = requests.session()
    apiurl ="http://api.izmirhackathon.com/locations"
    r = s.get(apiurl)
    for data in r.json():
        if(int(data["id"]) == s_id):
            return data


def ConvertHourToMinute(temp):
    hours=0
    minutes = 0
    finalTime = 0
    try:
        if(temp.find("hours")!=-1):
            hours=int(temp[0:temp.find("h")])
            if(temp.find("mins")!=-1):
                minutes=int(temp[temp.find("s")+1:temp.find("m")])
        else:
            minutes=int(temp[0:temp.find("m")])
    except Exception as e:
        return "Input ERROR",e
    
    return hours*60+minutes

print(ConvertHourToMinute("12 hours 6 mins"))
#print(GetStationLocation(5))
#print(GetStationLocation(6))
#print(GetBAStations(15))
#print(GetBAStations(15))
#print (GetStationData(15))
#print (GetStationData(15))
#print(CalculateDistance(3,4))
#print(CalculateDistance(3,4))
#print(CalculateDuration(3,4))
#print(CalculateDuration(3,4))
#print(GetTotalPassengers(15,20,22))
#print(GetTotalPassengers(15,7,7)) 
#GetStationsLocations()


