class Customer:
    def __init__(self, name, wallet, age, drunkenness_level):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness_level = drunkenness_level

    def reduce_wallet(self, amount):
        self.wallet -= amount
    

    def increase_alcohol_level(self, alcohol_level):
        self.drunkenness_level += alcohol_level
        return self.drunkenness_level

    def refuse(self, alcohol_level):
        alcohol_level = 10
        if alcohol_level >= self.drunkenness_level:
            return ("LEAVE")