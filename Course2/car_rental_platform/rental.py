import math
from customers import *

class Rental():

    # This list stores the selection of cars and how many in stock
    __inventory = [{'code': '1', 'name': 'Ford F150', 'hourly_rate': 8, 'daily_rate': 80, 'weekly_rate': 480, 'num_in_stock': 3},
                   {'code': '2', 'name': 'Buick Encore', 'hourly_rate': 6, 'daily_rate': 60, 'weekly_rate': 360, 'num_in_stock': 1},
                   {'code': '3', 'name': 'Tesla', 'hourly_rate': 7, 'daily_rate': 70, 'weekly_rate': 420, 'num_in_stock': 2}]

    # This list stores the status of each particular car and whether it is available (not rented)
    __available = [{'code': '1', 'plate': 'WBC524C', 'is_available': True},
                 {'code': '1', 'plate': 'YBA738F', 'is_available': True},
                 {'code': '1', 'plate': 'TRV273Z', 'is_available': True},
                 {'code': '2', 'plate': 'GDB827E', 'is_available': True},
                 {'code': '3', 'plate': 'PRS383R', 'is_available': True},
                 {'code': '3', 'plate': 'WYB473S', 'is_available': True}]

    # We use this to access the customer rentals so far
    __customer_rentals = Customers()

    def __init__(self) -> None:
        pass

    def show_inventory(self):
        print('\nAvailable Cars:')
        for n in Rental.__inventory:
            if n['num_in_stock'] > 0:
                print('Item #', n['code'], ', Name: ', n['name'], ', Hourly: ', n['hourly_rate'], ', Daily: ', n['daily_rate'], 
                      ', Weekly: ', n['weekly_rate'], ' Number Available: ', n['num_in_stock'], sep='')

    def show_rate_types(self):
        s = '\nAvailable Rates:\n'
        for n in Customers.rate_types:
            s += n + ', '
        s = s[0:len(s)-2]
        print(s + '\n')

    def rent_car(self, code, rate_type, count):
        car_inv = self.find_inv_by_code(code)
        if car_inv == None:
            print('That is not a valid Item #')
        elif not rate_type in Customers.rate_types:
            print('That is not a valid rate type')
        elif not (count.isnumeric() and math.floor(float(count)) == float(count) and int(count) > 0):
            print('That is not a valid count')
        else:
            if car_inv['num_in_stock'] >= int(count):   
                for n in range(int(count)):
                    car = self.find_avail_by_code(code)
                    Rental.__customer_rentals.add_car(code, car['plate'], rate_type)
                    car['is_available'] = False
                    car_inv['num_in_stock'] -= 1
                    print('Car with licence plate', car['plate'], 'rented', rate_type)
            else:
                print("Sorry, we don't have that many of that vehicle available")            

    def return_car(self, plate):
        car = self.find_avail_by_plate(plate)
        if car == None:
            print('That plate number has not been rented')
        else:
            car_inv = self.find_inv_by_code(car['code'])
            car_info = Rental.__customer_rentals.get_car_info(car['plate'])
            rate_type = car_info['rate_type']
            if rate_type == 'Hourly':
                total = car_info['time'] * car_inv['hourly_rate']
            elif rate_type == 'Daily':
                total = car_info['time'] * car_inv["daily_rate"]
            elif rate_type == 'Weekly':
                total = car_info['time'] * car_inv["weekly_rate"]              
            Rental.__customer_rentals.remove_car(car['plate'])
            car['is_available'] = True
            car_inv['num_in_stock'] += 1
            print('Car with licence plate', car['plate'], 'returned')
            print('Bill for this car is $', round(total, 2))

    def find_inv_by_code(self, code):
        for n in Rental.__inventory:
            if (n['code'] == code):
                return n
        return None
    
    def find_avail_by_plate(self, plate):
        for n in Rental.__available:
            if n['plate'] == plate and n['is_available'] == False:
                return n
        return None
    
    def find_avail_by_code(self, code):
        for n in Rental.__available:
            if n['code'] == code and n['is_available'] == True:
                return n
        return None
