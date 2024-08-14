import tkinter as tk
from tkinter import ttk
import requests

# Constants for API
API_KEY = '7635c80c730937a3bc9693b23f9ac8b7'
API_URL = 'http://api.openweathermap.org/data/2.5/weather'

def fetch_weather():
    city = city_entry.get()
    unit = unit_var.get()
    if unit == "Celsius":
        unit_param = 'metric'
    else:
        unit_param = 'imperial'
    
    params = {
        'q': city,
        'appid': API_KEY,
        'units': unit_param
    }
    
    response = requests.get(API_URL, params=params)
    data = response.json()
    
    if data['cod'] == 200:
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        
        temp_label.config(text=f"Temperature: {temp}°{unit[0]}")
        humidity_label.config(text=f"Humidity: {humidity}%")
        wind_label.config(text=f"Wind Speed: {wind_speed} m/s")
    else:
        temp_label.config(text="City not found.")
        humidity_label.config(text="")
        wind_label.config(text="")

# Create main window
root = tk.Tk()
root.title("Weather App")
root.geometry("300x200")
root.configure(bg="#f0f0f0")

# City input
city_label = tk.Label(root, text="Enter City:", bg="#f0f0f0")
city_label.pack(pady=5)

city_entry = tk.Entry(root, width=20)
city_entry.pack(pady=5)

# Units option menu
unit_var = tk.StringVar(value="Celsius")
unit_menu = ttk.OptionMenu(root, unit_var, "Celsius", "Celsius", "Fahrenheit")
unit_menu.pack(pady=5)

# Fetch button
fetch_button = tk.Button(root, text="Show Weather", command=fetch_weather, bg="#4CAF50", fg="white")
fetch_button.pack(pady=10)

# Weather information labels
temp_label = tk.Label(root, text="", bg="#f0f0f0")
temp_label.pack(pady=5)

humidity_label = tk.Label(root, text="", bg="#f0f0f0")
humidity_label.pack(pady=5)

wind_label = tk.Label(root, text="", bg="#f0f0f0")
wind_label.pack(pady=5)

# Run the main loop
root.mainloop()
