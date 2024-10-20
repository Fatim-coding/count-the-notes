# Taking amount as input from user
Amount =int(input("please Enter Amount for withdraw :"))

# calculaating the number fo notes of different denominations
note1 = Amount//100
note2 = (Amount%100)//10
note3 =((Amount%100)%50)//10


print("notes of 100 dalasis", note1)
print("notes of 50 dalasis", note2)
print("notesof 10 dalasis",note3)