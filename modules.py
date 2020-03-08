import requests,json,math,operator
from resources import *

def compareTrans(origin,destination):
   wcar = get_ddData(origin,destination,"driving")
   carduration = wcar["duration"]
   stationsnearme = GetNearestStations(origin)
   closeststationnearme = stationsnearme[0]["id"]
   stationsnearfinal = GetNearestStations(destination)
   closeststationnearfinal = stationsnearfinal[0]["id"]
   metroduration = CalculateDuration(closeststationnearme,closeststationnearfinal)
   cardurationminute = ConvertHourToMinute(carduration)
   finallat = GetStationLocation(closeststationnearfinal)["lat"]
   finallong = GetStationLocation(closeststationnearfinal)["long"]
   finalstationloc = str(finallat) + ", " + str(finallong)
   firstlat = GetStationLocation(closeststationnearme)
   firstlong = GetStationLocation(closeststationnearme)
   firststationloc = str(firstlat) + ", " + str(firstlong)
   caruntilstation = get_ddData(origin,firststationloc,"driving")
   walkingafterfinal = get_ddData(finalstationloc,destination,"walking")
   print(ConvertHourToMinute(walkingafterfinal["duration"]))
   ptranstotal =  ConvertHourToMinute(caruntilstation["duration"]) + math.floor(metroduration/60)
   print(f"Metro ile: {ptranstotal}")
   print(f"Araba İle: {wcar}")
compareTrans("38.435096, 27.168880","38.427115, 27.154540")