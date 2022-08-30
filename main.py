from flask import Flask,request,render_template
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
realay_pin = 7
realay_pin2 = 5
GPIO.setup(realay_pin, GPIO.OUT)
GPIO.setup(realay_pi2, GPIO.OUT)

app = Flask(__name__)

@app.route("/")
def home1():
    return render_template("index.html")
@app.route("/on1")
def home2():
    GPIO.output(realay_pin, GPIO.LOW)
    return render_template("index.html")
@app.route("/off1")
def home3():
    GPIO.output(realay_pin, GPIO.HIGH)
    
    return render_template("index.html")

@app.route("/on2")
def home23():
    GPIO.output(realay_pin2, GPIO.LOW)
    return render_template("index.html")
@app.route("/off2")
def home33():
    GPIO.output(realay_pin2, GPIO.HIGH)
    
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host="192.168.43.90",debug=True)


