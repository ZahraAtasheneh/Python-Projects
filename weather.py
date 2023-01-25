import requests


try:
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=35.6762&lon=139.6503&appid=79007029562c2ab46617d801d8018750")
   

except:
    print("Oops! No internet")

response_json = response.json()

#print(response_json["main"])
print(response_json["main"] ["temp"])

temp = response_json["main"] ["temp"]
temp_min = response_json["main"] ["temp_min"]
temp_max = response_json["main"] ["temp_max"]

print(f"In New York it is currntly {temp}° C")
print(f"Today's High: {temp_max}")
print(f"Today's Low: {temp_min}")

class City:
    def __init__(self, name, lat, lon, units="metric"):
        self.name= name
        self.lat=lat
        self.lon=lon
        self.units=units
        self.get_data()

    def get_data(self):
        try:
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid=79007029562c2ab46617d801d8018750")
   

        except:
            print("Oops! No internet")

#print(response_json["main"])
#print(response_json["main"] ["temp"])

        self.response_json = response.json()
        self.temp = self.response_json["main"] ["temp"]
        self.temp_min = self.response_json["main"] ["temp_min"]
        self.temp_max = self.response_json["main"] ["temp_max"]


    def temp_print(self):
        units_symbol= "C"
        if self.units == "imperial":
            units_symbol= "F"
        print(f"In {self.name} it is currntly {self.temp}° {units_symbol}")
        print(f"Today's High: {self.temp_max}")
        print(f"Today's Low: {self.temp_min}")

my_city = City("London", 51.5072, 0.1276)
my_city.temp_print()

great_city = City("Tokyo", 35.6762, 139.6503)
great_city.temp_print()


vacation_city = City("Portland", 45.5152, -122.6784, units="imperial")
vacation_city.temp_print()
print(vacation_city.response_json)


#python weather.py
#.\weather_venv\Scripts\activate
#deactivate
#      
