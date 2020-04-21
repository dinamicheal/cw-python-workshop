my_name =('Dina')
user_name = input('enter your name:') 
if user_name == my_name :
    print("Hello,Dina! The password is: @12")
else:
    print("Hello,",user_name,"! See you later.")





age =input('Are you a cigarette addict older than 75 years old: [yes , no]').lower()

chronic = input('enter if you have severe chronic disease [yes, no]?:').lower()
immune = input('enter if your immune system too weak[yes,no]?: ').lower()

if age == 'yes' :
   print(True)
else:
   print(False)


if chronic == 'yes':
    print(True)
else:
    print(False)

if  immune == 'yes' :
    print(True)
else:
    print(False)

if age or chronic or immune == True   :
   print("you're in risky group")
else:
   print("you're not in riskey group")