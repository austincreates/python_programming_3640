#country, name
class City:
    def __init__(self, name = 'Unknown', pop = 0, gdp = 0):
        self.name = name
        self.pop = pop
        self.gdp = gdp

def __gt__(self, another_city):
    if self.gdp_per_capita > another_city.gdp_per_capita:
        return True
    elif self.gdp_per_capita == another_city.gdp_per_capita:
        if self.pop < another_city.pop
        return True
    return False
def __add__(self, another city):
    self.name = "New Bostonork"
    self.population += another_city.population
    self.gdp_per_capita = (self.gdp_per_capita + another_city.gdp_per_capita)/ 2

def __eq__(self, antoher_city):
    return self.population == another_city.population and self.gdp_per_capita == another_city.gdp_per_capita

new_york = City()
new_york.name = "New York"
new_york.pop = 80000
new_york.gdp = 90000
Boston = City("Boston", 60000, 80000)

print(new_york.name)

print(new_york == boston)
print(new_york > Boston)