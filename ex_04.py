import json


class Budget():
    filepath = ""

    def __init__(self, pathtothefile):
        self.filepath = pathtothefile
        f = open(self.filepath)
        data = json.load(f)

        for typeoftransaction in data['transactions']:
            self.__transactions[typeoftransaction['category']] = typeoftransaction['value']

        print(self.__transactions)

        print("Welcome to your app, here's your transactions history")
        categorieslist = list(self.__transactions.keys())
        for category in categorieslist:
            print(f'Element in this category : {category}')
            for element in self.__transactions[category]:
                print(element)

    __transactions = dict()

    def print_transactions(self, category="defaultvalue"):

        finallist = []
        categorieslist = list(self.__transactions.keys())
        if category == "defaultvalue":
            for cat in categorieslist:
                finallist = finallist + self.__transactions[cat]
            print(finallist)
        else:
            print(self.__transactions[category])




    def add_transactions(self, categoryfromheader, valuefromheader):
        f = open(self.filepath)
        data = json.load(f)

        datatoadd = {
             "transactions": [
                 {
                    "value": [-42],
                    "category": "transportation"
                 },
                 {
                    "value": [1234, 1234.20],
                    "category": "income"
                 },
                 {
                     "value" : valuefromheader,
                     "category" : categoryfromheader
                 }
            ]
        }




        newData = json.dumps(datatoadd, indent=4)

        with open('newdata.json', 'a') as file:
            # write
            file.write(newData)

    ## Code to get the balance of the user
    def getsolde (self):
        finallist = []
        solde = 0
        categorieslist = list(self.__transactions.keys())

        for cat in categorieslist:
            finallist = finallist + self.__transactions[cat]
        print(finallist)
        for number in finallist:
            solde = solde + number

        print(f'Your balance is : {solde} ')




    ## Code to get transactions history at first launch
    def firstlaunch(self):
        print("Welcome to your app, here's your transactions history")
        categorieslist = list(self.__transactions.keys())
        for category in categorieslist:
            print(f'Element in this category : {category}')
            for element in self.__transactions[category]:
                print(element)



if __name__ == '__main__':
    myBudget = Budget('data.json')
    # myBudget.get_categories()
    # myBudget.print_transactions()
    #myBudget.print_sorted_transactions('income')
    #myBudget.add_transactions([-12, -102.13], "corn for poney")
    #myBudget.firstlaunch()
    #myBudget.getsolde()