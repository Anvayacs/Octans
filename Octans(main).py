# All imports
import pyttsx3
import math
import asumpy3
import wikipedia
import mpointpy3
from arithpro1 import ap_sum, ap_anyTerm, ap_firstTerm, ap_lastTerm 
from cirelarea import area, area_sector, theta_sector, circumference, circumference_sector, radius
import sys, os 
import json
from difflib import get_close_matches
import pyttsx3

    
#Python Text-To-Speech EngineX 
engine = pyttsx3.init()
VoiceRate = 190     
engine.setProperty('rate', VoiceRate,)

#Define speak function
def speak(audio): 
    engine.say(audio)
    engine.runAndWait()

def condition():
    print("The equation is a1x+b1y+c1=0 and a2x+b2x+c2=0")
    vala1= int(input("Enter the Value of 'a1' in a1x+b1y+c1=0>> "))
    vala2= int(input("Enter the Value of 'a2' in a2x+b2y+c2=0>> "))
    valb1= int(input("Enter the Value of 'b1' in a1x+b1y+c1=0>> "))
    valb2= int(input("Enter the Value of 'b2' in a2x+b2y+c2=0>> "))
    valc1= int(input("Enter the Value of 'c1' in a1x+b1y+c1=0>> "))
    valc2= int(input("Enter the Value of 'c2' in a2x+b2y+c2=0>> "))

    if vala1/vala2 == valb1/valb2 != valc1/valc2:
        print("The equations are inconsistent with no solution and represented by parallel lines")

    if vala1/vala2 == valb1/valb2 == valc1/valc2:
        print("The equations are consistent with infinitely many solutions and represented by coincident lines") 

    if vala1/vala2 != valb1/valb2:
        print("'The equations are consistent with a unique solution and represented by intersecting lines'")    


def mpo1nt():
    midf = input("What do you need to find out (midpoint, midpoint on x axis or midpoint on y axis)>> ") 
    if midf == 'midpoint':
        mpointpy3.midpoint()     
    if midf == 'midpoint on x axis' or 'midpoint on x':
        mpointpy3.midpointx()     
    if midf == 'midpoint on y axis' or 'midpoint on y':
        mpointpy3.midpointy()     
    else:
        quit()

def cirarea():
    cirar = input("What do you need to find out (area, radius, area of sector, theta of sector, circumference of sector)>> ") 
    if cirar == 'area':
        area()     
    if cirar == 'area of sector' or 'area sector':
        area_sector() 
    if cirar == 'radius':
        radius()
    if cirar == 'theta of sector':
        theta_sector()
    if cirar == 'circumference of sector':
        circumference_sector()
    if cirar == 'circumference':
        circumference()      
    else:
        quit()


if __name__ == '__main__':
  speak("Octans initialized")                           

  while True:     
    #To find out which formula is to be solved(soon to be voice based)  
    query = input("Which formula do you want to solve>> ")
   
    if query == 'angle sum property':
        asp = input("Which angle do you need to assess>> ")
        if asp == 'a':
            asumpy3.asumpy3.angA()
            continue
        if asp == 'b':
            asumpy3.asumpy3.angB()
            continue
        if asp == 'c':
            asumpy3.asumpy3.angC()
            continue
        else:
            quit()
            
     
    elif query == 'ap' or query=='arithmetic progression': 
        apv = input("What do you need to find out (first term.......)>> ") 

        if apv == 'first term':
            ap_firstTerm()
        if apv == 'sum of ap':
            ap_sum()
        if apv == 'last term' :
            ap_lastTerm()
        if apv == 'anyterm':
            ap_anyTerm()
        else:
            quit()
    
    elif query == 'midpoint formula' or query=='midpoint1':
        mpo1nt()  
    
    elif query== 'conditions' or query== 'conditions of linear equations':
        condition()
    
    elif query == 'area of circle':
        cirarea()
    
   
