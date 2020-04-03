import random
import sys
global list1
list1 = [0,1,2,3,4,5,6,7,8]

def comp():
    c = random.randint(0,8)
    if list1[c]=='X' or list1[c]=='O':
        print("Computer Played Wrong")
        comp()
    else:
        print("Computer Played")
        list1[c] = 'X'
        print1()
        check1()
def print1():
    print(list1[0],list1[1],list1[2])
    print(list1[3],list1[4],list1[5])
    print(list1[6],list1[7],list1[8])

def check():
    if (list1[0]=='O' and list1[1]=='O' and list1[2]=='O') or (list1[0]=='O' and list1[3]=='O' and list1[6]=='O') or \
            (list1[6]=='O' and list1[7]=='O' and list1[8]=='O') or (list1[2]=='O' and list1[5]=='O' and list1[8]=='O') or \
            (list1[0]=='O' and list1[4]=='O' and list1[8]=='O') or (list1[3]=='O' and list1[4]=='O' and list1[5]=='O') or \
            (list1[2]=='O' and list1[4]=='O' and list1[6]=='O') or (list1[0]=='O' and list1[1]=='O' and list1[2]=='O') or \
            (list1[3]=='O' and list1[4]=='O' and list1[5]=='O') or (list1[1]=='O' and list1[4]=='O' and list1[7]=='O'):
        print("******U WIN******")
        sys.exit()
def check1():
    if (list1[0]=='X' and list1[1]=='X' and list1[2]=='X') or (list1[0]=='X' and list1[3]=='X' and list1[6]=='X') or \
            (list1[6]=='X' and list1[7]=='X' and list1[8]=='X') or (list1[2]=='X' and list1[5]=='X' and list1[8]=='X') or \
            (list1[0]=='X' and list1[4]=='X' and list1[8]=='X') or (list1[3]=='X' and list1[4]=='X' and list1[5]=='X') or \
            (list1[2]=='X' and list1[4]=='X' and list1[6]=='X') or (list1[0]=='X' and list1[1]=='X' and list1[2]=='X') or \
            (list1[3]=='X' and list1[4]=='X' and list1[5]=='X') or (list1[1]=='X' and list1[4]=='X' and list1[7]=='X'):
        print("*****COMPUTER WINS*****")
        sys.exit()




n1 = 8

n2 = 10
while n1>0:
    check()

    comp()
    n = int(input("Enter n where you want to place 'O':"))
    if n>8:
        print("Incorrect input")
    elif list1[n]=='X' or list1[n]=='O':
        n = int(input("The current value is already entered. Enter a new value:"))
        a = n
        while a==n:
            n = int(input("Enter again"))
        list1[n] = 'O'
        print1()
        continue
    elif n<8:
        print("U played")
        list1[n] = 'O'
        print1()
    else:
        print("MATCH TIED")
        sys.exit()
