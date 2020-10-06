from file import Cat

animals = [
    {
        "name": "Феликс",
        "sex": "male",
        "age": 2,
        "type_animal": "dog",
    },
    {
        "name": "Барон",
        "sex": "male",
        "age": 2,
        "type_animal": "cat",
    },
    {
        "name": "Линда",
        "sex": "female",
        "age": 2,
        "type_animal": "dog",
    },
    {
        "name": "Гоша",
        "sex": "male",
        "age": 1,
        "type_animal": "parrot",
     },
    {
        "name": "Мухтар",
        "sex": "male",
        "age": 0,
        "type_animal": "dog",
    },
    {
        "name": "Сэм",
        "sex": "male",
        "age": 1,
        "type_animal": "cat",
    }
]

class OnlyCat(Cat):
    def showAnimal(self):
        if self.type_animal == "cat":
            print(self.type_animal, self.name, self.sex, self.age)

for animal in animals:
    animal_obj = OnlyCat()
    animal_obj.init_animal(animal)
    animal_obj.showAnimal()

# for animal in animals:
#     animal_obj = Cat(animal)
#     animal_obj.present_animal()