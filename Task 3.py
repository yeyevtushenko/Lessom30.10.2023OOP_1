# Створіть клас «Країна».
# Збережіть у класі: назву країни, назву континенту, кількість жителів країни,
# телефонний код країни, назву столиці, назву міст країни.
# Реалізуйте методи класу для введення-виведення даних та інших операцій.
print("Завдання №3")


class Country:
    def __init__(self, name, continent, population, phone_code, capital, cities):
        self.name = name
        self.continent = continent
        self.population = population
        self.phone_code = phone_code
        self.capital = capital
        self.cities = cities

    def display_info(self):
        print("Назва країни: ", self.name)
        print("Континент: ", self.continent)
        print("Кількість жителів: ", self.population)
        print("Телефонний код країни: ", self.phone_code)
        print("Столиця: ", self.capital)
        print("Міста країни:")
        for city in self.cities:
            print("  -", city)