
from datetime import datetime
from operator import attrgetter
import matplotlib.pyplot as plt


class Country:
    """ Pais ou regiao da consulta, cada pais tem uma lista com os registros diarios."""

    def __init__(self, country):
        self.country = country
        self.days = list()
        
        
    def set_day(self, population, date, cases, deaths):
        self.days.append(Day(   population = population,
                                date = date,
                                cases = cases,
                                deaths = deaths))

    def plot(self):
        print(f'  - plotando imagem de {self.country}')

        # Y = CASOS
        y_list = list()
        for day in self.days:
            y_list.append(day.cases)
        
        # X = DATA
        x_list = list()
        for day in self.days:
            x_list.append(day.date)

        #sortedArray = sorted(x_list, key=lambda x: datetime.strptime(x, '%d/%m/%y'), reverse=True)

        y = sorted(y_list, key=lambda x: [len(x), x])
        x = x_list[::-1]

        fig, ax = plt.subplots()

        ax.fill(x, y)
        #ax.grid(False, zorder=5)
        plt.savefig(f'img/{self.country}.png')
        

class Day:
    """ Registro diario para cada pais. """

    def __init__(self, population, date, cases, deaths):
        self.date = date
        self.population = population
        self.cases = cases
        self.deaths = deaths