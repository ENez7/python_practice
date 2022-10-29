from models.person import Person

class Professional(Person):
    def __init__(self, name, age, profession):
        super().__init__(name, age)
        self.profession = profession
        
    def getProfession(self) -> str:
        return f'{self.name}, {self.age} years old is a {self.profession}'