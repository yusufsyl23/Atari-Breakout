import turtle as tr
from raket import Raket
from top import Top
from skor import Skor
from zorluk import Zorluk , show_difficulty_selection
from tugla import Tugla
import time

zorluk_derecesi = show_difficulty_selection()

if not zorluk_derecesi:
    print("Zorluk seviyesi seçilmedi. Program kapatılıyor.")
    exit()

ekran = tr.Screen()
ekran.title("Atari Breakout")
ekran.bgcolor("black")
ekran.setup(width=1205,height=600)
ekran.tracer(0)

zorluk_seviyesi = Zorluk(zorluk_derecesi)
top = Top(zorluk_derecesi)  
tugla = Tugla(zorluk_derecesi)
tugla._duvar_yap(ekran)
skor_tablo = Skor(zorluk_derecesi)  
oyun_raketi = Raket(zorluk_derecesi) 

def game_over():
    if (skor_tablo._can == 0):
        top.goto(0,0)
        gameOver = tr.Turtle()
        gameOver.hideturtle()
        gameOver.speed(0)
        gameOver.color("Yellow")
        gameOver.penup()
        gameOver.goto(0,-100)
        gameOver.write(f"Kaybettiniz\nPuanınız : {skor_tablo._skor}" , align = "center" , font = ("Impact",24,"bold"))
        time.sleep(3)
        return True
    return False

def kazanma():
    if (len(tugla._tugla_liste) == 0):

        top.penup()
        top.goto(0,0)
        win = tr.Turtle()
        win.hideturtle()
        win.speed(0)
        win.color("Yellow")
        win.penup()
        win.goto(0,-100)
        win.write(f"Kazandınız\nPuanınız : {skor_tablo._can * skor_tablo._skor}",align = "center" , font = ("Impact",24,"normal"))
        time.sleep(3)
        return True
    return False

ekran.listen()
ekran.onkeypress(oyun_raketi._saga_hareket,"Right")
ekran.onkeypress(oyun_raketi._sola_hareket,"Left")
ekran.onkeypress(oyun_raketi._dur,"space")

while True:
    
    if (oyun_raketi._basla == 1 ):
    # Bu kısım topun konumunu güncelleyerek harek etmesini sağlar
        top._hareket()

    if game_over():   
        break
    if kazanma():
        break

    # Burda top sınıfının özelliği olan tuğla kırma metodunu çağırıp tuğlaları kırdık.
    top._tugla_kirma(tugla,skor_tablo)

    # Burda top sınıfının özelliği olan duvar sekme metodunu çağırıp duvarda sekmeleri yaptık.
    top._duvar_sekme(skor_tablo)
    
    # Burda top sınıfının özelliği olan raket sekme metodunu çağırıp rakette sekmeleri yaptık.
    top._raket_sekme(oyun_raketi)
    
    ekran.update()
    time.sleep(0.02)

 
    




