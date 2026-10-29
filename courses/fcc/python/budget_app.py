# You should have a Category class that accepts a name as the argument.
class Category:
    def __init__(self, name):
        self.name = name
# The Category class should have an instance attribute ledger that is a list, and contains the list of transactions.
        self.ledger = []

# The Category class should have the following methods:

# A deposit method that accepts an amount and an optional description. 
#If no description is given, it should default to an empty string. 
#The method should append an object to the ledger list in the form of {'amount': amount, 'description': description}.

    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount, 'description': description})
# A withdraw method that accepts an amount and an optional description 
#(default to an empty string). The method should store in ledger the amount passed in as a negative number, and should return True if the withdrawal succeeded and False otherwise.
# A get_balance method that returns the current category balance based on ledger.
# A transfer method that accepts an amount and another Category instance, withdraws the amount with description Transfer to [Destination], deposits it into the other category with description Transfer from [Source], where [Destination] and [Source] should be replaced by the name of destination and source categories. The method should return True when the transfer is successful, and False otherwise.
# A check_funds method that accepts an amount and returns False if it exceeds the balance or True otherwise. This method must be used by both the withdraw and transfer methods.
# When a Category object is printed, it should:

# Display a title line of 30 characters with the category name centered between * characters.
# List each ledger entry with up to 23 characters of its description left-aligned and the amount right-aligned (two decimal places, max 7 characters).
# Show a final line Total: [balance], where [balance] should be replaced by the category total.

if __name__ == "__main__":
    food = Category("Food")
    food.deposit(20, "groceries")
    print(food)
    print(food.ledger)
    