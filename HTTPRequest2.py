import requests
import  json

url= 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&radius=500&type=restaurant&keyword=cruise&key=AIzaSyBSa0SUjt7GVytZzWuzp32_nbby0RNBoNE'

response= requests.get(url)



class TheData(object):

    def __init__(self, data_object):
        self.results = data_object['results']

    def get_results(self):
        return Results(self.results)


class Results(object):
    def __init__(self, results):
        self.results = results


results = response.json()

print( results)
data=TheData(results)

print(data)
theResult=data.get_results()

print( theResult)
