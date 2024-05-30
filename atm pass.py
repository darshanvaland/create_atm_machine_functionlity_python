balance=4000
pin=123
pas=int(input("eneter your pass:"))
if pin==pas:
        print("Wel come to the Atm..")
        i=input("chose your operation: deposit,withrol,state:")
        if i=="deposit":
            deposit=int(input("enetr yopur deposit amt:"))
            o=balance+deposit
            a=input("would you want to show balance:")
            if a=="yes":
             print("total balance",o)
        elif i=="withrol":
            withrol=int(input("enter your withrol amt:"))
            if balance<=withrol:
                print("invalid")
            else:
                print("total bal",balance-withrol)
        elif i=="state":
            print("your balance is:",balance)
else:
    print("invalid pin")