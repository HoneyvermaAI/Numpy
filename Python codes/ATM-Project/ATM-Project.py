name = "Honey"

PIN = "8394"
avl_bal = 1200000

i = 0
while i < 3:
    acountt_name = input("\nenter your name:")
    pin = input("\nenter your password:")
    if (pin == PIN and name == acountt_name):
        print("\nlogin sucessfull\n")
        print("\n\nhello", name)
        while True:
            print("********* ATM MENU ********* ")
            print("\npress \"d\" for deposit money")
            print("\npress \"w\" for withdrawl")
            print("\npress \"np\" for change pin")
            print("\npress \"new\" for change name")
            print("\npress \"exit\" for exit ")
            user = input("\n\n enter your use of ATM:")
            if user == "d":
                d_amt = int(input("\nenter the amount you want to deposit:"))
                print("\ntransaction successful")
                avl_bal = avl_bal + d_amt
                print("\navailable balance :", avl_bal)
                break


            elif user == "w":
                w_amt = int(input("\nenter the amount you want to withdrawl :"))
                if w_amt <= avl_bal:
                    print("\ntransaction sucessfull")
                    avl_bal = avl_bal - w_amt
                    print("\navailable balance :", avl_bal)
                else:
                    print("\ninsufficient balance")
                break

            elif user == "np":
                new = input("\nenter new password:")
                PIN = new
                break

            elif user == "new":
                new_name = input("\nenter new name:")
                name = new_name
                break

            elif user == "exit":
                print("thankyou")
                exit()
            else:
                print("\nwrong choice,select again")



    else:
        print("\ninvalid credentials")
        i += 1
else:
    print("\ntry after 24 hrs")