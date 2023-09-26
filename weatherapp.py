import tkinter as tk 
from tkinter import *
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title("Weather app")
root.geometry("900x500+300+200")

def getweather():
    city = textfield.get()
    
    geolocator = Nominatim(user_agent="geoapiExercises")
    location=  geolocator.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
    print(result)
    
    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M %p")
    clock.config(text=current_time)
    name.config(text="CURRENT WEATHER")
    
    
    #weather
    api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=dc85f345c49d430a8bee3c45d89b337c"
    json_data=requests.get(api).json()
    condition=json_data['weather'][0]['main']
    description=json_data['weather'][0]['description']
    temp=int (json_data['main']['temp']-273.15)
    pressure=json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    
    t.config(text=(temp,"°"))
    c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))
    
    w.config(text=wind)
    g.config(text=humidity)
    h.config(text=description)
    q.config(text=pressure)
    


# search box
search_image = PhotoImage(file="Copy of search.png")
myimage=Label(image=search_image)
myimage.place(x=20,y=20)

#textfield
textfield = tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold",),bg="black",fg="white")
textfield.place(x=50,y=40)
textfield.focus()


#icon
icon_image = PhotoImage(file="Copy of search_icon.png")
myicon = Button(image=icon_image,borderwidth=0,cursor="hand2",bg="#404040",command=getweather)
myicon.place(x=350,y=34)

#logo
logo_image= PhotoImage(file="Copy of logo.png")
mylogo = Label(image=logo_image)
mylogo.place(x=150,y=100)

#bottom-box
frame_image= PhotoImage(file="Copy of box.png")
myframe= Label(image=frame_image)
myframe.pack(padx=5,pady=5,side=BOTTOM)


#time
name=Label(root,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock=Label(root,font=("Helvetica",20))
clock.place(x=30,y=130)


#label
label1 = Label(root, text="Wind",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label1.place(x=120,y=400)

label1 = Label(root, text="Humidity",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label1.place(x=250,y=400)

label1 = Label(root, text="Description",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label1.place(x=430,y=400)

label1 = Label(root, text="Pressure",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label1.place(x=650,y=400)


t=Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)
c=Label(font=("arial",15,"bold"))
c.place(x=400,y=250)


w = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
w.place(x=120,y=430)


g = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
g.place(x=250,y=430)


h = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
h.place(x=430,y=430)

q = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
q.place(x=650,y=430)








root.mainloop()
