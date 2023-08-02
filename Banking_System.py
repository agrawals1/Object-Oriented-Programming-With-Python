from datetime import date
from random import randint
import json

persons_dict = {}
class Interest():
    
    ROI: int
    def Calculate_Amount(self, time, balance):  
        pass


class SimpleInt(Interest):

    def __init__(self, ROI):
        self.ROI = ROI

    def Calculate_Amount(self, time, balance):                      # amount after interest calculation
        return balance + (self.ROI*time*balance)/100


class CompoundInt(Interest):

    def __init__(self, ROI):
        self.ROI = ROI

    def Calculate_Amount(self, time, balance):                      # amount after interest calculation
        return balance * (pow((1 + self.ROI / 100), time))


class Account():                    

    interest: Interest                                              # Interest Object (strategy pattern)
    balance : float

    def __init__(self, accnum, balance=0):
        self.CreatedOn = '2022'                               
        self.balance = balance
        self.accnum = accnum

    def QueryAmount(self, time='0'):
        if time == '0':                                               # Time in years
            print(f"Query Amount : {self.balance}")                                       # Current amount
        else:
            time = int(time.split('.')[0]) - int(self.CreatedOn)      # YYYY.MM.DD
            amt = self.interest.Calculate_Amount(time, self.balance)
            print(f"Query Amount : {amt}")

    def SetInterest(self, interest):
        self.interest = interest


class FixedDeposit(Account):

    __acctype : str
    def __init__(self, accnum, balance=0):
        self.CreatedOn = '2020'
        self.balance = balance
        self.interest = CompoundInt(10)
        self.accnum = accnum
        self.__acctype = "FixedDeposit"

    def getacctype(self):
        return self.__acctype

    def withdraw(self, withdraw_amnt, special):
        print("Cant Withdraw from Fixed Deposit, terminate the account instead...")
        return    

    def withdraw(self, deposit_amnt):
        print("Cant Withdraw from Fixed Deposit, terminate the account instead...")
        return        
           


class SavingsAccount(Account):

    __acctype : str
    def __init__(self, accnum, balance=0):
        self.CreatedOn = '2022'     
        self.balance = balance
        self.interest = CompoundInt(6)
        self.accnum = accnum
        self.__acctype = "Savings"

    def deposit(self, deposit_amnt):
        self.balance = self.balance + deposit_amnt
        print(f"new balance = {self.balance}")

    def withdraw(self, withdraw_amnt, special):
        if (self.balance >= withdraw_amnt or special):
            self.balance = self.balance - withdraw_amnt
            print(f"new balance = {self.balance}")
        else:
            print(f"Insufficient Funds!! {self.balance}")

    def getacctype(self):
        return self.__acctype        


class CurrentAccount(Account):

    __acctype : str
    def __init__(self, accnum, balance=0):
        self.CreatedOn = '2022'     
        self.balance = balance
        self.interest = CompoundInt(3)
        self.accnum = accnum              
        self.__acctype = "Current"

    def deposit(self, deposit_amnt):
        self.balance = self.balance + deposit_amnt
        print(f"new balance = {self.balance}")

    def withdraw(self, withdraw_amnt, special):
        if (self.balance >= withdraw_amnt or special):
            self.balance = self.balance - withdraw_amnt
            print(f"new balance = {self.balance}")
        else:
            print(f"Insufficient Funds!! {self.balance}")

    def getacctype(self):
        return self.__acctype        
            

class Services():                            

    def Subscribe(self):
        pass

    def Unsubscribe(self):
        pass

    
    
class PriorityQueue(Services):
    def Subscribe(self, name):
        print(f"{name} Subscribed to service PriorityQueue")

    def Unsubscribe(self, name):
        print(f"{name} Unsubscribed from service PriorityQueue")    

class PersonalManager(Services):
    def Subscribe(self, name):
        print(f"{name} Subscribed to service PersonalManager")

    def Unsubscribe(self, name):
        print(f"{name} Unsubscribed from service PersonalManager")    

class CashDelievery(Services):
    def Subscribe(self, name):
        print(f"{name} Subscribed to service CashDelievery")

    def Unsubscribe(self, name):
        print(f"{name} Unsubscribed from service CashDelievery")    


class Person:
    __name: str
    __dob: str
    gender: str
    special : bool = False
    accountDict: dict[str, Account]        # Dictionary {accnum : account} of accounts opened by person
    services: dict[str, Services]          # Dictionary {service_name : service} of services taken by person                            
                                            
                                                                        

    def __init__(self, name, dob, gender, special):
        self.__name = name
        self.__dob = dob
        self.gender = gender
        self.accountDict = {}
        self.services = {}
        self.special = special
        persons_dict[name] = self

    def getName(self):
        return self.__name

    def CreateAccountTxt(self, path):
        with open(path, 'r') as infile:
            multiaccnt : dict[str, float] = json.load(infile)
        for acctype, deposit_amnt in multiaccnt.items():
            self.CreateAccount(acctype, deposit_amnt)    
        print("accounts created")
        self.AllAccounts()       
        
    def CreateAccount(self, acctype, deposit_amnt):
        accnum = str(randint(100000, 999999))
        if acctype == "FixedDeposit":
            acc = FixedDeposit(accnum, balance=deposit_amnt)
            self.accountDict[accnum] = acc

        elif acctype == "Savings":
            acc = SavingsAccount(accnum, balance=deposit_amnt)
            self.accountDict[accnum] = acc

        elif acctype == "Current":
            acc = CurrentAccount(accnum, balance=deposit_amnt)
            self.accountDict[accnum] = acc

        else:
            print("Such an account type is not supported currently....Stay Tuned!!")

    def Terminate(self):
        print("Enter AccNum of the account which you want to terminate...")
        accnum = str(input(f"{self.accountDict.keys()}"))
        try:
            acc = self.accountDict[accnum]
        except:
            print("account not found")
            return    
        tot_time = 2022 - int(acc.CreatedOn)
        if acc.getacctype() == "FixedDeposit":
            if tot_time < 1:
                print("Cant close FD account before 1 year")

            else:
                print("We are sorry to see you go...")
                print(f"your total balance is {acc.interest.Calculate_Amount(tot_time, acc.balance)}. Please collect it.")
                self.accountDict.pop(accnum)
                print("Your account was successfully deleted")
        else:
            print("We are sorry to see you go..............")
            print(f"Please collect your balance of Rupees {self.accountDict[accnum].QueryAmount()}")
            self.accountDict.pop(accnum)
            print("Your account was successfully deleted")

    def TerminateTxt(path):
        pass

    def AttachService(self, service_name, service : Services):
        self.services[service_name] = service
        service.Subscribe(self.__name)
            

    def DetachService(self, service_name, service : Services):
        try:
            self.services.pop(service_name)

        except ValueError:
            print("You are not subscribed to this service...")

        else:
            service.Unsubscribe(self.__name)    

    def AllServices(self):
        print(f"Current Subscriptions of {self.__name} : ")
        print(list(self.services.keys()))        

    def AllAccounts(self):
        print(f"Current Accounts of {self.__name} : ")  
        print([y.getacctype() for x,y in self.accountDict.items()])
                
        




    

if __name__ == "__main__":  

    while(True):
        print("Enter 1 for registering a person")
        print("Enter 2 for opening single account")
        print("Enter 3 for opening multiple accounts")
        print("Enter 4 for closing single account")
        # print("Enter 5 for closing multiple accounts")
        print("Enter 6 for deposit")
        print("Enter 7 for withdrawl")
        print("Enter 8 for querying account")
        print("Enter 9 for list services")
        print("Enter 10 for adding service")
        print("Enter 11 for removing a service")
        print("Enter 12 for list of accounts")
        _ = int(input())

        if _ == 1:            
            name = input("plz enter your name")
            dob = input("plz enter your DOB as DD/MM/YY")
            gender = input("plz enter you gender")
            special = input('are you the special customer?')
            person = Person(name, dob, gender, special)

        elif _ == 2:
            name = input("Enter your name")
            acctype = input("Enter account type, FixedDeposit, Savings, Current")
            amount = input("Enter initial deposit amount")
            guy = persons_dict[name]
            guy.CreateAccount(acctype, amount)

        elif _ == 3:
            name = input("Enter your name")
            guy = persons_dict[name]
            guy.CreateAccountTxt("sample.json")

        elif _ == 4:
            name = input("Enter your name")
            guy = persons_dict[name]
            guy.Terminate()

        elif _ == 5:
            pass

        elif _ == 6:
            name = input("Enter your name")
            guy = persons_dict[name]
            amnt = float(input("Amount to be deposited?"))
            print("choose the account to deposit on")
            actype = input(f"{guy.AllAccounts()}")
            for k,v in guy.accountDict.items():
                if v.getacctype() == actype:
                    v.deposit(amnt)

        elif _ == 7:
            name = input("Enter your name")
            guy = persons_dict[name]
            amnt = float(input("Amount to be withdrawn?"))
            print("choose the account to withdraw from")
            actype = input(f"{guy.AllAccounts()}")
            for k,v in guy.accountDict.items():
                if v.getacctype() == actype:
                    v.withdraw(amnt, guy.special)

        elif _ == 8:
            name = input("Enter your name")
            guy = persons_dict[name] 
            time = input("Enter projection time yyy.mm.dd")    
            print("choose the account to query from")
            actype = input(f"{guy.AllAccounts()}")
            for k,v in guy.accountDict.items():
                if v.getacctype() == actype:
                    v.QueryAmount(time)        

        elif _== 9:
            name = input("Enter your name")
            guy = persons_dict[name]
            guy.AllServices()

        elif _ == 10:
            name = input("Enter your name")
            guy = persons_dict[name]
            srvc_string = input("Enter the service you want to add PriorityQueue, PersonalManager, CashDelievery")
            if srvc_string == "PriorityQueue":
                srvc = PriorityQueue()
            elif srvc_string == "PersonalManager"    :
                srvc = PersonalManager()
            elif srvc_string == "CashDelievery":
                srvc = CashDelievery()
            else:
                print("This service is not available yet")
            guy.AttachService(srvc_string, srvc)      

        elif _ == 11:
            name = input("Enter your name")
            guy = persons_dict[name]
            srvc_string = input("Enter the service you want to remove PriorityQueue, PersonalManager, CashDelievery")            
            guy.DetachService(srvc_string, guy.services[srvc_string])

        elif _ == 12:
            name = input("Enter your name")
            guy = persons_dict[name]
            guy.AllAccounts()







    # #         acctype = input("Enter account type")
    # #         deposit_amnt = int(input("Enter amounnt to be deposited, 0 for zero balance account"))
    # #         person.CreateAccount(acctype, deposit_amnt)

    # per1 = Person("shubham", "22/05/1995", "male", True)
    # # per1.CreateAccount("FixedDeposit", 50000)
    # # per1.CreateAccount("Savings", 35000)

    # per2 = Person("sourabh", "20/03/1998", "male", False)
    # # per2.CreateAccount("Current", 70000)
    # # per2.CreateAccount("Savings", 50000)
    # # amnt = per1.accountDict[list(per1.accountDict.keys())[1]].QueryAmount("2024.12.17")
    # # service_cash = CashDelievery()
    # # service_pm = PersonalManager()

    # # per1.AttachService("CashDelievery", service_cash)
    # # per1.AttachService("PersonalManager", service_pm)    
    # # per2.AttachService("CashDelievery", service_cash)
    # # per1.DetachService("CashDelievery", service_cash)
    # # per1.AllServices()
    # # per1.AllAccounts()
    # # per1.Terminate()
    # # per1.AllAccounts()
    # # perstr = json.dumps(persons_dict, default=lambda o: o.__dict__, indent=4)
    # # print(perstr)

    # dictionary = {
    # "Current": 75000,
    # "Savings": 50000,
    # "FixedDeposit": 100000
    # }
 
    # # Serializing json
    # json_object = json.dumps(dictionary, indent=4)
    
    # # Writing to sample.json
    # with open("sample.json", "w") as outfile:
    #     outfile.write(json_object)

    # per1.CreateAccountTxt("sample.json")    
