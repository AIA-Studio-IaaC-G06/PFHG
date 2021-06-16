from typing import ItemsView, Literal
from flask import Flask
import ghhops_server as hs
from ghhops_server.params import HopsNumber
import rhino3dm
import numpy as np
import os
import sys
#import tensorflow as tf
import pickle
import joblib
import machinelearning as ml

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

app = Flask(__name__)
hops = hs.Hops(app)

@hops.component(
    "/runML3",
    name="runML3",
    description="Run Machine Learning prediction",
    icon="examples/pointat.png",
    inputs=[
        hs.HopsNumber("Construction Cost", "Cost", "Construction Cost"),
        hs.HopsNumber("Rotation angle from North", "Rotation", "Rotation Angle"),
        hs.HopsNumber("Construction Time", "Time", "Construction Time"),
    ],
    outputs=[
        hs.HopsNumber("Length X", "X", "Length X"),
        hs.HopsNumber("Length Y", "Y", "Length Y"),
        hs.HopsNumber("Wall Panels number", "Wall N°", "Wall Panels number"),
        hs.HopsNumber("Window Panels number", "Window N°", "Window Panels number"),
        hs.HopsNumber("Spatial Daylight Autonomy", "sDA", "Spatial Daylight Autonomy"),
        hs.HopsNumber("Total Electricity consumption", "Electricity", "Total Electricity Consumption"),
        hs.HopsNumber("Light Electricity consumption", "Light", "Light Electricity Consumption"),
        hs.HopsNumber("Cooling Electricity consumption", "Cooling", "Cooling Electricity Consumption"),
        hs.HopsNumber("Heating Electricity consumption", "Heating", "Heating Electricity Consumption")
    ]
)

def runml(a,b,c):
    

    return ml.runml(a,b,c)

  

if __name__ == "__main__":
   app.run(debug=True)



   
#######################################
#BONUS HINT

#if you had a scaler in your training you should have had this
##Normalize data using standard scaling
#scalerY = StandardScaler().fit(outputArr)
#y_scaled = scalerY.transform(outputArr)
#print("y_scaled", np.amin(y_scaled), np.amax(y_scaled))

##Save scaler model for later use
#joblib.dump(scalerY, 'scalerY.pkl')

#SO YOU NEED TO
#Load scaler for inverse transformation
#scalerY = joblib.load("scalerY.pkl")
#And apply it to either input or output

#########################################