import sys
import time

# Variablen

req_password = 1234

#Start.

print()
print("================")
print("Guestbook")
print("================")
print()

print("Loading...")
time.sleep(1)

input_name = input("Please enter your name! >>")
time.sleep(0.6)

print("Loading...")
time.sleep(1.2)

input_password = int(input("Please validate your ID! (password) >>"))

print("Loading...")
time.sleep(2.4)

# Validate Password.

if input_password == req_password:
    print()
    time.sleep(1.5)
    
    print("Welcome,",input_name," ")
    print()
    time.sleep(0.4)
    
    #Create sentece.
    
    input_user = input("Enter your opinion! >>")
    datei_handler = open('guestbook_log.txt',mode='a')
    datei_handler.write(input_user)
    print()
    print("Thank you,",input_name,"!")
    time.sleep(1)

    print("The Guestbook will be closed in 5 seconds ...")
    time.sleep(5)
    exit(0)

else: print("Validation failed",input_name,":-(")
print("The Guestbook will be closed in 5 seconds ...")
time.sleep(5)
exit(0)




