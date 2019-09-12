import string                 
dict={}
data=""
ff=open('NewFile.txt','w')
for i in range(len(string.ascii_letters)):                #string.ascii_letters have all the 26 alphabets in small and capital
    dict[string.ascii_letters[i]]=string.ascii_letters[i-1]
   # print(dict)
with open('OldFile.txt','r') as f:                        #opening file in read mode
    while True:
        c=f.read(1)
        if not c:
            print("End of File")
            break
        if c in dict:
            data=dict[c]
        else:
            data=c
        ff.write(data)                                        #encrypting the file
ff.close()
with open('NewFile.txt','r') as ff:                           #opening the encrypted file
    while True:
        c=ff.read(1)
        if not c:
            print('Eof')
            break
        else:
            print(c)
        
    
    
''' Input file : Hello How are you I am fine thank you   
    Output File: Gdkkn Gnv Zqd xnt? H Zl ehmd sgZmj xnt! 
'''
