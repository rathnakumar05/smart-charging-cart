import os
import re
import json
import datetime
from flask import Flask, render_template, send_from_directory
from waitress import serve

app = Flask(__name__)

desired_order = [114990191666836, 61797658713100, 259872926915596, 132183582759948, 189692557846164, 123781989721748, 206757083143180]
on_off_minutes = 5
show_hide_temp = 0

def readFile():
    content = None
    with open(os.path.join(app.root_path, 'result.json'), "r") as file:
        content = file.read()
    return content

def orderData(data):
    print("Before Sort")
    print(data)
    print("==================================================================")
    data = [el for el in data if el["DeviceID"] in desired_order]
    data = sorted(data, key=lambda x: desired_order.index(x["DeviceID"]))
    print("After Sort")
    print(data)
    return data

def parseData(data):
    parsed_data = {
        "front" : {},
        "back" : {}
    }
    if data != None:
        data = [data[i:i+3] for i in range(0, len(data), 3)]
        for i in range(len(data)):
            front = []
            back = []
            if len(data[i])==3:
                front = [*data[i][0]["TempData"][0:8], *data[i][1]["TempData"][0:8], *data[i][2]["TempData"][0:8]]
                back = [*data[i][2]["TempData"][8:16], *data[i][1]["TempData"][8:16], *data[i][0]["TempData"][8:16]]
            elif len(data[i])==2:
               front = [*data[i][0]["TempData"][0:8], *data[i][1]["TempData"][0:8]]
               back = [*data[i][1]["TempData"][8:16], *data[i][0]["TempData"][8:16]]
            else:
                front = [*data[i][0]["TempData"][0:8]]
                back = [*data[i][0]["TempData"][8:16]]
            
            parsed_data["front"]["row"+str(i)] = front
            parsed_data["back"]["row"+str(i)] = back
    return parsed_data

@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/")
def index():
    content = data = None
    last_updated = []
    status = "OFF"
    content = readFile()
    if content is not None:
        try:
            data = json.loads(content)
            data = data["data"]
        except:
            print("JSON ERROR")
    if data is not None:
        data = orderData(data)
        last_updated = [{"DeviceID": el["DeviceID"], "LastUpdated": el["LastUpdated"]} for el in data]
    data = parseData(data)

    current_time = datetime.datetime.now()
    if last_updated is not None and len(last_updated) > 0:
        updated_time = datetime.datetime.strptime(str(last_updated[0]["LastUpdated"]), "%Y-%m-%d %H:%M:%S")
        diff_time = current_time - updated_time
        if(diff_time.total_seconds() / 60 <= on_off_minutes):
            status = "ON"
    current_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

    return render_template('index.html', data=data, last_updated=last_updated, current_time=current_time, status=status, show_hide_temp=show_hide_temp)


if __name__ == '__main__':
    # app.run(debug=True)
    serve(app, host='0.0.0.0', port=5000)