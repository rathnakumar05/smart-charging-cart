import os
import re
import json
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

desired_order = [114990191666836, 61797658713100, 259872926915596, 132183582759948, 189692557846164, 123781989721748, 206757083143180]

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
            if len(data[i])>=3:
                front = [*data[i][0]["TempData"], *data[i][1]["TempData"][0:8]]
                back = [*data[i][1]["TempData"][8:], *data[i][2]["TempData"]]
            elif len(data[i])>=1:
                front = [*data[i][0]["TempData"]]
                if len(data[i])>1:
                    front = [*front, *data[i][1]["TempData"][0:8]]
                    back = data[i][1]["TempData"][8:]
            parsed_data["front"]["row"+str(i)] = front
            parsed_data["back"]["row"+str(i)] = back
    return parsed_data

@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/")
def index():
    content = data = None
    content = readFile()
    if content is not None:
        data = json.loads(content)
        data = data["data"]
    data = orderData(data)
    data = parseData(data)

    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)