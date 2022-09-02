class ATM: 
    def __init__(self,name,cardnumber,pin,balance):
        self.name=name
        self.cardnumber = cardnumber
        self.pin=pin
        self.balance=balance
    def checkbalance(self):
        p=int(input('Enter the pin : '))
        if(self.pin==p):
            print('Your balance is : ' + str(self.balance)+' dollars')
        else:
            print('You entered the incorrect pin')
    def withdrawmoney(self):
        p=int(input('Enter the pin : '))
        if(self.pin==p):
            amt=int(input('Enter the amount you want to withdraw : '))
            if(amt<=self.balance):
                self.balance = self.balance - amt
                print('The new balance after withdrawel is '+str(self.balance)+' dollars')
            else:
                print('Insufiacient balance')
        else: 
            print('You entered the incorrect pin')
    def depositmoney(self):
        p=int(input('Enter the pin : '))
        if(self.pin==p):
            amt=int(input('Enter the amount you want to deposit : '))
            self.balance = self.balance + amt
            print('The new balance after withdrawel is '+str(self.balance)+' dollars')
        else: 
            print('You entered the incorrect pin')

customer1=ATM('Medha',123456,9784,500)
customer1.depositmoney()