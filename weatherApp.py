#you will need some libraries!
#pip install requests
#pip install Pillow ----- which stands for python imaging library
#urllib and tkinter library comes by default in python so you do not need to install it !!

import tkinter as tk
from tkinter import font
import requests
root = tk.Tk()
#root.mainloop() ----- put this thing in the end later!
#Now you should see a new window there!

def format_response(weather):
    name = weather["name"]
    desc = weather["weather"][0]["description"]
    temp = weather["main"]["temp"]
    
    return "City: " + name + "\n" + "Condition: " + desc + "\n" + "Temperature in Celcius: "+ str(temp)

def fun(entry):
    print("You have typed!",entry)

def get_wet(city):
    key = "pls get your own api key!"
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {'APPID':key,"q":city, "units":"metric"}
    response = requests.get(url,params=params)
    weather = response.json()
    #print(weather)
    #name = weather["name"])
    #print(weather["weather"][0]["description"])
    #print(weather["main"]["temp"])
    
    label["text"]  = format_response(weather)

HEIGHT = 500
WIDTH = 600

canvas = tk.Canvas(root,height = HEIGHT, width = WIDTH)
canvas.pack()

#bg_image = tk.PhotoImage(file="download.png")
#bg_label = tk.Label(root,image=bg_image)
#bg_label.place(relwidth=1,relheight=1)

frame = tk.Frame(root, bg="#FF8000", bd=5)
frame.place(relx = 0.5, rely = 0.1, relwidth=0.75,relheight=0.1, anchor="n")

entry = tk.Entry (frame, bg="white", font = 40)
#entry.pack(side="left", fill = "both")
#use grid instead of pack
#entry.grid(row=0,column=2)
entry.place(relwidth=0.65, relheight=1)

#button = tk.Button (root, text = "My Test Button").grid()
#or you may use it this way
button = tk.Button (frame, text="Cal Weather", bg="#0000A6", fg= "white", font=40, command= lambda: get_wet(entry.get())) #for yellow #FF8000
#button.pack(side="left", fill="x", expand=True) # this method puts button into center!
#use grid or place instead of pack if you like
#button.grid(row=0,column=0)
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg="#FF8000", bd=5)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor="n")

label = tk.Label(lower_frame, bg="white", font = ("courier",18), anchor="nw", justify="left" )
#label.pack(side="left", fill="both")
#use grid instead of pack
#label.grid(row=0,column=1)
label.place(relwidth=1, relheight=1)

root.mainloop()