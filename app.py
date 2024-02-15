from flask import Flask, render_template, request
import pickle

model = pickle.load(open("rf_model.pkl", "rb"))

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST", "GET"])
def predict():
    if request.method == "post":
        state = float(request.form["state"])
        variety = float(request.form["variety"])
        min_price = float(request.form["min_price"])
        max_price = float(request.form["max_price"])

        data = [[state, variety, min_price, max_price]]

        prediction = model.predict(data)
    
        return render_template("predict.html", prediction_text= "Prediction: {}".format(prediction))
    return render_template("predict.html")

if __name__ == '__main__':
    app.run(debug=True)