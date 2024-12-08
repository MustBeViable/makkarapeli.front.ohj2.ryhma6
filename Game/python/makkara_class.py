from random import randint

from tabulate import tabulate

from Game.python.sql_querys.fetch_all_makkaras import fetch_all_makkaras


class Makkara:
    def __init__(self, makkara_id):
        self.makkara_id = makkara_id
        self.price = 100

    def change_price(self, price):
        self.price = price

    def get_price(self):
        return self.price


class PlaythroughMakkaras:
    def __init__(self):
        self.makkaras = []

        for makkara_i in fetch_all_makkaras():
            makkara = Makkara(makkara_i)
            self.makkaras.append(makkara)

    def show_makkara_price(self, makkara_id):
        return self.makkaras[makkara_id].get_price()

    def change_prices(self, min_price, max_price):
        for makkara in self.makkaras:
            makkara.change_price(
                        min_price + (makkara.makkara_id - 1) * ((max_price - min_price) // len(self.makkaras))
            )

    def easy_mode(self):
        self.change_prices(60, 400)

    def medium_mode(self):
        self.change_prices(100, 7000)

    def hard_mode(self):
        self.change_prices(200, 5000)

    def print_status(self):
        cars = sorted(self.makkaras, key=lambda makkara: makkara.makkara_id)
        car_info = []
        for car in cars:
            car_info.append([car.makkara_id, car.get_price()])
        print(tabulate(car_info,
                       headers=['numero', 'hinta'],
                       tablefmt="grid"))