
# Kütüphaneler Tanımlandı
from flask import Flask,request,render_template
import RPi.GPIO as GPIO

#Raspberry Pi pinlerine erişilip 12 numaralı (board numaralandırmalı) pin
#Çıkış pini olarak tanımlandı
GPIO.setmode(GPIO.BOARD)
relay = 12
GPIO.setup(relay, GPIO.OUT)

# Flask nesenesi app değişkine üzerine çağrıldı
app = Flask(__name__)


# Web Sayfası açıldığında görüntülenecek sayfa
@app.route("/") 
def main():
    #Bu fonksiyon devreye girince sadece index.html dosyası render edildi
    return render_template("index.html")

#Işık yakma butonuna basılınca yönlendirilecek olan sayfa 
@app.route("/on")
def ac():
    #Bu fonksiyon devreye girince ışık açlıldı
    GPIO.output(relay, GPIO.HIGH)
    #Eğer her fonksiyonun sonuna index.html dosyası render edilmez ise sayfa boş kalır
    return render_template("index.html")

@app.route("/off")
def kapa():
    #Bu fonksiyon devreye girince ışık Kapandı
    GPIO.output(relay, GPIO.LOW)
    
    return render_template("index.html")

    
if __name__ == '__main__':
    app.run(host="192.168.1.28",debug=True, port=8000)  # Local IP nizi girin (hostname - I komutu ile bulabilirsiniz)


