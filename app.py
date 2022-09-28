
import numpy as np
from flask import Flask , request, render_template
import pickle

app=Flask(__name__)

model=pickle.load(open("random.pkl", "rb"))

@app.route("/")
def main():
    return render_template('homePage.html')

@app.route("/login")
def main1():
    return render_template('login.html')

@app.route("/registration")
def main2():
    return render_template('registration.html')

@app.route("/diet")
def main3():
    return render_template('diet.html')

@app.route("/exercise")
def main4():
    return render_template('exercise.html')

@app.route("/form")
def Home():
    return render_template("medHistory.html")

def dataConvertor (features):
    finaldata= []
    for feature in features:
        if feature[0] == 'name':
            finaldata.append(feature[1])
        
        else:
            finaldata.append(int(feature[1]))
    return finaldata

@app.route("/predict",methods=['POST'])
def predict():
    # features =dataConvertor(request.form)
    # print(features)
    # float_features = [x for x in request.form.values()]

    nm = request.form['name'] #name
    em = request.form['email'] #email
    #rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr
    ag = request.form['age'] #age
    gn = request.form['gender'] #gender
    cp = request.form['chestpain'] #cp
    bp = request.form['bloodpressure'] #bp
    sc = request.form['sech'] #sech
    fbs = request.form['fbs'] #fbs
    ecg = request.form['ecg'] #fbs
    hra = request.form['hra'] #hra
    eia = request.form['eia']
    deprst=request.form['deprst']
    spe = request.form['slope']
    mv = request.form['vessels']
    thal = request.form['thal']

    qop = np.array([[ag, gn, cp, bp, sc, fbs, ecg,hra, eia, deprst, spe, mv, thal]])
    
    # features=[np.array(float_features)]
    prrr = model.predict(qop)
    print(prrr)
    print(type(prrr[0]))
    a = "default"
    if prrr[0] == 1:
        a = "You might have heart disease"
    elif prrr[0] == 0:
        a = "You don't have a Heart disease"
        
    return render_template("result.html",prediction =a)

if __name__ == "__main__":
    app.run(debug=True)


