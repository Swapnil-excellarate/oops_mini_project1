from carinfo import carShowroom, coustmer, secondHandCare    

def main():
    shop=carShowroom()
    coustmers=coustmer()
    # resell=secondHandCare()
    
    while True:
        print("""
        ---Audi Showroom---
        
        1. Check all the car features. 
        2. Car model Info.
        3. For check more info about car.
        4. sell your car to us.
        
        """)

        choise= int(input("Enter your choise :- "))

        try:
            choise=int(choise)
        except ValueError:
            print("Please enter the intiger valeu")
            continue

        if choise==1:
            shop.displayStock(10)
        elif choise==2:
            shop.typeOfcare('A1')
        elif choise==3:
            shop.moreInfo('red', '280km/hr', 'petrol')
        elif choise==4:
            #coustmer.request=secondHandCare.printSecondHandCar()
            coustmers.request()
        elif choise==5:
            break
        else:
            print("Invalid Choise, please enter valid choise")

         
if __name__=="__main__":
    main()