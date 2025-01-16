user_name = input("Enter your user name: ")
money_bank = ['SHADOW AGENCY MONEY ']
code = input('Enter your code')


if user_name.startswith('Banker Danny'):# and code.isnumeric():
    print("VALID USER IDENTITY")
    if code.isnumeric() and code.startswith(('419 001')):
        print("VALID CODE")
        print("ENTERED\n",money_bank)
    else:
         print("WRONG CODE \n. (code) is invalid")

else:
    print(f"ACCESS DENIED \n. (user_name) is incorrect")