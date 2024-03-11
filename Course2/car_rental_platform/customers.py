import datetime as dt
class Customers():
    rate_types = ['Hourly', 'Daily', 'Weekly']

    def __init__(self) -> None:
        pass
    
    # This list stores the actual cars rented so far
    __customer_cars_rented = []
    
    def add_car(self, code, plate, rate_type):
        Customers.__customer_cars_rented.append({'code': code, 'plate': plate, 'rate_type': rate_type, 'time': dt.datetime.now() })

    def get_car_info(self, plate):
        car = self.find_car_by_plate(plate)
        rate_type = car['rate_type']
        time_diff = (dt.datetime.now() - car['time'])
        if rate_type == 'Hourly':
            time = time_diff.total_seconds() / 3600
        elif rate_type == 'Daily':
            time = time_diff.total_seconds() / 3600 / 24
        elif rate_type == 'Weekly':
            time = time_diff.total_seconds() / 3600 / 24 / 7
        return {'rate_type': rate_type, 'time': time}
    
    def remove_car(self, plate):
        car = self.find_car_by_plate(plate)
        Customers.__customer_cars_rented.remove(car)

    def find_car_by_plate(self, plate):
        for car in Customers.__customer_cars_rented:
            if car['plate'] == plate:
                return car
        return None
