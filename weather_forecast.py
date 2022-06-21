from pyparsing import col
import requests, pprint
import api_key, pandas


class Weather:
    """
    Create a Weather object by putting as input:
        -The apikey generated in (https://openweatherapp.org)
        -The name of a city or the latitude and longitude coordinates."""

    def __init__(self, apikey, city=None, lat=None, lon=None):
        if city:
            url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&APPID={apikey}&units=metric"
            r = requests.get(url)
            self.data = r.json()
        elif lat and lon:
            url = url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&APPID={apikey}&units=metric"
            r = requests.get(url)
            self.data = r.json()
        else:
            raise TypeError("provide either a city or lat and lon arguments")

        if self.data['cod'] != '200':
            raise ValueError(self.data['message'])


    def next_12hs(self):
        """Returns 3-hour data for the next 12 hours as a dict"""
        return self.data['list'][:4]


    def next_12hs_simplified(self):
        """
        Returns date, temperature, and sky condition every 3 hours
        for the next 12 hours as a tuple of tuples
        """
        simple_data = []
        for dicty in self.data['list'][:4]:
            simple_data.append({(f"'Date-Hour':[{dicty['dt_txt']}], 'Temp':[{dicty['main']['temp']}°C], 'Sky':[{dicty['weather'][0]['description']}]")})
            df = pandas.DataFrame(simple_data)
            
        return df

          
          
         
     
if __name__=='__main__':
    apikey = api_key.main()
    #weather = Weather(apikey=apikey, lat=4.1, lon=4.5)
    weather = Weather(apikey=apikey, city="Rome")
    #print(weather.next_12hs())
    print(weather.next_12hs_simplified())
    
    df = weather.next_12hs_simplified()
    df.to_excel('./Excel_Sample_out.xlsx',sheet_name='Hoja1')

