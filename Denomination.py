amount = int(input("Enter the amount you would like to withdraw: "))
note1 = amount // 500
note2 = (amount%500) // 100
note3 = ((amount%500)%100) // 50
note4 = (((amount%500)%100)%50) // 10

print("The number of notes of 500 are " , note1)
print("The number of notes of 100 are " , note2)
print("The number of notes of 50 are " , note3)
print("The number of notes of 10 are " , note4)
