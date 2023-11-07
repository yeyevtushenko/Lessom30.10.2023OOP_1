# Реалізуйте клас «Людина». Збережіть у класі:
# ПІБ, дату народження, контактний телефон, місто, країну, домашню адресу.
# Реалізуйте методи класу для введення-виведення даних та інших операцій.
print("Завдання №1")

class Person:
    def __init__(self, full_name, date_of_birth, phone_number, city, country, adress):
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.phone_number = phone_number
        self.city = city
        self.country = country
        self.adress = adress

    def display_info(self):
        print("ПІБ: ", self.full_name)
        print("Дата народження: ", self.birth_date)
        print("Контактний телефон: ", self.contact_phone)
        print("Місто: ", self.city)
        print("Країна: ", self.country)
        print("Домашня адреса: ", self.home_address)

    def update_phone_number(self, new_contact_phone):
        self.contact_phone = new_contact_phone
        print("Контактний телефон оновлено.")


