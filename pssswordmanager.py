import string
import random

password={

}
# loading file


try:
    with open('password.txt','r') as file:
        for line in file:
            website,pwd=line.strip().split(':')
            password[website]=pwd

except Exception as err:
    print(f"You got an exception as {err}")


def generatepss():
    chars=string.ascii_letters+string.digits+"!@#$%&"
    passw="".join(random.choice(chars) for _ in range(8))

    return passw

while True:

    print("\n--------Person Password Manager--------\n")

    print("1. Save Password ")
    print("2. View Password ")
    print("3. Generate Password ")
    print("4. Exit")

    choice=int(input("Please enter your choice: "))

    if choice==1:
        site=input("Enter the website: ")
        passw=input("Enter the password: ")

        password[site]=passw

        with open('password.txt','a') as file:
            file.write(f"{site}:{passw} \n")

        print("Saved!")

    elif choice==2:
        if not passw:
            print("No data exist")

        else:
            for site,passw in password.items():
                print(site,":",passw)


    elif choice==3:
        print("Generaed Password: ",generatepss())

    elif choice==4:
        print("Ok bye..!")
        break

    else:
        print("Invalid Input")





