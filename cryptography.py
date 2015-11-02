"""
cryptography.py
Author: Anoushka Alavilli
Credit: <list sources used, if any>

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
message= input("Please enter a message. ")
key= input("Please enter a key. ")
listnumsofmessage= []
listnumsofkey= []

for i in (message):
    listnumsofmessage.append(associations.find(i))
print (listnumsofmessage)

for i in (key):
    listnumsofkey.append(associations.find(i))
print (listnumsofkey)

#print (((listnumsofmessage).count(i))%((listnumsofkey).count(i)))
    #for x in (listnumsofmessage):
        #for y in (listnumsofkey):
            #print (x,y)
        #break

#lenkey= (len(listnumsofkey))
#rangekey= (range(lenkey))
#print (rangekey)
#iinrangekey= (i in rangekey)
#for x in range(len(listnumsofmessage)):
   #print (x, iinrangekey)
x= None
if (len(listnumsofmessage)) >= (len(listnumsofkey)):
    number= ((len(listnumsofmessage))*x)%(len(listnumsofkey))=0)
    print (number)