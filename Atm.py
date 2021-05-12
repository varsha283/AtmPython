class Atm(object):
    def __init__(self,atmCardNo,pinNo):
        self.atmCardNo=atmCardNo
        self.pinNo=pinNo
    def CashWithdrawal(self):
        print("1000 Rupees withdrawn from the account")
    def BalanceEnquiry(self):
        print("5000 Rupees left in your account")
    
Customer1=Atm("1234567890123456","1234")
print("Your ATM card no. is "+Customer1.atmCardNo)
print("Your Pin no. is "+Customer1.pinNo)
print(Customer1.CashWithdrawal())
print(Customer1.BalanceEnquiry())

    

