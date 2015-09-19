#-*- coding: utf8 -*-
import crypt

def testPass(cryptPass):
    salt=cryptPass[0:2]
    dicFile=open('dictionary.txt','r')
    a=1
    for word in dicFile.readlines():
        word = word.strip('\n')
        cryptWord = crypt.crypt(word,salt)
        a += 1
        if (cryptWord==cryptPass):
            print "[+] Password is : "+word+"\n"
            return
    print "[-] Password not Found."
    return

def main():
    passFile = open('password.txt','r')
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip(' ')
            print "[*] Cracking Password For: "+user
            testPass(cryptPass)
    
if __name__=="__main__":
    main()

#1.strip함수
#2.split함수
#3.readLines함수
#4.리스트 슬라이싱과 string타잎
#3.hash함수의 개념과 salt
#4.
