from flask import render_template
from flask import Flask
from datetime import datetime
import os
import re
import time
import DrowsinessDetectionOrig
import graphFile

app = Flask(__name__, template_folder = "templates")

@app.route("/")
@app.route("/home/")
def home():
    return render_template("test.html")

@app.route("/launch/")
def launch():
    beep = "BEEP!"
    return render_template("test2.html", data=beep)

@app.route("/go/")
def go():
    theData = DrowsinessDetectionOrig.mainLoop()
    print("App.py",theData)
    return render_template("test2.html", data=theData)
    
@app.route("/analytics/")
def analytics():
    return render_template("test3.html")

@app.route("/graph/<graphdata>")
def graph(graphdata):                                                                                        
    print(graphdata) 
    print("WOWOOWOW")
    graphFile.splitString(graphdata)
    return render_template("test3.html")
