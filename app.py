from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('NewDelhiRentPrice_model.pkl','rb'))


# main  index page route
@app.route ('/')
@app.route('/index')
def home():
        return render_template("home.html")

#prediction function
def ValuePredictor(x):
    z=np.zeros(10)
    z[0]=x[0]
    z[1]=x[1]
    z[2]=x[2]
    z[3]=x[3]
    z[4]=x[4]
    z[5]=x[5]
    z[6]=x[6]
    z[7]=x[7]
    z[8]=x[8]
    z[9]=x[9]    
    print(x)
    
    result = model.predict([z])[0]
    print(result)
    return result

# prediction result
@app.route('/result',methods = ['POST','GET'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        
        to_predict_list=list(to_predict_list.values())
        to_predict_list = list(map(str, to_predict_list))
        result = ValuePredictor(to_predict_list)
        result=round(result*1000)
            
        return render_template("home.html", result='==>Rent price is {} INR<=='.format(result))

if __name__=="__main__":
    app.run(debug=True)