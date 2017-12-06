#!/usr/bin/python3

cod = {'1': 4.00, '2': 4.50, '3': 5.00, '4': 2.00, '5': 1.50}
entr = input().split()
print("Total: R$ {:.2f}".format(cod[entr[0]] * int(entr[1])))
