class car:
    color = "",
    varient ="",
    brand= "ABC",
    model = ""
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def applyBrake(self):
        return "Brake Applied"
  
    def acclerate(self):
        return "Speed Increased!!"

 #inheritence syntax (BaseClass)   
class bmw(car):
    def __init__(self, brand, model, engine , noOfSeat):
        super().__init__(brand, model)
        self.engine = engine
        self.noOfSeat = noOfSeat

    def display(self):
        print("The Car has "+ self.engine + self.noOfSeat+ " Seats")

    def brake(self):
        b= super().applyBrake()
        return b
        print("New breaks ")

bmw1 = bmw("BMW","M1","V8","5")
print(bmw1.applyBrake())
print(bmw1.acclerate())
bmw1.display()

print(bmw1.engine)
print(bmw1.model)
print(bmw1.brand)


