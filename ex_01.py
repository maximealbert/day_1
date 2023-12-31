def print_transactions(transactions):
    for element in transactions:

        if type(element) is float or int:
            if element >= 0:
                print(f'You received {element} euros')
            else:
                print(f'You spend {abs(element)} euros')
        else:
            print('Error, not number of float')


def print_sorted_transactions(transactions):

    newlist = sorted(transactions)

    for element in newlist:

        if type(element) is float or int:
            if element >= 0:
                print(f'You received {element} euros')
            else:
                print(f'You spend {abs(element)} euros')
        else:
            print('Error, not number of float')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_transactions([512, -12, 42.08])
    print_sorted_transactions([512, 34, -123, 0, 42.08, -12])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
