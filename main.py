#створення симуляції життя
class Human:
    def __init__(self,
                 name = "Human",
                 job = None,
                 home = None,
                 car = None):
        self.name = name
        self.money = 50_000
        self.gladness = 50 #радість
        self.satiety = 50 #харчування
        self.job = job
        self.car = car
        self.home = home

    def get_home(self):
        pass
    def get_car(self):
        pass
    def get_job(self):
        pass
    def eat(self):
        pass
    def work(self):
        pass
    def shoping(self):
        pass
    def chill(self):
        pass
    def clean_home(self):
        pass
#вивід показників життєвого стану перса
    def days_indexes(self, day):
        pass
    def is_alive(self):
        pass
    def live(self, day):
        pass