class account:
    
    def __init__(self,curr_balance=0):
        self.balance=curr_balance
    
    def deposit(self,amount):
        self.balance +=amount
        print("Your new balance is ",self.balance)
    
    def withdraw(self,amount):
        if amount > self.balance:
            print( "Isufficient Balance")
            return
        self.balance -= amount
        print("Your new balance is ",self.balance)
    
    def check_balance(self):
        print("Your new balance is ",self.balance)
        
        
a= account(1000)
a.check_balance()
a.deposit(50)
a.withdraw(25)