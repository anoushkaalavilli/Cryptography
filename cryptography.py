"""
cryptography.py
Author: Anoushka Alavilli
Credit: Mr. Dennison, Sarah Dunbar

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
message= input("Please enter a message. ")
key= input("Please enter a key. ")
listnumsofmessage= []
listnumsofkey= []

#ENCRYPTION:
for i in (message):
    listnumsofmessage.append(associations.find(i))
print (listnumsofmessage)

for i in (key):
    listnumsofkey.append(associations.find(i))
print (listnumsofkey)

keylength = len(key)
messagelength = len(message)
increasefactor = 1 + messagelength//keylength
key= increasefactor*key
print (message, key)
sumval= []
for i in (range(messagelength)):
    print (message[i], key[i])

for i in (key):
    listnumsofkey.append(associations.find(i))
print ((listnumsofmessage), (listnumsofkey))

numbersinmessage= (len(listnumsofmessage))
print (numbersinmessage)
encrypted= []
for i in range (numbersinmessage):
    placeinassociations= ((listnumsofmessage[i]) + (listnumsofkey[i]))
    if placeinassociations > 84:
        placeinassociations= ((placeinassociations) - 85)
    encrypted.append(associations[placeinassociations])
print (encrypted)

#DECRYPTION:
for i in (encrypted):
    print (associations.find(i))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
  
  
    #print (associations.find(message[i], key[i]))

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

#x= lambda ((len(listnumsofmessage))*x)%(len(listnumsofkey))=0)

#if (len(listnumsofmessage)) >= (len(listnumsofkey)):
 #   ((listnumsofkey)*x)