import RPi.GPIO as GPIO # importer les GPIO
from tkinter import * # importer la librairie Tkinter
from tkinter import font 

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.OUT)
GPIO.output(27, GPIO.LOW)
p=GPIO.PWM(27, 100) #MLI

def ledON():
    print("Boutton pressé.") # affiche le texte "bouton préssé" sur la fenêtre de compilation python
    if GPIO.input(27): 
        GPIO.output(27, GPIO.LOW) 
        ledButton["text"] = "LED OFF"
        p.start(0)
        
    else:
        GPIO.output(27, GPIO.HIGH) 
        ledButton["text"] = "LED ON"
        p.start(100)

def gpio_mli_activation(value):
        temp = value.get()
        print(temp)
        p.ChangeDutyCycle(temp)
        

win = Tk() # Création de la fenêtre principale
#win.geometry('600x380')
win.attributes('-fullscreen', 1)

exitButton = Button(win, width=7, height=2, text = "Quitter", fg="white",bg='#205B96',activebackground="#ffffff",font="Arial 20 italic", command=win.destroy) # Permet de quitter le programme en appuyant sur le bouton 
exitButton.place(x=320, y=350, in_=win)

ledButton = Button(win, width=10, height=4, text = "LED ON", fg="white", bg="#205B96", activebackground="white", font="arial 30", command=ledON)
ledButton.place(x=130, y=80, in_=win)

value = DoubleVar() #MLI
scale = Scale(win, variable=value, orient=HORIZONTAL, length=160, width=50, bg="#205B96",activebackground="white", command=lambda x: gpio_mli_activation(value)) #MLI
scale.place(x=40, y=350, in_=win) #MLI

photo = PhotoImage(file="lamp.png") # ajout de la photo "lamp.png"

canvas = Canvas(win,width=309, height=443, bg="#357AB7")
canvas.create_image(-5, -5, anchor=NW, image=photo)
canvas.place(x=472, y=17, in_=win)

mainloop() # Boucle principale
