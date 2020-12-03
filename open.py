import random
char = "abcçdefgğhiıjklmnoöprsştuüvyz0123456789.,:;/*-+?[]{}&%^'"
password = ""
hane = int(input("istediğiniz hane sayısı"))
i = 1
while i <= hane:
    sayi = random.randint(0,len(char)-1)
    password += char[sayi]
    i+=1
print("*********Şifre Oluşturuldu***********")
print(password)
print("*************************************")