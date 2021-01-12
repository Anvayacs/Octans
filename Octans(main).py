# All imports
import pyttsx3
import math

#Python Text-To-Speech Engine
engine = pyttsx3.init()
VoiceRate = 190
engine.setProperty('rate', VoiceRate,)

#Define speak function
def speak(audio): 
    engine.say(audio)
    engine.runAndWait()

#To find out which formula is to be solved(soon to be voice based)
query = input("Which formula do you want to solve>> ")
    
if query == 'angle sum property': # Angle Sum Property Basic theorem
    speak("Please input the angle you need to assess") #speech introduction 
    asp = input("Which angle do you need to assess>> ") 

    # Possibility of Angle A as the missing angle
    if asp == 'a':
        angb = int(input(("Please tell me the value of Angle B>>")))
        angc = int(input(("Please tell me the value of Angle C>>")))
        anga = 180 - (angb + angc)

    #To figure out if the provided angles form a valid triangle(all 3 possibilities have same provision)  
        if (anga + angb + angc) == 180 and anga>0 : 
            print("This pair of angles form a valid triangle")
            print("Steps")
            print("Angle A = 180 - (Angle B + Angle C)")
            print("Angle A = 180 - " "(" ,angb, " + ",angc, ")") 
            print ("Angle A = 180 -" ,(angb+angc), )
            print("Angle A =" ,(180- (angb+angc)))
            print("The value of Angle a is>> ", anga, " Degrees")
        continue
            
        elif (anga + angb + angc) != 180 or anga<=0:   
            print ("This triangle is not valid")
        continue

    # Possibility of Angle B as the missing angle 
    elif asp == 'b':  
        anga = int(input(("Please tell me the value of Angle A>>")))
        angc = int(input(("Please tell me the value of Angle C>>")))
        angb = 180 - (anga + angc)

        if (anga + angb + angc) == 180 and angb>0 :
            print("This pair of angles form a valid triangle")
            print("Steps")
            print("Angle B = 180 - (Angle A + Angle C)")
            print("Angle B = 180 - " "(" ,anga, " + ",angc, ")") 
            print ("Angle B = 180 -" ,(anga+angc), )
            print("Angle B =" ,(180- (anga+angc)))
            print("The value of Angle b is>> ", angb, " Degrees")
        continue
        
        elif (anga + angb + angc) != 180 or angb<=0:   
            print ("This triangle is not valid") 
        continue

    # Possibility of Angle C as the missing angle  
    elif asp == 'c':  
        anga = int(input(("Please tell me the value of Angle A>> ")))
        angb = int(input(("Please tell me the value of Angle B>> ")))
        angc = 180 - (anga + angb)

        if (anga + angb + angc) == 180 and angc>0 :
            print("This pair of angles form a valid triangle")
            print("Steps")
            print("Angle C = 180 - (Angle A + Angle B)")
            print("Angle C = 180 - " "(" ,anga, " + ",angb, ")") 
            print ("Angle C = 180 -" ,(anga+angb), )
            print("Angle C =" ,(180- (anga+angb)))
            print("The value of Angle c is>> ", angc, " Degrees")
        continue
            
        elif (anga + angb + angc) != 180 or angb<=0:   
            print ("This triangle is not valid") 
        continue  

if query == 'surface area' or 'tsa' or 'csa' or 'volume': # Surface Area and volume  
    sa = input(" Surface Area of which Shape do you need to find out>> ")

    if sa == 'cube':
        tysa= input("Which formula would u like to use (tsa/csa/volume) or the value of the edge>> ")

        if tysa == 'tsa' or 'TSA':
            aside= int((input("What is the value of the edge>> ")))
            tsacub= (6*aside*aside)
            print ("The tsa of the given cube is" ,tsacub)

        elif tysa == 'csa' or 'CSA':
            aside= int((input("What is the value of the edge>> ")))
            csacub= (4*aside*aside)
            print ("The csa of the given cube is" ,csacub)

        if tysa == 'volume' or 'Volume':
            aside= int((input("What is the value of the edge>> ")))
            volcube= (aside*aside*aside)
            print ("The Volume of the given cube would be," volcube)

        if tysa == 'edge' or 'Edge': #TO Calculate edge by the given 3 possibilities
            ques= input("What is the given value (tsa(press 1) or csa(press 2) or volume (press 3))>> ")
            if ques == '1':#TSA Possibility
                tsacub= int((input("What is the TSA>> ")))
                aside = math.sqrt(tsacub)/6
                print ("The edge in this instance is " ,tsacub)

            if ques == '2':#CSA Possibility
                csacub= int((input("What is the CSA>> ")))
                aside = math.sqrt(csacub)/4
                print ("The edge in this instance is " ,csacub)

            if ques == '3':#Volume Possibility
                volcube= int((input("What is the Volume>> ")))
                aside = volcubea**(1./3.)
                print ("The edge in this instance is " ,tsacub)
    
    elif sa == 'cuboid':
        tysa1= input("Which formula would u like to use (tsa/csa/volume)>> ")
        if tysa1 == 'tsa':
            lcubo=int((input("What is the value of the Length>> ")))
            bcubo=int((input("What is the value of the Breadth>> ")))
            hcubo=int((input("What is the value of the Height>> ")))
            tsacubo = 2*((lcubo*bcubo)+(bcubo*hcubo)+(lcubo*bcubo))
            print ("The TSA of the given cube is" ,tsacubo)

        elif tysa1 == 'csa':
            lcubo=int((input("What is the value of the Length>> ")))
            bcubo=int((input("What is the value of the Breadth>> ")))
            hcubo=int((input("What is the value of the Height>> ")))
            csacubo = (2*hcubo)*(lcubo+bcubo)
            print ("The CSA of the given cube is" ,csacubo)

        elif tysa1 == 'volume':
            lcubo=int((input("What is the value of the Length>> ")))
            bcubo=int((input("What is the value of the Breadth>> ")))
            hcubo=int((input("What is the value of the Height>> ")))
            volcubo = (lcubo*hcubo*bcubo)
            print ("The Volume of the given cube is" ,volcubo)

        elif tysa == 'edge' or 'Edge': #TO Calculate edge by the given 3 possibilities
            ques= input("What is the given value (tsa(press 1) or csa(press 2) or volume (press 3))>> ")
            if ques == '1':#TSA Possibility
                tsacub= int((input("What is the TSA>> ")))
                aside = math.sqrt(tsacub)/6
                print ("The edge in this instance is " ,tsacub)

            if ques == '2':#CSA Possibility
                csacub= int((input("What is the CSA>> ")))
                aside = math.sqrt(csacub)/4
                print ("The edge in this instance is " ,csacub)

            if ques == '3':#Volume Possibility
                volcube= int((input("What is the Volume>> ")))
                aside = volcubea**(1./3.)
                print ("The edge in this instance is " ,tsacub)
        

    elif sa == 'cylinder':
        tysa2= input("Which formula would u like to use (tsa/csa/volume)>> ")
        if tysa2 == 'tsa':
            rcyl = int(input("What is the value of the radius>> "))
            hcyl = int(input("What is the value of the height>> "))

if query == 'arithmetic progression' or 'ap': # Arithmetic Progression 
    ap = input("What do you need to find out (sum, first term, last term or any term)>> ")  
    
    if ap == 'sum': # Possibility 1- Sum of 'N' terms
        nterms = int(input("Sum of how many terms is required>> "))
        aterm = int(input("First Term>> "))
        dterm= int(input("Difference between the terms>> "))
        sumot = ((nterms/2)) * (2*aterm + (nterms-1) * dterm)
        print("Steps to solve")
        print("Sum of" ,nterms, " is = N/2 x (2a + (N-1) x d)")
        print("Sum of" ,nterms, " is = " ,nterms,"/2" " x " "(2 x" ,aterm, "+" "(" ,nterms, "-1)" "x" ,dterm,)
        print ("The sum of " ,nterms, " term is " ,sumot,)



    
    


