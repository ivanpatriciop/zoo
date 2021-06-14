class Animal:
    def __init__(self,name, age, health = 100, happiness = 0):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness
        
    def display_info(self):
        print(f"Nombre: {self.name}, Edad:{self.age}, Salud:{self.health}, Felicidad: {self.happiness}")
        return self
    
    def feed(self):
        self.health += 10
        self.happiness +=10
        return self

class Tiger(Animal):
    def __init__(self, name, age,color, health= 80, happiness= 20):
        super().__init__(name, age, health, happiness)
        self.color = color
    
    def display_info(self):
        print(f"Nombre: {self.name}, Edad:{self.age}, Color: {self.color}, Salud:{self.health}, Felicidad: {self.happiness}")
        return self
    
    def feed(self):
        self.health += 5
        self.happiness += 5
        return self
            
class Lion(Animal):
    def __init__(self, name, age, strength, health=20, happiness=10):
        super().__init__(name, age, health, happiness)
        self.strength = strength
        
        
    def display_info(self):
        print(f"Nombre: {self.name}, Edad:{self.age}, Strength: {self.strength}, Salud:{self.health}, Felicidad: {self.happiness}")
        return self
        
    def feed(self):
        self.health += 15
        self.happiness += 15
        return self
        
class Bear(Animal):
    def __init__(self, name, age, health=80, happiness=80):
        super().__init__(name, age, health=health, happiness=happiness)
        
    def feed(self):
        self.health += 4
        self.happiness += 4

class Zoo:
    def __init__(self, zoo_name):
        self.animals= []
        self.name= zoo_name
        
    def add_lion(self, name, age, strength):
        self.animals.append(Lion(name, age, strength))
        
    def add_tiger(self, name, age,color):
        self.animals.append(Tiger(name, age, color) )

    def add_bear(self, name):
        self.animals.append(Tiger(name))

    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()
        
zoo1 = Zoo("John's Zoo")
zoo1.add_lion("Nala", 22, 50)
zoo1.add_lion("Simba", 10, 50)
zoo1.add_tiger("Rajah", 5, "Blanco")
zoo1.add_tiger("Shere Khan", 2, "Naraja")
zoo1.print_all_info()
        

