class cardHolder():
    def __init__(self, cardNum, pin, firstname, lastname, balance):
        self.cardNum = cardNum
        self.pin= pin   
        self.firstname = firstname
        self.lastname = lastname
        self.balance = balance

        ### Get Method
    def get_cardNum(self):
        return self.cardNum
    def get_pin(self):
        return self.pin
    def get_firstname(self):
        return self.firstname
    def get_lastname(self):
        return self.lastname
    def get_balance(self):
        return self.balance

        ### Set Method
    def set_cardNum(self, newVal):
        self.cardNum = newVal
    def set_pin(self, newVal):
        self.pin = newVal
    def set_firstname(self, newVal):
        self.firstname = newVal
    def set_lastname(self, newVal):
        self.lastname = newVal
    def set_balance(self, newVal):
        self.balance = newVal

    def print_out(self):
        print("Card Number: ", self.cardNum)
        print("Pin Number: ", self.pin)
        print("Fist Name: ", self.firstname)
        print("Last Name: ", self.lastname)
        print("Balance: ", self.balance)