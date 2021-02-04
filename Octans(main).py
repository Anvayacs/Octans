# All imports
import pyttsx3
import math
import angsum

#Python Text-To-Speech EngineX` 
engine = pyttsx3.init()
VoiceRate = 190     
engine.setProperty('rate', VoiceRate,)

#Define speak function
def speak(audio): 
    engine.say(audio)
    engine.runAndWait()

#To find out which formula is to be solved(soon to be voice based)


if __name__ == '__main__':
  speak("Octans initialized")

  while True:
    query = input("Which formula do you want to solve>> ")
   
    if query == 'angle sum property':
        asp = input("Which angle do you need to assess>> ")
        if asp == 'a':
            angsum.angA()
        if asp == 'b':
            angsum.angB()
        if asp == 'c':
            angsum.angC()

    else:
        quit()
            





    

   
   

    



    
    


