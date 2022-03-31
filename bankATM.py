class ATM:
    def __init__(self,cardnumber,pin):
        self.cardnumber=cardnumber
        self.pin=pin
    def checkbalance(self):
        print("your balance is 500000")

    def withdraw_amount(self,amount):
        newamount=500000-amount
        print("you have withdrawn amount"+str(amount)+"your remaining balance is"+str(newamount))   

def main():
        cardnumber=input("enter your card number")  
        pinnumber=input("enter your pin number")  
        newuser=ATM(cardnumber,pinnumber)
        print("choose your action 1 is for balance inquery and 2 is for withdraw")
        activity=int(input("enter your activity number"))
        if (activity==1):
            newuser.checkbalance() 
        elif (activity==2):
            amount=int(input("enter the withdrawal amount"))
            newuser.withdraw_amount(amount)
        else:
            print("enter a valid activity number")

if __name__=="__main__":
        main()                        
