# Weather-Forecast
This pure programming project in **Python** language consists of obtaining climatic data from a city in the world or from a certain latitude and longitude coordinate. The data for the next 12 hours is obtained in four sections of forecasts for the next three hours.
For this purpose the user must:
-	Get your API key (called apikey in the program) from https://openweatherapp.org
-	Wait a couple of hours for the apikey to be activated
-	Create a weather object using the previously generated API key and the chosen city, or the chosen latitude and longitude coordinate
   
   
Examples of creating a weather object:

```sh
python3 weather_forecast.py

weather1 = Weather(apikey= "29932039203320", city="Madrid") 
```

```sh
weather2 = Weather(apikey="93934993943944", lat=41.1, lon=-4.1)
```
In this case, there is an API key (called apikey in the program), but remember that each person must generate their key.

***

To get complete weather data for the next 12 hours: 
```sh
weather1.next_12hs()
```


To obtain simplified data for the next 12 hours: 
```sh
weather1.next_12hs_simplified()
```


---
If it were desirable to generate an Excel file with the data for the next 12 hours divided into four three-hour parts, It would be used, for example:
```sh
df = time.next_12hs_simplified()
df.to_excel('./Excel_Sample_out.xlsx', sheet_name='Sheet1')
```


