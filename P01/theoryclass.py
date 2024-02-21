class Car:
    def __init__(self, brand, speed = 0): #creats an object
        self.brand = brand #brand is a local variable, self.sometghing is an atribute and can be seen and modified all over the class
        self.speed = speed #hacerlo cada vez, init con todos los atributos
    def set_speed(self, speed):
        self.speed = speed

    def get_speed(self):
        return self.speed

    def get_brand_nationality(self):
        if self.brand == "Renault":
            return "France"
        elif self.brand == "Ferrari":
            return "Italy"

mycar = Car("Renault", 30) #esto es llama el init
#only give you one because, self is always the object itself
#print(mycar.get_speed())
mycar.set_speed(80)
print(mycar.speed)
#print(mycar.get_speed())

print(mycar.get_brand_nationality())

yourcar = Car("Ferrari", 250)
print(yourcar.speed)#lo mismo que la linea de abajo, esta linea es como se hace
#print(yourcar.get_speed())

#varios objects to the same idea
#init to moove from class to object, it has to be there
#self is a parameter of all, its the object itself

class Ferrari(Car): #pones entre parentesis de la clase del que hereda
    def __int__(self): # si estuviese solo el self.music, como la tiene no va a subir, va directamente ahi, tenes musica pero no los otros attribute
        super().__init__("Ferrari", 100)#super va para arriba #y para unir lo que esta arriba y lo que esta abajo
        self.music = "classic"


    def make_cabrio(self):
        self.speed = 20
        self.music = "loud"
        return "Wow"

mycar = Car("Renault")
#yourcar = Ferrari() este esta mal porque falta un argument
yourcar = Ferrari("Ferrari") #como ferrari no tienen init function, va a class car, YOURE USING INHERITANCE
print(yourcar.brand)
print(yourcar.speed)
yourcar.set_speed(120)
print(yourcar.speed)
print(yourcar.make_cabrio(), "and music is", yourcar.music, "and speed is", yourcar.speed)
#print(mycar.make_cabrio(), "and music is", mycar.music, "and speed is", mycar.speed) NO FUNCIONA, porque inheritance doesnt go downsords

#the point to have different classes is to programme the differences