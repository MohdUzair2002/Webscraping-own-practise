import time
from turtle import bgcolor, width
from typing import Sized
import requests
import json
import tkinter as tk
import tkinter.font
from tkinter import *
from PIL import Image, ImageTk
from datetime import datetime
import pytz
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

window = tk.Tk()
window.title("Tempy")
window.geometry("800x600")
greeting = tk.Label(text="Tempy",fg="#17706E", bg="Black",anchor="center")
greeting.place(x=320,y=150)
greeting1 = tk.Label(text=" Weather Forecaster",fg="white", bg="Black")
greeting1.place(x=280,y=230)
window.resizable(0,0)
window.configure(bg='Black')
Desired_font = tkinter.font.Font( family = "Nixie One", 
                                 size = 14, 
                                 weight = "bold")
Desired_font1 = tkinter.font.Font( family = "Audiowide", 
                                 size = 28, 
                                 weight = "bold")    
greeting.configure(font = Desired_font1) 
greeting1.configure(font = Desired_font)



label = tk.Label(text="City:",bg="Black",fg='white')
label.place(x=220,y=280)
label.configure(font=Desired_font1)

entry = tk.Entry(fg="black", bg="white", width=50)
entry.place(x=340,y=297,
        height=25)

# CITYNAME=entry.get()        
DateTime=datetime.today().strftime('%d-%m-%Y-%H:%M:%S')
def get_data():
   Weather()

def Weather():
    button.destroy()
    label.destroy()
    
    greeting1.destroy()
    greeting.destroy()
    
    Data = entry.get()
    api_key='855808198d041ffb768e9b10e445c276'
    # Data='Lahore'
    url=f" http://api.openweathermap.org/data/2.5/weather?q={Data}&appid={api_key}&units=metric"
    response=requests.get(url)
    s=Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    driver.get(f"https://www.google.com/search?q={Data}+time")
    T=driver.find_elements(By.CSS_SELECTOR,"div[role='heading']")
    city_time=T[1].text
    print(city_time)
    entry.destroy()
    
   
    
    image1 = Image.open(r"C:\Users\Mohammad Uzair\Desktop/download.png")
    test = ImageTk.PhotoImage(image1)
    
    label1 = tkinter.Label(image=test)
    label1.image = test

# Position image
    label1.place(x=45, y=250)
    image2 = Image.open(r"C:\Users\Mohammad Uzair\Desktop/25.jpg")
    test = ImageTk.PhotoImage(image2)
    label2 = tkinter.Label(image=test)
    label2.image = test
    label2.place(x=300, y=250)
    image3 = Image.open(r"C:\Users\Mohammad Uzair\Desktop/download.jpg")
    test = ImageTk.PhotoImage(image3)
    label3 = tkinter.Label(image=test)
    label3.image = test
    label3.place(x=500, y=250,width=300)

    Result1=response.json()["main"]["temp"]
    Result2=response.json()["main"]["temp_max"]
    Result3=response.json()["main"]["temp_min"]
    Result4=response.json()["main"]["humidity"]
    Result5=response.json()["name"]
    Result8=response.json()["sys"]['country']
    
    # print(response.status_code)
    
    Result=tk.Label(text=f"Temp:{Result1}",bg='#116562')
    Result.place(x=0,y=100,width=300,height=100)
    Result.configure(font=Desired_font1)
    def rgb_hack(rgb):
     return "#%02x%02x%02x" % rgb 
    
    Result11=tk.Label(text=f"Temp_Max:{Result2}",bg='black',fg='white')
    Result11.place(x=310,y=100,width=200,height=40)
    Result11.configure(font=Desired_font) 
    #----------------------------------------------
    Result113=tk.Label(text=f"Temp_Min:{Result3}",bg='black',fg='white')
    Result113.place(x=310,y=150,width=200,height=40)
    Result113.configure(font=Desired_font)
    Result213=tk.Label(text=f"Humidity:{Result4}",bg='black',fg='white')
    Result213.place(x=550,y=120,width=200,height=50)
    Result213.configure(font=Desired_font)
    Result513=tk.Label(text=f"Date:{DateTime[0:10]} Time:{T[1].text}",bg='black',fg='white')
    Result513.place(x=0,y=0,width=330,height=50)
    Result513.configure(font=Desired_font)
    Result613=tk.Label(text=f"City:-{Result5}",bg='black',fg='white')
    Result613.place(x=340,y=0,width=200,height=50)
    Result613.configure(font=Desired_font)
    Result713=tk.Label(text=f"Country:-{Result8}",bg='black',fg='white')
    Result713.place(x=550,y=0,width=200,height=50)
    Result713.configure(font=Desired_font)
    # print(Result1)
    print(Result11)
 
        
    return Result
button = tk.Button(
    text=" Search!",
    width=25,
    height=2,
    bg="pink",
    fg="Black",
    command=get_data
)     
button.place(x=360,y=400)

window.mainloop()
