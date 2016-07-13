import json
from Person import Person

class JSONReader(object):
    path = '/home/cfit010/Desktop/contact.json'

    def get_all(self):
        with open(self.path) as data_file:
            data = json.load(data_file)
        person_details = list()
        map1 = data["hits"]
        for key in map1:
            person = Person()
            person.set_name(str(map1[key]["Name"]))
            person.set_city(str(map1[key]["city"]))
            person.set_email_id(str(map1[key]["EmailId"]))
            person.set_phone_number(str(key))
            person_details.append(person)
        return person_details


    def get_contacts(self,number):
        with open(self.path) as data_file:
            data = json.load(data_file)
        map1 = data["hits"][number]
        person_details = Person()
        person_details.set_name(str(map1["Name"]))
        person_details.set_city(str(map1["city"]))
        person_details.set_email_id(str(map1["EmailId"]))
        person_details.set_phone_number(str(number))
        return person_details

    def get_field(self,field, value):
        with open(self.path) as data_file:
            data = json.load(data_file)
        map1 = data["hits"]
        for key in map1:
            if map1[key][field] == value:
                person = Person()
                person.set_name(str(map1[key]["Name"]))
                person.set_city(str(map1[key]["city"]))
                person.set_email_id(str(map1[key]["EmailId"]))
                person.set_phone_number(str(key))

        return person


if __name__ == '__main__':
    obj = JSONReader()
    p = obj.get_all()
    for i in p:
        print(i.get_name())

    p1 = obj.get_contacts("873459879045")
    print(p1.__dict__)

    p2 = obj.get_field("Name","ram")
    print(p2.__dict__)
