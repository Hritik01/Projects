st_list = ['AP','AR','AS','BR','CT','GA','GJ','HR','HP',
'JK','JH','KA','KL','MP','MH','MN','ML','MZ','NL','OR','PB','RJ','SK','TN','TG','TR','UT','UP','WB']
import random
available = [0,1,2,3,4,5,6,7,8]
a_list = ['0','1','2','3','4','5','6','7','8']
position = 0
letter = 0
def printl():
    print(a_list[0],a_list[1],a_list[2])
    print(a_list[3],a_list[4],a_list[5])
    print(a_list[6],a_list[7],a_list[8])
printl()
letters = [chr(i) for i in range(65,91)] + [chr(i) for i in range(97,123)]

def play_user():
    l = input("Enter position and the letter(with space):").split(' ')
    position = l[0]
    letter = l[1]
    try:
        if int(position) in available and letter in letters:
            a_list[int(position)] = letter.upper()
            available.remove(int(position))
            return int(position)

        else:
            print("Input wapas dal yaar")
            play_user()
    except:
        print("Exception raised")
    printl()


def play_comp():
    position = random.choice(available)
    letter = random.choice(letters)
    if int(position) in available and letter in letters:
        a_list[int(position)] = letter.upper()
        available.remove(int(position))
    printl()
    return int(position)


def toss():
    if random.choice([1,2])==1:
        print("Comp wins toss")
        first,second = 'comp','user'
        return  first,second
    else:
        print("User wins toss")
        first,second = 'user','comp'
        return first,second
def check(p):
    count = 0
    if p not in (0,1,2) :
        if a_list[p] + a_list[p-3] in st_list or a_list[p-3] + a_list[p] in st_list:
            count=count+1
    if p not in (6,7,8):
        if a_list[p] + a_list[p+3] in st_list or a_list[p+3] + a_list[p] in st_list:
            count=count+1
    if p not in (0,3,6):
        if a_list[p] + a_list[p-1] in st_list or a_list[p-1] + a_list[p] in st_list:
            count=count+1
    if p not in (2,5,8):
        if a_list[p] + a_list[p+1] in st_list or a_list[p+1] + a_list[p] in st_list:
            count=count+1
    return count

def compare(user_count,comp_count):
    if user_count>comp_count:
        print("User Wins")
    else:
        print("Computer Wins")

user_count = 0
comp_count = 0
f,s = toss()
if f=='user':
    while True:
        p = play_user()
        user_count = user_count + check(p)
        print("User count =",user_count)
        if len(available)==0:
            break
        p = play_comp()
        comp_count=comp_count+check(p)
        print("Comp count =",comp_count)
        if len(available)==0:
            break
else:
    while True:
        p = play_comp()
        comp_count= comp_count+check(p)
        print("Comp count =",comp_count)
        if len(available)==0:
            break
        p = play_user()
        user_count = user_count + check(p)
        print("User count =",user_count)
        if len(available)==0:
            break
compare(user_count,comp_count)
    #left
    #right
