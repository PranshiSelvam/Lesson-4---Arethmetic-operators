math = int(input("Enter the marks scored in Math : "))
english = int(input("Enter the marks scored in English : "))
second_language = int(input("Enter the marks scored in Second Language : "))
chemistry = int(input("Enter the marks scored in Chemistry : "))
biology = int(input("Enter the marks scored in Biology : "))
physics = int(input("Enter the marks scored in Physics : "))
geography = int(input("Enter the marks scored in Geography : "))
history = int(input("Enter the marks scored in History : "))

sum = math+english+second_language+chemistry+biology+physics+geography+history
print("The total marks achieved in all the subject is ", sum)

percentage = (sum/800)*100
print("You have secured ", percentage)