class Cars:

    def __init__(self, brand, model, year, speed=0):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self, added_speed):
        self.speed += added_speed

    def brake(self, losing_speed):
        self.speed -= losing_speed

        print(f"The {self.brand} {self.model} from {self.year} is now going at {self.speed} km/h")


Honda = Cars("Honda", "Civic", 2023)
Honda.accelerate(60)
Honda.brake(30)
