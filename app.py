from flask import Flask, request, jsonify
import os,sys
from resources import CalculateDuration, GetStationData, GetTotalPassengers, GetBAStations,GetTotalPassengers,GetStationNames
from resources import GetNearestStations, get_ddData, GetStationLocation
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
sys.stdout = sys.__stdout__
sys.stderr = sys.__stderr__

@app.route("/apis/duration",methods=["POST"])
def return_duration():
    st1 = request.json["st1"]
    st2 = request.json["st2"]
    duration = CalculateDuration(int(st1),int(st2))
    data = {"duration": duration}
    return jsonify(data)

@app.route("/apis/getbastation",methods=["POST"])
def return_getbastation():
    print(request)
    stno = request.json['stno']
    data = GetBAStations(int(stno))
    return jsonify(data)

@app.route("/apis/stationdata",methods=["POST"])
def return_stationData():
    stno = request.json['stno']
    data = GetStationData(int(stno))
    return jsonify(data)

@app.route("/apis/totalpassengers",methods=["POST"])
def return_totalpassengers():
    stno = request.json["stno"]
    time = request.json["time"]
    try:
        time2 = request.json["time2"]
        data = GetTotalPassengers(stno,time,time2)
        return jsonify({"psnum":data})
    except Exception as e:
        data = GetTotalPassengers(stno,time)
        return jsonify({"psnum":data})
@app.route("/apis/getnstations",methods=["POST"])
def return_nstations():
    origin = request.json["origin"]
    nstations = GetNearestStations(origin)
    return jsonify(nstations)
@app.route("/apis/ddata",methods=["POST"])
def return_dddata():
    origin = request.json["origin"]
    destination = request.json["destination"]
    mode = request.json["mode"]
    data = get_ddData(origin,destination,mode)
    return jsonify(data)
@app.route("/apis/getstationlocation",methods=["POST"])
def return_getstlocation():
    stno = request.json["stno"]
    data = GetStationLocation(stno)
    return jsonify(data)
if __name__ == '__main__':
    app.run()