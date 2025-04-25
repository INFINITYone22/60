class Temperature:
    def __get__(self, instance, owner):
        return instance._temperature

    def __set__(self, instance, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero.")
        instance._temperature = value

class Thermometer:
    temperature = Temperature()

    def __init__(self, initial_temperature):
        self.temperature = initial_temperature

therm = Thermometer(25)
print(therm.temperature)

therm.temperature = 30
print(therm.temperature)

try:
    therm.temperature = -300
except ValueError as e:
    print(e)
