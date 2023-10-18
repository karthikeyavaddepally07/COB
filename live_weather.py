import requests
import tkinter as tk
from tkinter import messagebox

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # You can change the unit to 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            temperature = data['main']['temp']
            description = data['weather'][0]['description']
            result = f'Temperature: {temperature}°C\nDescription: {description.capitalize()}'
            return result
        else:
            return f'Error: {data["message"]}'
    except Exception as e:
        return f'An error occurred: {str(e)}'

def get_weather_button_click():
    city = city_entry.get()
    api_key = '789848c94ab037243ed265fe7bdbfbfe'

    if not city or not api_key:
        messagebox.showwarning("Warning", "Please enter both city and API key.")
        return

    weather_result = get_weather(api_key, city)
    result_label.config(text=weather_result)

# GUI setup
app = tk.Tk()
app.title("Weather App")

# Labels
tk.Label(app, text="City:").grid(row=0, column=0, padx=10, pady=10)
tk.Label(app, text="API Key:").grid(row=1, column=0, padx=10, pady=10)

# Entry widgets
city_entry = tk.Entry(app)
city_entry.grid(row=0, column=1, padx=10, pady=10)

api_key_entry = tk.Entry(app)
api_key_entry.grid(row=1, column=1, padx=10, pady=10)
''
# Result label
result_label = tk.Label(app, text="", wraplength=300)
result_label.grid(row=2, column=0, columnspan=2, pady=10)

# Get Weather button
get_weather_button = tk.Button(app, text="Get Weather", command=get_weather_button_click)
get_weather_button.grid(row=3, column=0, columnspan=2, pady=10)

app.mainloop()