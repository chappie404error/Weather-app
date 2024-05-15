import webbrowser
import requests
import folium

api_key = "ur api key"

base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = input("city_name:")

complete_url = base_url + "appid=" + api_key + "&q=" + city_name
response = requests.get(complete_url)

data = response.json()
print(data)
lat = data["coord"]['lat']
lon = data["coord"]["lon"]

rain = data["weather"][0]['description']
wind = data["wind"]["speed"]
max_temp = data["main"]["temp_max"]
min_temp = data["main"]["temp_min"]
humidity = data["main"]["humidity"]

m = folium.Map(location=[lat, lon], zoom_start=5)
folium.Marker([lat, lon], popup=f"Rain={rain} \n"
                                f"WIND={wind} \n"
                                f"MAX TEMP={int(max_temp-273)} \n"
                                f"MIN TEMP={int(max_temp-273)} \n"
                                f"HUMIDITY={humidity}" , icon=folium.Icon(icon="home", color="red")).add_to(m)

m.save("map.html")
webbrowser.open_new_tab('map.html')
