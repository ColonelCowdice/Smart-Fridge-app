import os
import requests
import matplotlib.pyplot as plt
from datetime import datetime

api_key = 'Enter API key here'
# Create variable to get the city for the weather
city = input("Enter City for weather: ")

exclude = "minutely,daily,alerts"

# Covert the temp values to the metric system
units = "metric"

# Get latitude and longitude for the city
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
res = requests.get(url)
data = res.json() 
latitude = data['coord']['lat']
longitude = data['coord']['lon']

# Get weather data using latitude and longitude
url = f'https://api.openweathermap.org/data/2.5/onecall?lat={latitude}&lon={longitude}&exclude={exclude}&units={units}&appid={api_key}'
res = requests.get(url)
data = res.json()

# Extract hourly temperature and time data for today
hourly_temps = [hour['temp'] for hour in data['hourly'][:24]]
hourly_times = [datetime.fromtimestamp(hour['dt']).strftime('%H:%M') for hour in data['hourly'][:24]]
current_day = datetime.now().strftime('%Y-%m-%d')

# Plot hourly temperature data on a line graph(p.s the time is in Eastern time)
fig, ax = plt.subplots(figsize=(7, 6))
# fig, ax = plt.subplots()
ax.plot(hourly_times, hourly_temps)
ax.set_xlabel('Time(hours)')
ax.set_ylabel('Temperature (°C)')
ax.set_title(f'Hourly Weather Forecast for {city} on {current_day}')
plt.xticks(rotation=45)

# Save plot as PNG
if not os.path.exists('images'):
    os.makedirs('images')
filename = 'images/weather.png'
plt.savefig(filename)

# plt.show()
