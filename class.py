class Car(object):

    def __init__(self,model,color,company,speedlimit):
        self.color=color
        self.model=model
        self.company=company
        self.speedlimit=speedlimit

    def start(self):
        print("started") 

    def stop(self):
        print("car stoped")

    def accelaration(self):
        print("car is accelarating")

    def change_gear(self,geartype):
        print("gear changed")

audi=Car("a6","black","audi","250")
print(audi.start())        


