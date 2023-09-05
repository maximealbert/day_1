def print_sorted_transactions(transactions):
    newlist = sorted(transactions)

    for element in newlist:

        if type(element) is float or int:
            if element >= 0:
                print(f'You received {element}')
            else:
                print(f'You spend {element}')
        else:
            print('Error, not number of float')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_sorted_transactions([512, 34, -123, 0, 42.08, -12])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
