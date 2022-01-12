# kms = float(input("how many kms do you want to convert?!"))

# print(f"ok you said {kms} KMs")
# mail = kms /1.60934
# mail = round(mail,2)
# print(f"{ kms }is{mail}")

nameuser = (input("What is your name:"))
print(f"Welcome {nameuser}")
i = 8
while i>7:
    requstuser = str(input(' for  kilometers to miles:"kms"  for miles to kilometr:"mail" for quiet:"q":>'))
    if requstuser == "kms":
        kms = float(input("how many KMs you want to convert?!"))
        print(f"ok you said {kms} KMs")
        mail = kms /1.60934
        mail = round(mail,2)
        print(f"{ kms } KMis{mail}miels")
    if requstuser == "mail":
        mail = float(input("how many Miles you want to convert?!"))
        print(f"ok you said {mail} miles")
        kms = mail *1.60934
        kms = round(kms,2)
        print(f"{ mail } MIleS  is  {kms}KM")
    elif requstuser == "Q" :
        print("you quiet")
        break
    else:
            print("Invalid input  Try again")
        
    