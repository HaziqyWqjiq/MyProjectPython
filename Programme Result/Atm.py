balance=4,301,839.50
print("    ATM    ")
print("""
1)        Balance
2)        Withdraw
3)        Deposit
4)        Quit


""")
Option=int(input("Enter Option: "))

if Option==1:
    print("Balance  RM ",balance)


if Option==2:
    print("Balance  RM  ",balance)
    Withdraw=float(input("Enter Withdraw amount £ "))
    if Withdraw>0:
        forewardbalance=(balance-Withdraw)
        print("Foreward Balance  £ ",forewardbalance)
    elif Withdraw>balance:
        print("No funs in account")
    else:
        print("None withdraw made")

if Option==3:
    print("Balance  RM ",balance)
    Deposit=float(input("Enter deposit amount RM "))
    if Deposit>0:
        forewardbalance=(balance+Deposit)
        print("Forewardbalance  £ ",forewardbalance)
    else:
        print("None deposit made")


if Option==4:
    exit()