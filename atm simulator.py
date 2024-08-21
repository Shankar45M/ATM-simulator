print("Enter 1 for checking account balance")
print("Enter 2 to withdraw money")
print("Enter 3 to deposit money")
print("Enter 4 to exit the system")
bal=500
while True:
    ch=int(input("Enter the choice"))
    if ch==1:
        print("Bank balance is",bal)
    elif ch==2:
        w_amt=int(input("Enter amount to be withdrawn"))
        print("Amount withdrawn successfully. Bank balance is",(bal-w_amt))
    elif ch==3:
        d_amt=int(input("Enter amount to be deposited"))
        print("Amount deposited successfully. Bank balance is",(bal+d_amt))
    elif ch==4:
        print("Thank you for using the ATM. Goodbye!")
        break

