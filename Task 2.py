# Створіть клас «Місто».
# Збережіть у класі: назву міста, назву регіону, назву країни, кількість
# жителів у місті, поштовий індекс міста, телефонний код міста.
# Реалізуйте методи класу для введення-виведення даних та інших операцій.
print("Завдання №2")
class City:
    def __init__(self, name, region, country, population, zipcode, phone_code):
        self.name = name
        self.region = region
        self.country = country
        self.population = population
        self.postal_code = zipcode
        self.phone_code = phone_code

    def display_info(self):
        print("Назва міста: ", self.name)
        print("Регіон: ", self.region)
        print("Країна: ", self.country)
        print("Кількість жителів: ", self.population)
        print("Поштовий індекс: ", self.zipcode)
        print("Телефонний код: ", self.phone_code)

