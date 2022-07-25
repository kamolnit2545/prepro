"""preproonsite"""

def main():
    """prepro"""
    money = int(input())
    waterprice = int(input())
    usemoney = money - waterprice
    snack1 = int(input())
    snack2 = int(input())
    snack3 = int(input())
    if usemoney %3 == 0:
        snack1 *= 10
    elif usemoney %3 == 1:
        snack1 *= 15
    elif usemoney %3 == 2:
        snack1 *= 20
    usemoney -= snack1
    print(usemoney)
    if usemoney %3 == 0:
        snack2 *= 12
    elif usemoney %3 == 1:
        snack2 *= 15
    elif usemoney %3 == 2:
        snack2 *= 18
    usemoney -= snack2
    print(usemoney)
    if usemoney %3 == 0:
        snack3 *= 5
    elif usemoney %3 == 1:
        snack3 *= 7
    elif usemoney %3 == 2:
        snack3 *= 9
    usemoney -= snack3
    print(usemoney)
    if usemoney < 0:
        print("Now you have" , money , "left.")
        print("You don't have enough money!")
    else:
        print("Now you have" , usemoney, "left.")
        print("Here's your order!")   
        print("Water:" , waterprice , "baht")
        print("Snack number 1:", snack1 , "baht")
        print("Snack number 2:", snack2 , "baht")
        print("Snack number 3:", snack3 , "baht")
main()
