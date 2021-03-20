import math

print ("Ohm's law states that the current through a conductor between two points is directly proportional to the voltage across the twopoints.")
print("It is given by the mathematical equation V/I = R (where R is the constant)")

olaw= input("What term is given(V(Voltage), I(Current), R(Resistance))>> ")

if olaw== 'V' or olaw=='Voltage':
    V= int(input("What is the value of voltage>> "))
    p1 = input("Is any other term given>>")
    if p1=='Yes' or p1=='yes':
        p2= input("What is the term>> ")

        if p2=='Resistnce' or p2=='R':
            R= int(input("What is the value of R>> "))
            I = V/R
            print("The value of current is " ,I, " Amperes")
        
        if p2=='Current' or p2=='I':
            I= int(input("What is the value of I>> "))
            R = V/I
            print("The value of current is " ,R, "Ohms")

if olaw== 'R' or olaw=='resistance':
    R= int(input("What is the value of Resistance>> "))
    p1 = input("Is any other term given>>")
    if p1=='Yes' or p1=='yes':
        p2= input("What is the term>> ")

        if p2=='current' or p2=='I':
            I= int(input("What is the value of I>> "))
            V = I*R
            print("The value of current is " ,I, " Amperes")
        
        if p2=='Voltage' or p2=='V':
            V= int(input("What is the value of V>> "))
            I = V/R
            print("The value of current is " ,R, "Ohms")

if olaw== 'I' or olaw=='current':
    I= int(input("What is the value of current>> "))
    p1 = input("Is any other term given>>")
    if p1=='Yes' or p1=='yes':
        p2= input("What is the term>> ")

        if p2=='Resistance' or p2=='R':
            R= int(input("What is the value of R>> "))
            V = I*R
            print("The value of current is " ,V, " Amperes")
        
        if p2=='Voltage' or p2=='V':
            V= int(input("What is the value of V>> "))
            I = V/R
            print("The value of current is " ,I, "Ohms")
