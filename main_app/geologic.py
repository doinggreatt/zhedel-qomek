from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

class ClientStreet():
    def __init__(self, lat, long):
        self.lat = lat 
        self.long = long
        self.geolocator = Nominatim(user_agent="my_geocoder")
        self.location = self.geolocator.reverse((lat, long), exactly_one=True)
        self.output = self.calculate_street()
    def calculate_street(self):
        try:
            if self.location:
                address_components = self.location.raw['address']
                street_name = address_components.get('road', None)
                house_number = address_components.get('house_number', None)
                return f'{street_name} {house_number}'
            else:
                return None
        except GeocoderTimedOut:
            raise exception('Error') 

