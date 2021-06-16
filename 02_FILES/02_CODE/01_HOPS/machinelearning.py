import rhino3dm
import numpy as np
import pickle
import joblib
from tensorflow import keras


def runml(a,b,c):
   
    model = keras.models.load_model(r'C:\Users\kimky\Desktop\tmp\S4_STUDIO\ML-GEOMETRY\ML\regression_model_V5.h5')
    model.summary()

    #Load Standardscaler
    from sklearn.preprocessing import StandardScaler
    scalerX = joblib.load(r'C:\Users\kimky\Desktop\tmp\S4_STUDIO\ML-GEOMETRY\ML\scalerX2.pkl') 
    scalerY = joblib.load(r'C:\Users\kimky\Desktop\tmp\S4_STUDIO\ML-GEOMETRY\ML\scalerY2.pkl') 
    print('Scalers loaded')

    #-------------------
    Newdata = [[a,b,c]]
    Newdata = np.array((Newdata),dtype=np.float64)
    Newdata = Newdata.astype(np.float32)
    Newdata_scaled = scalerX.transform(Newdata)

    predictions = model.predict(Newdata_scaled)

    finalPrediction = scalerY.inverse_transform(predictions)

    list1 = finalPrediction.tolist()
    flat_list = []
    for i in list1:
        flat_list += i

    final_pred = predictions[0]
    print(flat_list)

    return flat_list[0], flat_list[1],flat_list[2],flat_list[3],flat_list[4],flat_list[5],flat_list[6],flat_list[7], flat_list[8]

#To debug, look at Test2