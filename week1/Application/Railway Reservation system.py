import random
import csv

class Train:
    
    def __init__(self):
        self.train_name = ""
        self.wclass = ""
        self.cost = 0
        self.resno = 0 
        self.name = ""
        self.age = 0
        self.cl =""
        self.cp =""
        self.sp = 0
        self.avl1=180
        self.avl2=180
        self.stats=""
        self.ti=0
    
    def customername(self):
        self.name = input("Enter your name: ").strip()
    
    def customer_age(self):
        self.age = int(input("Enter your age: "))
        
    def trains_available(self):
        chance = 1
        while(chance == 1):
            chance = 0
            print("Trains available: \n1.Train 10020 \n2.Train 21092 \n3.Train 18290\n")
            choice = int(input("enter your choice of Train\n"))
            if choice == 1:
                    print("Train 10020\n")
                    self.train_name = 10020
            elif choice == 2:
                    print("Train 21092\n")
                    self.train_name = 21092
            elif choice == 3:
                    print("Train 18290\n")
                    self.train_name = 18290
            else:
                print("Enter the correct choice\n")
                chance = 1 
                
    def classes(self):
        try:
            with open("Reservation.csv") as f:
                mycsv = csv.reader(f)
                for row in mycsv:
                    self.avl1 = int(row[-2])
            with open("Reservation.csv") as f:
                mycsv = csv.reader(f)
                for row in mycsv:
                    self.avl2=int(row[-1])
        except FileNotFoundError:
            self.avl1=180
            self.avl2=180          
        print(f"The following Classes are available:\n1.AC CHAIRCAR:-\tcost = Rs.800\tavailable seats = {self.avl1}\n2.SECOND CLASS\tcost = Rs.400\tavailable seats = {self.avl2}\n3.UNRESERVERD\tcost = Rs.200\n")
        chance = 1
        self.cost = 0
        while(chance ==1):
            chance = 0
            self.cl = int(input("Select the class you would like to travel:\n"))
            self.ti = int(input("Enter no of ticket u would like to book:\n"))
            if self.cl == 1:
                self.cost = self.cost + (800*self.ti)
                self.resno = random.randrange(10000,99999)
                self.cl = "AC CHAIRCAR"
                print(f"Name:{self.name}\nAge:{self.age}\nAC CHAIRCAR\nTotal Cost of ticket(s) = {self.cost}\nReservation No:{self.resno}\nNo of tickets:{self.ti}")
                if self.avl1 > 0:
                    self.cp =random.randrange(1,3)
                    self.sp =random.randrange(1,60)
                    print(f"coach position is : A{self.cp}")
                    print(f"seat position is :{self.sp}")
                    self.avl1 = self.avl1-1
                    self.stats ="confirmed"
                else:
                    self.stats ="waiting list"        
            elif self.cl == 2:
                self.cost = self.cost + (400*self.ti)
                self.resno = random.randint(10000,99999)
                self.cl = "SECOND CLASS"
                print(f"Name:{self.name}\nAge:{self.age}\nSECOND CLASS\nTotal self.Cost of ticket(s) = {self.cost}\nReservation No:{self.resno}\nNo of tickets:{self.ti}")
                if self.avl2 > 0:
                    self.cp =random.randrange(1,3)
                    self.sp =random.randrange(1,60)
                    print(f"seat confirmed\ncoach position is : B{self.cp}")
                    print(f"seat position is :{self.sp}")
                    self.avl2=self.avl2-1
                    self.stats ="confirmed"
                else:
                    self.stats ="waiting list" 
                    print("waiting list")
            elif self.cl == 3:
                self.cost = self.cost + (200*n)
                self.resno = random.randint(10000,99999)
                self.cl = "UNRESERVERED"
                print(f"Name:{self.name}\nAge:{self.age}\nUNRESERVERD\nTotal Cost of ticket(s) = {self.cost}\nReservation No:{self.resno}\nNo of tickets:{self.ti}")                            
            else:
                print("Enter the correct class\n")
                chance = self.avl1=180
        self.avl2=180
            
    def database(self):
        with open("Reservation.csv", "a") as file:
            writer = csv.DictWriter(file, fieldnames=["Name", "Age","Train","Class","Cost","no of tickets","Coach no","Seat no","PNR no","Status","avl in fc","avl in sc"])
            writer.writerow({"Name": self.name, "Age": self.age, "Train" : self.train_name, "Class" : self.cl, "Cost" : self.cost,"no of tickets":self.ti,"Coach no":str(self.cp),"Seat no":self.sp,"PNR no": self.resno,"Status" :self.stats ,"avl in fc": self.avl1,"avl in sc":self.avl2})
    
    def cancelation(self):
        L=[]
        j=input("enter the PNR no: ")
        with open("Reservation.csv", "r") as F:
            ro = csv.reader(F)
            for i in ro:
                L.append(i)
            for i in L:
                if i[-4]==j:
                    L.remove(i)
                    break
            with open("Reservation.csv","w") as F:
                wo = csv.writer(F)
                wo.writerows(L)
                     
class PNR:
    
    def search(self):
        with open("Reservation.csv") as f:
            reader = csv.reader(f)
            i=input("enter the PNR no: ")
            for row in reader:
                if(row[-4]== i):
                    print(row[-3])

        
        

def menu():
    tr=Train()
    se=PNR()
    print("\nRailway Reservation system\n")
    chance = 1
    while(chance == 1 ):
        chance = 0
        print("The following services are provided\n1.Reservation\n2.PNR check\n3.cancelation of ticket\n")
        op = int(input("enter the service that you want: "))
        if op == 1:
            print("\nReservation Service has been selected\n")
            tr.customername()
            tr.customer_age()
            tr.trains_available()
            tr.classes()
            tr.database()
        elif op == 2:
            print("PNR check service has been selected\n")
            se.search()
        elif op == 3:
            print("Cancelation of Ticket services is selected")
            tr.cancelation()
            
        else:
            print("enter the available choice")
            
menu()
        
        