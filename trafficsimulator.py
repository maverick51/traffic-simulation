import random


class Road(object):
    """Controls what moves and does not move along a road."""
    road_length = 999
    current_road_array = []
    cumulative_road_array = []

    def __init__(self):
        """Initializes road contents with 0 if no car and car number if their is a car."""
        array_count = 0
        car_count = 0
        car_num = 30
        while array_count <= 999:  # set road empty of cars and add cars in proper places
            if (car_count == 25) and (car_num > 0):
                self.current_road_array.append(Car(car_num, True, array_count, array_count + 5))
                self.current_road_array.append(Car(car_num, True, array_count, array_count + 5))
                self.current_road_array.append(Car(car_num, True, array_count, array_count + 5))
                self.current_road_array.append(Car(car_num, True, array_count, array_count + 5))
                self.current_road_array.append(Car(car_num, True, array_count, array_count + 5))
                car_count = 0
                array_count += 5
                car_num -= 1
            else:
                self.current_road_array.append(Car(0, False))
                array_count += 1
                car_count += 1

    def move_car(self, rate):
        pass

    def check_random_slow_down(self):
        number = random.randint(1, 10)
        if number == 1:
            return True
        else:
            return False

    def check_end_of_road(self, a_car):
        if a_car.front_end == 999:
            return True
        else:
            return False

    def should_car_stop(self, car_to_check, front_car):
        if front_car.rear_end == car_to_check.front_end + 1:
            return True
        else:
            return False


class Car(object):
    """Car object that keeps track of speed and its number."""
    car_speed = 0
    car_number = 0
    real_car = False
    front_end = 0
    rear_end = 0

    def __init__(self, number, real_car, front, rear):
        self.car_number = number
        self.real_car = real_car
        self.front_end = front
        self.rear_end = rear


class Simulation(object):
    time = 0


if __name__ == '__main__':
    count = 0
    road = Road()
    print("The array is size: {}".format(len(road.current_road_array)))
    while count <= len(road.current_road_array) - 1:
        print(road.current_road_array[count].car_number)
        count += 1
