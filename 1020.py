#!/usr/bin/python3

dias = int(input().strip())

print("{} ano(s)".format(dias // 365))
print("{} mes(es)".format(dias % 365 // 30))
print("{} dia(s)".format(dias % 365 % 30))
