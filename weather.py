import requests
import datetime 
import sys 
#using the weatherbit API!
api_key = 'c576d9ac4ee1b6de9fbe752c53f180fe' 
failed_api_request = "FAILED API REQUEST\n"
invalid_api_request = "INVALID API REQUEST\n" 

#Next feature: adding support for failed API requests. 



"""
Weather Class

This class provides a way to retrieve weather information using the Weatherstack API based on a specified location and time option.

Author: [Your Name]

Date: [Current Date]

Usage:
    weather = Weather(location, timeoption)
    condition = weather.get_weather()
    print(condition)

"""
class Weather:
    def __init__(self, location):
        self.location = location
        self.today = today = datetime.date.today()

    def get_weather(self, timeoption):
        if(timeoption == 'today'):
            cond = self.get_current_condition()

            if 'success' in cond:
                sys.stderr.write(failed_api_request)
                exit() 

            cond = cond['current']['weather_descriptions']
            return cond[0]
        
        elif (timeoption == 'yesterday'):
            cond = self.get_previous_condition()

            if cond['success'] == False:
                sys.stderr.write(failed_api_request)
                exit() 
        
            cond = cond['current']['weather_descriptions']
            return cond[0] 
        
        else:
            sys.stderr.write(invalid_api_request) 
            exit() 

    def get_current_condition(self):
        request = requests.get('http://api.weatherstack.com/current?access_key='+ api_key +'&query='+ self.location +'')
        request = request.json() 
        return request 
        
    def get_previous_condition(self):
        yesterday = self.today - datetime.timedelta(days=1)
        request = requests.get('http://api.weatherstack.com/current?access_key='+ api_key +'&query='+ self.location +'&historical_date=' + str(yesterday) +'') 
        request = request.json() 
        return request

class Forecasts(Weather): 
    def __init__(self, weatherInstance): 
        self.location = weatherInstance.location

    def one_day_forecast(self):
        request = requests.get('http://api.weatherstack.com/forecast?access_key=' + api_key + '&query=' + self.location + '&forecast_days = 1')
        request = request.json() 
        forecast = request['current']['weather_descriptions']
        return forecast





waterlooWeather = Weather('Waterloo')  
print("Weather Conditions", waterlooWeather.get_weather('today'))
location_conditions = Forecasts(waterlooWeather)
print(location_conditions.one_day_forecast())



