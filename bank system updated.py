print("Welcome to State Bank of India,Main Branch , Bilaspur,CG")
a=int(input("Enter Account Number:"))
if a==123456789012:
     print("Name: Rajan Kumar")
     print("Balance Amount:68924")
if a==787936238154:
     print("Name: Prateek Dutta")
     print("Balance Amount:786975")
if a==989331359072:
     print("Name: Pankaj Dutta")
     print("Balance Amount:365300")
if a==896282167328:
     print("Name: Papiya Dutta")
     print("Balance Amount:560492")
if a==121106578943:
     print("Name: Raja Dutta")
     print("Balance Amount:125865")
print("1. Withdraw amount")
print("2. Deposit amount")
print("3. Quit as I want to know the status of account")
x=int(input("Enter the coice:"))
if x==1:
     b=int(input("Please enter the balance amount:"))
     y=int(input("Enter Amount you want to withdraw:"))
     print("Your avialable balance amount:",b-y)
     p=int(input("would you like to continue(1-yes/2-no):"))
     if p==1:
          print("your account number:",a)
          print("Balance amount:",b-y)
          print("1. Withdraw amount")
          print("2. Deposit amount")
          r=int(input("Enter the coice:"))
          if r==1:
               t=int(input("Enter Amount you want to withdraw:"))
               print("Your avialable balance amount:",b-y-t)
          if r==2:
               s=int(input("Enter amount you want to deposit:"))
               print("Your avialable balance amount:",b-y+s)
     else:
          print("Thank You , Please visit again , Have a Nice Day")
if x==2:
     c=int(input("Please enter the balance amount:"))
     z=int(input("Enter Amount you want to Deposit:"))
     print("Your avialable balance amount:",c+z)
     e=int(input("would you like to continue(1-yes/2-no):"))
     if e==1:
          print("your account number:",a)
          print("Balance amount:",c+z)
          print("1. Withdraw amount")
          print("2. Deposit amount")
          w=int(input("Enter the coice:"))
          if w==1:
               d=int(input("Enter Amount you want to withdraw:"))
               print("Your avialable balance amount:",c+z-d)
          if w==2:
               f=int(input("Enter amount you want to deposit:"))
               print("Your avialable balance amount:",c+z+f)
     else:
          print("Thank You , Please visit again , Have a Nice Day")
if x==3:
     print("Thank You,Please visit again , Have a Nice Day")
