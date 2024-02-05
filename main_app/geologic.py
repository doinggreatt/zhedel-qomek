from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from geopy.distance import geodesic
from .models import Cars, CarsPosition

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


class FindNearest():
    def __init__(self, cl_lat, cl_long):                                
        self.cl_pos = (cl_lat, cl_long)
        cl_pos = (cl_lat, cl_long)
        
    def find_nearest(self):
        cl_pos = self.cl_pos
        cars_free = []
        near_drivers = [] 

        get_cars_free = CarsPosition.objects.filter(is_free=True)
                
        if len(list(get_cars_free))>0:
            for c in get_cars_free:
                cars_free.append({'id': c.id, 'pos': (c.lat, c.long)})

        else:
            return None

        for i in range(len(cars_free)):
            car_pos =cars_free[i]['pos']
            dist = geodesic(cl_pos, car_pos).meters 
            near_drivers.append({
                    'id': cars_free[i]['id'],
                    'distance': dist 
                    })

        drivers_sorted = sorted(near_drivers, key=lambda x: x['distance'])
        returned_car = drivers_sorted[0]
        return returned_car
