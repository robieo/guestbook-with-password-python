import sys
import time
from datetime import date
import datetime


# Variablen

datei_handler_count_words = open('guestbook_log.txt')
inhalt = datei_handler_count_words.read()
trennwoerter = inhalt.split(' ')

leerzeichen = " "
doppelpunkt = ":"
verweis = ">>"

req_password = 1234

aktuelles_Datum = date.today()

now = datetime.datetime.today()
aktuelle_Zeit = now.strftime('%H:%M:%S')

#Start.

print()
print('Anzahl Wörter: '+str(len(trennwoerter))+' Wörter')
print()
print("================")
print("Guestbook")
print("================")
print()



input_name = input("Please enter your name! >>")

print()

input_password = int(input("Please validate your ID! (password) >>"))


# Validate Password.

if input_password == req_password:
    print()
    
    print("Welcome,",input_name," ")
    print()
  
    
    #Create sentece.
    
    input_user = input("Enter your opinion! >>")
    datei_handler = open('guestbook_log.txt',mode='a')
    
    ### text.write ###

    datei_handler.write('\n'+input_name + leerzeichen + '[' + str(aktuelles_Datum) + ']' + leerzeichen + '[' + str(aktuelle_Zeit) + ']' + leerzeichen + verweis + leerzeichen + input_user)
    
    ### text.write ###

    print()
    print("Thank you,",input_name,"!")
    

    print()
    print("The Guestbook will be closed...")
    time.sleep(1)
    exit(0)
    

else: print("Validation failed",input_name,":-(")
print("The Guestbook will be closed in 5 seconds ...")
time.sleep(5)
exit(0)




