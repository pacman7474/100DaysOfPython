from car import Car
import random
SPEEDS = [5,7,10,12,15,20]
X_POS = [-500,-400,-300,-200,-100,0,100,200,300,400,500]

class Lane():
    def __init__(self):
        self.cars = []
        self.speed = random.choice(SPEEDS)
        direction = random.choice(["left","right"])
        num_cars = random.randint(3,5)
        for _ in range(num_cars):
            new_car = Car()
            if direction == "left":
                new_car.setheading(180)
                new_car.shape("car_left.gif")
            else:
                new_car.shape("car_right.gif")
            self.cars.append(new_car)


    def set_position(self,y_coord):
        for this_car in self.cars:
            x_coord = random.choice(X_POS)
            this_car.goto(x_coord,y_coord)

    def move_lane(self):
        for x in self.cars:
            x.forward(self.speed)


