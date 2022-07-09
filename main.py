from os import system as sys
from time import sleep as s
import msvcrt as ms


def clear():
    sys("cls")
    print("---- BODY MASS INDEX ----\n")


def bmistat(bmi):
    list1 = [0, 18.4, 24.9, 34.9, 44.9]
    list2 = ["Underweight", "Normal", "Overweight", "Obese", "Extremly obese"]
    for i in range(5):
        if i != 4:
            if list1[i] < bmi <= list1[i + 1]:
                return list2[i], \
                       f"If you lose {round(bmi - list1[i])} kilos you will be {list2[i - 1]}", \
                       f"If you gain {round(list1[i + 2] - bmi)} kilos you will be {list2[i + 1]}"
        else:
            return "Very extremely obese", \
                   f"If you lose {round(bmi - list1[i])} kilos you will be", "exit"


clear()
weight = ""
while type(weight) != float:
    weight = input("Enter weight (kg->76) >> ")
    try:
        weight = float(weight)
    except:
        if "," in weight:
            print("Plase use '.' and try again.")
        else:
            print("Please enter integer.")
        s(2)
    clear()

s(1)
clear()
height = ""
while type(height) != float:
    height = input("Enter height (m->1.76) >> ")
    try:
        height = float(height)
    except:
        if "," in height:
            print("Plase use '.' and try again.")
        else:
            print("Please enter integer.")
        s(2)
    clear()

s(1)
print(f"Body mass index (BMI): {round(weight / (height ** 2))}")
s(1)
a, b, c = bmistat(weight / (height ** 2))
print(a)
s(1)
print(b)
s(1)
if c != "exit":
    print(c)
    s(1)
print("\nPress any key to exit...")

while True:
    if ms.kbhit():
        exit()
        
