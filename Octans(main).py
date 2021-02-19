# All imports
import pyttsx3
import math
import asumpy3
import wikipedia
import mpointpy3
from arithpro1 import ap_sum, ap_anyTerm, ap_firstTerm, ap_lastTerm 
import cirRelArea
import sys, os 
    
#Python Text-To-Speech EngineX 
engine = pyttsx3.init()
VoiceRate = 190     
engine.setProperty('rate', VoiceRate,)

#Define speak function
def speak(audio): 
    engine.say(audio)
    engine.runAndWait()

def firstterm():
    ap_firstTerm()


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

    if query == 'midpoint formula' or 'midpoint1': 
        midf = input("What do you need to find out (midpoint, midpoint on x axis or midpoint on y axis)>> ") 
        if midf == 'midpoint':
            mpointpy3.midpoint()     
        if midf == 'midpoint on x axis' or 'midpoint on x':
            mpointpy3.midpointx()     
        if midf == 'midpoint on y axis' or 'midpoint on y':
            mpointpy3.midpointy()     

        else:
            quit()
    
    if query == 'ap' or 'arithmetic progression': 
        apv = input("What do you need to find out (first term.......)>> ") 

        if apv == 'first term':
            firstterm()
        
        else:
            quit()

    

    
    
                





    

   
   

    



    
    

