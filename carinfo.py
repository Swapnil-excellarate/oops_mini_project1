
class carShowroom:
    def __init__(self, company='audi'):
        #self.price = price
        
        self.company = company
    
    def displayStock(self, stock):
        self.stock = stock
        print("company name is {}, and {} cars are available".format(self.company, self.stock))

    def typeOfcare(self, carModel):
        self.carModel = carModel
        print("company name is {}, {} model is available".format(self.company, self.carModel))
    
    def moreInfo(self, colour, speed, engineType):
        self.color=colour
        self.speed=speed
        self.engineType=engineType

        if self.company=='audi':
            print("""Here more information about audi car 
            1. Colour = {} 
            2. Speed = {}
            3. Engine Type = {}""".format(self.color, self.speed, self.engineType))
        else:
            print('No information is available')
    #call function from secondHandCar and display information

    def showSecondhandCar(self, showsecondHandCar):
        self.showSecondhandCar=showsecondHandCar
        print("""Here more information about second hand car""".format(self.showSecondhandCar))


class secondHandCare:
    # def __init__(self):
    #     if secondHandCare==True:
    #         self.secondHandCares()
    #         self.printSecondHandCar()

    def SecondhandCar(self):
    #def __init__(self):
        self.customer = input("Enter the your name: ")
        self.carname = input("Enter the car name: ")
        self.careModel = input("Enter the car model: ")
        self.careYear = input("Enter the car year: ")
        self.careMileage = input("Enter the car mileage: ")

        print("record is sotred succesfully")

    #def SecondhandCar(self):
        #store in a dictionary
        self.secondhandcar = {'name':self.customer, 'carName': self.carname, 'carModel': self.careModel, 'carYear': self.careYear, 'carMileage': self.careMileage}
        return self.secondhandcar
    
    def printSecondHandCar(self):
        pass


class coustmer(carShowroom, secondHandCare):
    # def __init__(self):
    #     pass
    
    def request(self):
        print("""
        1. To sell secondhand(Your) car. Give us infomation
        2. To disply your record
        """)
        choise = int(input("choose any one option"))
        # if self.choise==1:
        #     print(carShowroom.displayStock())
        if choise==1:
            secondHandCare.SecondhandCar(self)   
        elif choise==2:
            print(secondHandCare.printSecondHandCar(secondHandCare))    

# BMW = carShowroom("red", "$20000", "200", "gas", "10", "BMW")
#audi1=carShowroom()
#audi1.moreInfo('red', '400Km/hr', 'petrol')
# # BMW.displayStock()
# # BMW.typeOfcare()

# a=coustmer()
# a.printSecondHandCar()