# VARIABLE 
# sebuah feature untuk menyimpan value

# case style
# camelCase
# myFruit = "lychee"
# myFruit = "pineapple" #overwrite / reassign value
# print(myFruit)

# snake_case
# my_fruit = "kiwi"
# print(my_fruit)

# PascalCase
# MyFruit = "apple"
# print(MyFruit)

# CONSTANT
# variable yang nilainya tidak bisa diubah
# PI = 3.14
# print(PI)

# multiple assignment
# name, age, is_married = "John", 25, False
# print(name)
# print(age)
# print(is_married)

# swap variable
# a = 10
# b = 20
# a, b = b, a
# print(a)
# print(b)

# unpacking
# fruits = ["apple", "banana", "cherry"]
# fruit1, fruit2, fruit3 = fruits
# print(fruit1)
# print(fruit2)
# print(fruit3)

# global variable
# def myFunction():
#     global x
#     x = "fantastic"
#     print(fruit1, "is", x)

# myFunction()

# string + variable
# print('I love', fruit1, "!")
# print(fruit2 + " is delicious", fruit3 + " is sweet")
# print(f' I love {fruit1} !')

# int
# age = 25
# print(age)
# print(type(age))

# float
# height = 175.5
# print(type(height))

# soal 1
# tentukan hasil dari 5 + 2 :(1/2)
# print(5 + 2 / (1/2))
# print(type(5 + 2 / (1/2)))

# list --> mutable
# list_job = ["DS", "DA", "BI Analyst"]
# stud = ["John", 25, False, 175.5, list_job]
# hitung maju -> 0, 1, 2, 3, 4
# hitung mundur -> -5, -4, -3, -2, -1
# print(stud)
# print(type(stud))
# print(stud[4],[1])
# print(stud[4][1])
# print(stud[-3])

# tuple --> immutable
# tuple_job = ("DS", "DA", "BI Analyst")
# print(tuple_job)
# print(type(tuple_job))
# print(tuple_job[1])

# dictionary (key : value)
# stud = {
#     "name" : "Josi",
#     "age" : 25,
#     "status" : True
# }
# print(stud["status"])
# print(type(stud))

# dictionary + list
# stud = {
#     "name" : ["Josi", "Alfi"],
#     "age" : [25, 24],
#     "status" : [True, True]
# }
# print(stud["name"][1])
# print(type(stud))
# print(type(stud["age"]))
# print(type(stud["age"][1]))

# boolean
# bool1 = True
# bool2 = False
# print(type(bool1))

# range
# myRange = range(6) # nilai akhir di exclude 1
# print(type(myRange))
# print(list(myRange))
#cara penulisan kedua
# print(list(range(6)))
# print(list(range(-2,15)))

# set
# set1 = {4, 3, 2, 5, 1,}
# print(set1)
# print(type(set1))

# none
# x = None
# print(type(x))

#catatan bedanya immutable dan mutable
# tuple_job[1] = "Data Analyst"
# list_job[1] = "Data Analyst"
# print(list_job)
# list_job.append("Data Engineer") #menambahkan value --> append


# ARITHMATIC OPERATIONS

# x = 125000000
# y = 125e6
# print(x,y)
# print(x, type(x))
# print(y, type(y))

# penjumlahan
# x = 10
# y = 3  
# print(x + y)

# pengurangan
# print(x - y)

# perkalian
# print(x * y)

# pembagian
# print(x/y)

# modulus
# print(x % y)

# pangkat
# print(x**y)

# floor division
# print(x//y)

# assignment operator
# a = 5
# b = 3
# a+=b # a = a + b
# a%=b # a = a%b
# print(a)
# print(b)
# b+=a
# print(b)

# x = 4.7
# x2 = 4.1
# print(round(x))

# math module
# import math

# print(math.ceil(x2))

# python casting --> meruhbah data type
# string to float
# nik = "367401239933"
# print(float(nik))

# int to string
# postcode = 15311
# postcode = str(postcode)
# print(postcode)
# print(type(postcode))

# string format
# escape character
# print("I'm a \"student\"")

# \n -> new line
# print("I'm a \n\"student\"")

# \t -> tab
# print("I'm a \t\"student\"")

# string method

# text = "I'm a student"
# len() --> menghitung jumlah karakter
# print(len(text))
# split() --> memisahkan kata
# print(text.split())
# lower() --> mengubah huruf menjadi kecil
# print(text.lower())
# upper() --> mengubah huruf menjadi besar
# print(text.upper())
# replace() --> mengganti kata
# print(text.replace("student", "teacher"))
# title() --> mengubah huruf pertama menjadi besar
# print(text.title())

# string slicing
# x = "Data Science"
# 1 keluarkan sci
# print(x[5:8])
# 2 keluarkan science
# print(x[5:])
# 3 keluarkan ata
# print(x[1:4])
# 4 keluarkan ecne
# print(x[-4:][::-1])
# print(x[::-1][:4])
# print(x[-1:-5:-1])
# # 5 keluarkan sine
# print(x[5::2])
# print(x[5:12:2])
# print(x[5]+x[7]+x[9]+x[11])

# user input
# vol balik (p x l x t)
# p = 3
# l = 4
# t = 5

# print(f"Volume balok dengan panjang {p}, lebar {l}, dan tinggi {t} adalah {p*l*t}")

#program yang bisa diinput oleh user
# p = int(input("Masukkan panjang: "))
# l = int(input("Masukkan lebar: "))
# t = int(input("Masukkan tinggi: "))
# print(f"Volume balok dengan panjang {p}, lebar {l}, dan tinggi {t} adalah {p*l*t}")

# soal user input
# # program untuk menghitung luas lingkaran
# import math
# d = int(input("Masukkan diameter: "))
# r = d/2
# luas = math.pi*r**2
# print(f"Luas lingkaran dengan diameter {d} adalah {luas}")


