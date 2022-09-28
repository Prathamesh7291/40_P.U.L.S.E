
import numpy as np
from flask import Flask , request, jasonify, render_template
import pickle

app=Flask(__name__)

model=pickle.load(open("model.pkl", "rb"))

@app.route("/n")
def Home():
    return render_template("")

@app.route("/predict",methods=['POST'])
def predict():
    float_features = [float (x) for x in request.form.values()]
    features=[np.array(float_features)]
    prediction=model.prediction(features)

    return render_template(".html",prediction_text="".format(prediction))

if __name__ == "__main__":
    app.run(debug=True)


