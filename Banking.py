class clerk:
    def __init__(self,account_number,current_balance):
        self.accnumber=account_number
        self.currentbal=current_balance
    def checkbalance(self):
            print("Balance amount for account number",self.accnumber,"is",self.currentbal)
class acountant(clerk):
    def __init__(self,account_number,current_balance,user,amount):
        super().__init__(account_number,current_balance)
        
        self.user=user
        self.amount=amount
    def sum1(self):
        
        if self.user=="credit":
            credit=self.currentbal+self.amount
            print("Your current balance is",credit)
        else:
            debit=self.currentbal-self.amount
            print("Your current balance is",debit)
       
class manager(acountant):
    pass
o=clerk(11022003,50000)
o.checkbalance()
ob=manager(11022003,50000,input("Enter a method credit or debit:"),int(input("Enter a amount:")))
ob.sum1()


