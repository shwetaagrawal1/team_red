class Person(object):

    def __init__(self):
        self._name = ""
        self._phone_number = ""
        self._email_id = ""
        self._city = ""

    def set_name(self,name):
        self._name = name

    def get_name(self):
        return self._name

    def set_phone_number(self, phone_number):
        self._phone_number = phone_number

    def get_phone_number(self):
        return self._phone_number

    def set_email_id(self, email_id):
        self._email_id = email_id

    def get_email_id(self):
        return self._email_id

    def set_city(self, city):
        self._city = city

    def get_city(self):
        return self._city


if __name__ == '__main__':
    p = Person()
    p.set_city("hyd")
    p.set_name("abc")
    print(p.get_city())
    print(p.get_name())
