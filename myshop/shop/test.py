class Bank:
    amount = 0
    bank_name = 'Central bank'
    intrest_rate = 0.1
    def __init__(self,name):
        
    
        self.name = name
        print(f"{__class__.bank_name}")
        print(f"Account for {self.name}. You can withdraw or deposit")
    
    def __str__(self):
        return f"Account for {self.name}"
    
    def deposit(self,deposit_money):
        self.amount += deposit_money
        print(f"Deposit successful, avilable balance :{self.amount}")
    
    def withdraw(self, withdraw_money):
        if self.amount >= 0:
            self.amount -= withdraw_money
            print(f"Withdrawing successful, avilable balance :{self.amount}")
        else:
            print("Not enough money")
    
class NewBank(Bank):
    bank_name = ""
    def __init__(self,name):
    
        self.bank_name = name
        print(f"Bank {self.bank_name} created under {super().bank_name}")
    
    

d = {'age':1}
print(d['age'])