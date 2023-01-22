

## From user get the place ID, from there use the search radius to look for all the mental health facitilities

# Depending on the categories
# We can offer, physciastrist, hospital, clubs (pottery,cycling,swimming,music), parks to go on walks


#GMAPS API CLIENT
from urllib.parse import urlencode
import requests
import json
GOOGLE_API_KEY = 'AIzaSyBdPwSklxcsSD-QaExwKkCp2CgkxpHcoQU'


class GoogleMapsClient(object):
    lat = None
    lng = None
    data_type = 'json'
    location_query = None
    api_key = None
    
    def __init__(self, api_key=None, address=None):
        if api_key == None:
            raise Exception("API key is required")
        self.api_key = api_key
        self.location_query = address
        if self.location_query != None:
            self.extract_lat_lng()
    
    def extract_lat_lng(self, location=None):
        loc_query = self.location_query
        if location != None:
            loc_query = location
        endpoint = f"https://maps.googleapis.com/maps/api/geocode/{self.data_type}"
        params = {"address": loc_query, "key": self.api_key}
        url_params = urlencode(params)
        url = f"{endpoint}?{url_params}"
        r = requests.get(url)
        if r.status_code not in range(200, 299): 
            return {}
        latlng = {}
        try:
            latlng = r.json()['results'][0]['geometry']['location']
        except:
            pass
        lat,lng = latlng.get("lat"), latlng.get("lng")
        self.lat = lat
        self.lng = lng
        return lat, lng
    
    def search(self, keyword, radius, location=None):
        lat, lng = self.lat, self.lng
        if location != None:
            lat, lng = self.extract_lat_lng(location=location)
        endpoint = f"https://maps.googleapis.com/maps/api/place/nearbysearch/{self.data_type}"
        params = {
            "key": self.api_key,
            "location": f"{lat},{lng}",
            "rankby":"distance",
            "keyword": keyword
        }
        params_encoded = urlencode(params)
        places_url = f"{endpoint}?{params_encoded}"
        r = requests.get(places_url)
        if r.status_code not in range(200, 299):
            return {}
        return r.json()

    def distance_time(self, curr_location,des_location):
        curr_loc = self.location_query
        endpoint = f"https://maps.googleapis.com/maps/api/distancematrix/{self.data_type}"
        params = {
            "key": self.api_key,
            "origins": curr_location,
            "units":"metric",
            "destinations": des_location
        }
        params_encoded = urlencode(params)
        places_url = f"{endpoint}?{params_encoded}"
        r = requests.get(places_url)
        if r.status_code not in range(200, 299):
            return {}
        return r.json()
    
    
# USER_ADRESS = 'M1P4Z3'
# USER_PLACE = 'psychiatrist'

# client = GoogleMapsClient(api_key=GOOGLE_API_KEY, address=USER_ADRESS)

# #aaresults = client.search(keyword="parks", radius=10000)['results'][0]['name']
# testing = client.search(keyword=USER_PLACE, radius=10000)['results']

# potential_places = []
# dummy = []
# for i in range(len(testing)):
#     potential_places.append(testing[i]['name'])
#     dummy.append(testing[i]['place_id'])

# print(potential_places)
# dist = client.distance_time(curr_location =USER_ADRESS,des_location=potential_places[0] )



# bins = {"Level 1":["parks","movies"],"Level 2": ["swimming"],"Level 3":["mental health"]}
# # Currently the rating of the locations is not considered, something to look at to ensure quality services/expierences 
