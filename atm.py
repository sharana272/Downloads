balance=10000
pin =1234

print("wlecome to atm")
print("insert card here")
if("card inserted"):
      print("yes")
else:
     print("no")

print(" enter pin")
pin_input = int(input("enter pin"))
if("pin is correc t"):
      print("pin is correct")
else:
      print("no")

print("select language")
pin_input==int(input("select language"))
print("1.english")
print("2.kannada")
print("3.hindi")
if("1 "):
    print("selected 1.english")
elif("2"):
     print("selected 2.kannada")
elif("3"):
        print("selected 3.hindi")
else:
   print("in valid")

print("select option")
pin_input==int(input("select option"))
print("1.withdraw")
print("2.deposit")
print("3.balance")
if("1 "):
    print("selected 1.deposit")
elif("2"):
     print("slected 2.withdraw")
elif("3"):
     print("selected 3.balance")
else:
     print("in valid")
print("enter amount to withdraw")
withdraw =int(input("withdraw"))

print("withdraw successful")
print("do you want check balance")
if("check balance"):
 print("yes")
else:
 print("no")
 
print("your balance is", withdraw-balance)
print("please collect your card")
print("thank you for using atm")




