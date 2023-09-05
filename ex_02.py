
class Budget:

    __transactions = []

    def print_transactions(self):
        for element in self.__transactions:

            if type(element) is float or int:
                if element >= 0:
                    print(f'You received {element} euros')
                else:
                    print(f'You spend {abs(element)} euros')
            else:
                print('Error, not number of float')

    def add_transactions(self, newtransaction):
        print(newtransaction)
        self.__transactions = self.__transactions + newtransaction

    def print_sorted_transactions(self):

        for element in self.__transactions:
            if type(element) is float or int:
                print('')
            else:
                break

        newlist = sorted(self.__transactions)

        for element in newlist:

            if type(element) is float or int:
                if element >= 0:
                    print(f'You received {element} euros')
                else:
                    print(f'You spend {abs(element)} euros')
            else:
                print('Error, not number of float')