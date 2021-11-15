class Atm:
    def __init__(self, card_number,pin):
        self.card_number = card_number
        self.pin = pin

    def check_balance(self, amount):
        print("Your balance is 50000")
        
    def withdrawl(self, amount):
        new_amount = 50000-amount
        print("You Have Withdrawn amount"+str(amount)+". your remining balance is "+str(new_amount))

def main():
    card_number = input("Insert your card number: ")
    pin_number = input("Enter your pin: ")

    new_user = Atm(card_number, pin_number)

    print("Choose your activity: ")
    print("1. Balance Enquiry 2. Withdrawl ")
    activity = int(input("Enter Amount: "))

    if(activity == 1):
        new_user.check_balance()

    elif(activity == 2):
        amount = int(input("Enter Amount: "))
        new_user.withdrawl(amount)
    
    else:
        print("Enter A Valid Number")

if __name__ == "__main__":
    main()
    