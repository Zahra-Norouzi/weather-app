import tkinter as tk
import requests

API_KEY = "YOUR_API_KEY"
BASE_URL = "http://api.openweathermap.org/data/2.5/"

class WeatherApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Weather App")
        self.master.geometry("300x200")

        self.city_label = tk.Label(master, text="Enter city name:")
        self.city_label.pack()

        self.city_entry = tk.Entry(master, width=20)
        self.city_entry.pack()

        self.get_weather_button = tk.Button(master, text="Get Weather", command=self.get_weather)
        self.get_weather_button.pack()

        self.weather_label = tk.Label(master, text="")
        self.weather_label.pack()

    def get_weather(self):
        city_name = self.city_entry.get()
        weather_url = f"{BASE_URL}weather?q={city_name}&appid={API_KEY}&units=metric"
        response = requests.get(weather_url)
        weather_data = response.json()

        if weather_data.get('cod') != 200:
            self.weather_label.config(text="City not found!")
            return

        main = weather_data['main']
        wind = weather_data['wind']
        weather_description = weather_data['weather'][0]['description']

        weather_text = f"City: {weather_data['name']}\n"
        weather_text += f"Weather: {weather_description}\n"
        weather_text += f"Wind speed: {wind['speed']} m/s\n"
        weather_text += f"Temperature: {main['temp']}°C"

        self.weather_label.config(text=weather_text)

root = tk.Tk()
app = WeatherApp(root)
root.mainloop()