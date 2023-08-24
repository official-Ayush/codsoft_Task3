import tkinter as tk
import requests
from tkinter import *


def get_weather_data():
    city_name = entry_city.get("1.0", tk.END).strip()
    api_key = "1997b6990880ff8d697ac301365c6673" 
    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

    response = requests.get(api_url)
    data = response.json()

    if data["cod"] == 200:
        
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        temp_celsius = temperature - 273.15  
        main_humidity = data["main"]["humidity"]
        pressure_hpa = data["main"]["pressure"]
        pressure_inhg = pressure_hpa * 0.02953
        country = data["sys"]["country"]

        label_output.config(text=f"Weather for {city_name}: {weather_description}\n Country:{country}\nTemperature: {temp_celsius:.2f} °C \n Humidity: {main_humidity}%\n pressure: {pressure_inhg}in",font=("Helvetica", 14))
    else:
        label_output.config(text=f"Error: {data['message']}")


root = tk.Tk()
root.title("Weather App")

welcome_label = tk.Label(root, text="Welcome!\n Please enter your city name to get the weather information.",font=("Helvetica", 14))
welcome_label.pack(pady=10)


entry_city = tk.Text(root, width=20, height=1, font=("Arial", 10))
entry_city.pack(pady=10)


button_fetch = tk.Button(root, text="Fetch Weather Data", command=get_weather_data)
button_fetch.pack()


label_output = tk.Label(root, text="")
label_output.pack(pady=10)


root.mainloop()
