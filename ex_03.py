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

    def get_categories(self):
        categorieslist = list(self.__transactions.keys())
        print(categorieslist)

    def print_sorted_transactions(self, category="defaultvalue"):
        finallist = []
        categorieslist = list(self.__transactions.keys())
        if category == "defaultvalue":
            for cat in categorieslist:
                finallist = finallist + self.__transactions[cat]
            print(sorted(finallist))
        else:
            print(sorted(self.__transactions[category]))


if __name__ == '__main__':
    myBudget = Budget("data.json")
    myBudget.get_categories()
    myBudget.print_transactions()
    myBudget.print_sorted_transactions('income')

