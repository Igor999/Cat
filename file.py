class Cat:
    def __init__(self, name="", sex = "", age=0, type_animal=""):
        self.name = name
        self.sex = sex
        self.age = age
        self.type_animal = type_animal

    def init_animal(self, dict):
        self.name = dict.get("name")
        self.sex = dict.get("sex")
        self.age = dict.get("age")
        self.type_animal = dict.get("type_animal")

    def present_animal(self):
       print(self.type_animal, self.name, self.age, self.sex)


# animals = [
#     {
#         "name": "Феликс",
#         "sex": "male",
#         "age": 2,
#         "type_animal": "dog",
#     },
#     {
#         "name": "Барон",
#         "sex": "male",
#         "age": 2,
#         "type_animal": "cat",
#     },
#     {
#         "name": "Линда",
#         "sex": "female",
#         "age": 2,
#         "type_animal": "dog",
#     },
#     {
#         "name": "Гоша",
#         "sex": "male",
#         "age": 1,
#         "type_animal": "parrot",
#      },
#     {
#         "name": "Мухтар",
#         "sex": "male",
#         "age": 0,
#         "type_animal": "dog",
#     },
#     {
#         "name": "Сэм",
#         "sex": "male",
#         "age": 1,
#         "type_animal": "cat",
#     }
# ]
#
# for animal in animals:
#     animal_obj = Cat()
#     animal_obj.init_animal(animal)
#     animal_obj.present_animal()