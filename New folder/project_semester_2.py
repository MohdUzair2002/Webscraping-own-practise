from socket import gaierror
import time
import requests
import json
import tkinter as tk
import tkinter.font
api_key='855808198d041ffb768e9b10e445c276'
Cites='Lahore'
url=f" http://api.openweathermap.org/data/2.5/weather?q={Cites}&appid={api_key}&units=metric"

response=requests.get(url)
print(response.status_code)
print (json.dumps(response.json(), indent=4))
window = tk.Tk()
window.title("Tempy")
window.geometry("800x600")
greeting = tk.Label(text="Tempy",fg="#17706E", bg="#81B214",anchor="center")
greeting.place(x=320,y=230)
greeting1 = tk.Label(text=" Weather Forecaster",fg="green", bg="#FFE699")
greeting1.place(x=280,y=280)
window.resizable(0,0)
window.configure(bg='#206A5D')
Desired_font = tkinter.font.Font( family = "Nixie One", 
                                 size = 14, 
                                 weight = "bold")
Desired_font1 = tkinter.font.Font( family = "Audiowide", 
                                 size = 28, 
                                 weight = "bold")    
greeting.configure(font = Desired_font1) 
greeting1.configure(font = Desired_font)
time.sleep(2)
def destroy():
    button.destroy()

# greeting1.destroy()
# greeting.destroy()
# label = tk.Label(text="Name")
# label.grid(row=0, column=0)

# entry = tk.Entry(fg="yellow", bg="blue", width=50)
# entry.pack()
button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
    command=destroy
)     
button.pack()                    
window.mainloop()