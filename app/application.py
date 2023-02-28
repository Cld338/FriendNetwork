from flask.templating import render_template
import graphDistance
from flask import Flask, request, send_from_directory
import time
import os
import sys
app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    startID = (request.args.get('startID', default = "", type = str).replace(" ","")).lower()
    endID = request.args.get('endID', default = "", type = str).replace(" ","").lower()
    if startID=="":
        return render_template("index.html", startID=startID, endID=endID, able=1)
    print(str(graphDistance.traslate_id_pk(startID)))
    if startID not in 
    path=None
    distance=None
    if startID and endID:
        path = graphDistance.search(startID, endID)
        if path:
            distance=len(path)-1
        else:
            distance=-1
    # time.sleep(10)
    return render_template("index.html", startID=startID, endID=endID, path=path, distance=distance, able=1)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == "__main__":
    currDir = os.path.dirname(os.path.realpath(__file__))
    # fileNum = len([file.replace(".txt", "") for file in os.listdir(currDir+"/network") if file.endswith(".txt")])
    # privateNum = len([file.replace(".txt", "") for file in os.listdir(currDir+"/private") if file.endswith(".txt")])
    app.run(debug=True, host="0.0.0.0", port=5000)