class Person:
    def __init__(self, name, deposit=1000, loan=0):
        self.name = name
        self.deposit = deposit
        self.loan = loan

    def __str__(self):
        return f"Person (name: {self.name}, deposit: {self.deposit}, loan: {self.loan})"


class House:
    def __init__(self, ID, price, owner=None):
        self.ID = ID
        self.price = price
        self.owner = owner 
        self.status = "for sale"

    def sale(self, buyer, loan_amount=None):
        if loan_amount is None:
            if buyer.deposit >= self.price:
                self.owner.deposit += self.price
                self.owner = buyer
                self.status = "sold"
                self.owner.deposit -=self.price
                print(f"------- Apartment #{self.ID} sold to {buyer.name} for {self.price}.✅ -------")
            else:
                print(f"------- {buyer.name} cannot afford the apartment!❌ -------")
        else:
            if loan_amount >= self.price:
                self.owner.deposit += self.price
                self.owner = buyer
                self.status = "sold on loan"
                buyer.loan += loan_amount
                print(f"------- Apartment #{self.ID} sold to {buyer.name} for {self.price} with a loan of {loan_amount}.✅ -------")
            else:
                print(f"------- {buyer.name} cannot afford the apartment with the specified loan amount!❌ -------")

    def __str__(self):
        return f"House (ID: {self.ID}, price: {self.price}, owner: {self.owner}, status: {self.status})"

# Person objects
seller = Person("Morpheus")
buyer = Person("Neo", 125000)

# House objects with the seller as the owner
apartment = House(ID="777", price=120000, owner=seller)
apartment2 = House(ID="888", price=130000, owner=seller)

# Initial information
print("Initial Information:")
print(f"Seller's starting info: {seller}")
print(f"Buyer's starting info: {buyer}")
print(f"Apartment's starting info: {apartment}")



# Sale without a loan
print("\nAfter Sale (Without Loan):")

apartment.sale(buyer)
print(f"Seller's updated info: {seller}")
print(f"Buyer's updated info: {buyer}")
print(f"Apartment's updated info: {apartment}")



# Sale with a loan
print("\nAfter Sale (With Loan):")

apartment2.sale(buyer, 135000)
print(f"Seller's updated info: {seller}")
print(f"Buyer's updated info: {buyer}")
print(f"Apartment's updated info: {apartment}")
