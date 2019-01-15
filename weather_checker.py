import requests
loc = input("Where are you?")

if "," in loc:
    loc1 = loc[0:loc.find(",")+1]
    loc2 = loc[loc.find(",")+1:]
    url = "https://api.openweathermap.org/data/2.5/weather?q=" + loc1 + "," + loc2 + "&appid=03b4149f3b619dcdeea070bee44d1963"
else:
    url = "https://api.openweathermap.org/data/2.5/weather?q=" + loc + "&appid=03b4149f3b619dcdeea070bee44d1963"
response = requests.get(url)
if response.status_code != 200:
    print("You spelled the city wrong [e.g New Yrok] , or you did not type in a city [e.g California], or you did not include a comma between the city and its state/country [e.g New York NY instead of New York, NY] . Try again.")
else:
    json_response = response.json()
    temp = float(json_response["main"]["temp"])
    tempF = round(((temp - 273.15)*(9/5) + 32), 2)
    tempC = round((temp-273.15), 2)
    print("The weather in " + loc + " is currently " + str(tempF) + " degrees Fahrenheit/" + str(tempC) + " degrees Celsius.")
