from cardHolder import cardHolder

def print_menu():
        print("Please choose from one of the following options... ")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Show Balance")
        print("4. Exit")


def deposit(cardHolder):
        try:
            deposit = float(input("How much money would you like to withdraw: "))
            cardHolder.set_balance(cardHolder.get_balance() + deposit)
            print("Thank you for your money. Your new balance is: ", str(cardHolder.get_balance()))
        except:
            print("Invalid Input")

def withdraw(cardHolder):
        try: 
            withdraw = float(input("How much would you like to withdraw: "))
            if(cardHolder.get_balance() < withdraw):
                print("Insuficient Balance")
            else:
                cardHolder.set_balance(cardHolder.get_balance() - withdraw)
                print("Your Good to go. Your New Balance is: ", str(cardHolder.get_balance()))

        except:
            print("Invalid Input")
        
def check_balance(cardHolder):
        print("Your current balance is ", cardHolder.get_balance())

if __name__ == "__main__": 
    current_user = cardHolder("","","","","")

    ### Create a repo of cardholder
List_of_cardHolders = []
List_of_cardHolders.append(cardHolder("2131232412321310", 8888, "Ian", "Michael", 150.31))
List_of_cardHolders.append(cardHolder("324453452341322132", 1234, "Mike", "Jordan", 523.13))
List_of_cardHolders.append(cardHolder("809890381889018033", 5463, "Martha", "Stewart", 254.56))
List_of_cardHolders.append(cardHolder("243536453234323435", 9182, "Dawn", "Smith", 900.99))
    
    ### Prompt user for debit card number 
debitCardNum = ""
while True: 
        try:
            debitCardNum = input("Please Insert your Debitcard number: ")
            ### Check against repo
            debitMatch = [holder for holder in List_of_cardHolders if holder.cardNum == debitCardNum]
            if(len(debitMatch) > 0):
                current_user = debitMatch[0]
                break
            else:
                print("DebitCard Number not recognized. Please try again:")
        except:
            print("DebitCard Number not recognized. Please try again:")

    ###Promt for pin
while True: 
        try:
            userpin = int(input("Please enter your Pin: ").strip())
            if(current_user.get_pin() == userpin):
                break
            else:
             print("Invalid Pin. Please try again: ")
        except:
            print("Invalid Pin. Please try again: ")

print("Welcome ", current_user.get_firstname(), ":D" )
option = 0
while (True):
            print_menu()
            try:
                option = int(input())
            except: 
                 print("Invalid Input. Please try again: ")

            if(option == 1):
                deposit(current_user)
            elif(option == 2):
                withdraw(current_user)
            elif(option == 3):
                check_balance(current_user)
            elif(option == 4):
                    break
            else: 
                option = [0]
                print("Have a nice day :D ")