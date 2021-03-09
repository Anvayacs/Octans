# All imports
import pyttsx3
import math
def lcm(x, y): 
    if x > y:
       z = x
   else:
       z = y

   while(True):
       if((z % x == 0) and (z % y == 0)):
           lcm = z
           break
       z += 1

   return lcm

#Python Text-To-Speech Engine
engine = pyttsx3.init()
VoiceRate = 190
engine.setProperty('rate', VoiceRate,)

#Define speak function
def speak(audio): 
    engine.say(audio)
    engine.runAndWait()

#To find out which formula is to be solved(soon to be voice based)
query = input("Which chapter or formula do you want to solve>> ")
    
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
            print(f"The value of Angle a is>> {-anga} Degrees")
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

elif query == 'surface area' or 'tsa' or 'csa' or 'volume': # Surface Area and volume  
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
        qtype = input("Which formula would u like to use (tsa/csa/volume)>> ")
        if qtype == 'tsa':
            r = float(input("What is the value of the radius>> "))
            h = float(input("What is the value of the height>> "))
            pi = input('what is the value of pi>> ')
            if pi == '22/7':
                tsa = 2*(22/7)*r*(r+h)
                print(f"The total surface area is {tsa}")
            elif pi == '3.14':
                tsa = 2*(3.14)*r*(r+h)
                print(f"The total surface area is {tsa}")
            else:
                print("Please enter a valid value")

        if qtype == 'csa':

            r = float(input("What is the value of the radius>> "))
            h = float(input("What is the value of the height>> "))
            pi = input('what is the value of pi>> ')
            if pi == '22/7':
                csa = 2*(22/7)*r*(h)
                print(f"The total surface area is {csa}")
            elif pi == '3.14':
                csa = 2*(3.14)*r*(h)
                print(f"The total surface area is {csa}")
            else:
                print("Please enter a valid value")
        
        if qtype == 'volume':
            r = float(input("What is the value of the radius>> "))
            h = float(input("What is the value of the height>> "))
            pi = input('what is the value of pi>> ')
            if pi == '22/7':
                volume = (22/7)*(r*r)*h
                print(f"The total surface area is {volume}")
            elif pi == '3.14':
                volume = (3.14)*(r*r)*h
                print(f"The total surface area is {volume}")
            else:
                print("Please enter a valid value")
  
    elif sa == 'cone':
        qtype = input("Which formula would u like to use (tsa/csa/volume)>> ")
        if qtype == 'tsa':
            qtype2 = input('Is slant height given>>')
            if qtype2 == 'no':
                r = float(input("What is the value of the radius>> "))
                h = float(input("What is the value of the height>> "))
                l = ((h**2)+(r**2))**0.5
                pi = input('what is the value of pi>> ')
                if pi == '22/7':
                    tsa = (22/7)*r*(r+l)
                    print(f"The total surface area is {tsa}")
                elif pi == '3.14':
                    tsa = (3.14)*r*(r+l)
                    print(f"The total surface area is {tsa}")
                else:
                    print("Please enter a valid value")

            if qtype2 == 'yes':
                r = float(input("What is the value of the radius>> "))
                l = float(input('What is the slant height>> '))
                pi = input('what is the value of pi>> ')
                if pi == '22/7':
                    tsa = (22/7)*r*(r+l)
                    print(f"The total surface area is {tsa}")
                elif pi == '3.14':
                    tsa = (3.14)*r*(r+l)
                    print(f"The total surface area is {tsa}")
                else:
                    print("Please enter a valid value")
        
        if qtype == 'csa':

            qtype2 = input('Is slant height given>>')
            if qtype2 == 'no':
                r = float(input("What is the value of the radius>> "))
                h = float(input("What is the value of the height>> "))
                l = ((h**2)+(r**2))**0.5
                print(l)
                pi = input('what is the value of pi>> ')
                if pi == '22/7':
                    csa = (22/7)*r*l
                    print(f"The lateral surface area is {csa}")
                elif pi == '3.14':
                    csa = (3.14)*r*l
                    print(f"The lateral surface area is {csa}")
                else:
                    print("Please enter a valid value")

            if qtype2 == 'yes':
                r = float(input("What is the value of the radius>> "))
                l = float(input('What is the slant height'))
                pi = input('what is the value of pi>> ')
                if pi == '22/7':
                    csa = (22/7)*r*l
                    print(f"The curved surface area is {csa}")
                elif pi == '3.14':
                    csa = (3.14)*r*l
                    print(f"The curved surface area is {csa}")
                else:
                    print("Please enter a valid value")
        
        if qtype == 'volume':
            r = float(input("What is the value of the radius>> "))
            h = float(input("What is the value of the height>> "))
            pi = input('what is the value of pi>> ')
            if pi == '22/7':
                volume = (1/3)*(22/7)*(r*r)*h
                print(f"The volume surface area is {volume}")
            elif pi == '3.14':
                volume = (1/3)*(3.14)*(r*r)*h
                print(f"The volume surface area is {volume}")
            else:
                print("Please enter a valid value")

    elif sa ==  'sphere':
        qtype = input("Which formula would u like to use (surface area/volume)>> ")
        if qtype == 'surface area':
            r = float(input('What is the radius>> '))
            pi = input('what is the value of pi>> ')
            if pi == '22/7':
                tsa = 4*(22/7)*(r**2)
                print(f"The total surface area is {tsa}")
            elif pi == '3.14':
                tsa = (3.14)*4*(r**2)
                print(f"The total surface area is {tsa}")
            else:
                print("Please enter a valid value")
            
        if qtype == 'volume':
            r = float(input('What is the radius>> '))
            pi = input('what is the value of pi>> ')
            if pi == '22/7':
                volume = (4/3)*(22/7)*(r**3)
                print(f"The total surface area is {volume}")
            elif pi == '3.14':
                volume = (4/3)*(3.14)*(r**3)
                print(f"The total surface area is {volume}")
            else:
                print("Please enter a valid value")

    elif sa == 'hemisphere':
        qtype = input("Which formula would u like to use (tsa/csa/volume)>> ")
        if qtype == 'tsa':
            r = float(input('What is the radius>> '))
            pi = input('what is the value of pi>> ')
            if pi == '22/7':
                tsa = 3*(22/7)*(r**2)
                print(f"The total surface area is {tsa}")
            elif pi == '3.14':
                tsa = (3.14)*3*(r**2)
                print(f"The total surface area is {tsa}")
            else:
                print("Please enter a valid value")

        if qtype == 'csa':
            r = float(input('What is the radius>> '))
            pi = input('what is the value of pi>> ')
            if pi == '22/7':
                csa = 2*(22/7)*(r**2)
                print(f"The total surface area is {csa}")
            elif pi == '3.14':
                csa = (3.14)*2*(r**2)
                print(f"The total surface area is {csa}")
            else:
                print("Please enter a valid value")
            
        if qtype == 'volume':
            r = float(input('What is the radius>> '))
            pi = input('what is the value of pi>> ')
            if pi == '22/7':
                volume = (2/3)*(22/7)*(r**3)
                print(f"The total surface area is {volume}")
            elif pi == '3.14':
                volume = (2/3)*(3.14)*(r**3)
                print(f"The total surface area is {volume}")
            else:
                print("Please enter a valid value")

elif query == 'arithmetic progression' or 'ap' or 'AP': # Arithmetic Progression 
    ap = input("What do you need to find out (sum, first term, last term, or any term)>> ")

    if ap == 'sum': 
        qtype = input("Is the first term of the AP given?>>")
        if qtype == 'yes':  # Possibility 1- Sum of 'N' terms when d is given
            nterms = int(input("Sum of how many terms is required>> "))
            aterm = int(input("First Term>> "))
            dterm= int(input("Difference between the terms>> "))
            sumot = ((nterms/2)) * (2*aterm + (nterms-1) * dterm)
            print("Steps to solve")
            print("Sum of" ,nterms, " is = N/2 x (2a + (N-1) x d)")
            print("Sum of" ,nterms, "terms is = " ,nterms,"/2" " x " "(2 x" ,aterm, "+" "(" ,nterms, "-1)" "x" ,dterm,)
            print ("The sum of " ,nterms, " term is " ,sumot,)

        elif qtype == 'no':  # Possibility 2 - Sum of 'N' terms when d is not given
            nterms = int(input("Sum of how many terms is required>> "))
            aterm = int(input("First Term>> "))
            lterm= int(input("last term>> "))
            sumot = ((nterms/2)) * (aterm+lterm) 
            print ("The sum of " ,nterms, " term is " ,sumot,)    
    
    elif ap == 'first term': #Possibility 1 - first term of an AP
        gterm = int(input("What is the given term>>"))
        numterm = int(input("which number of term is given ? >>"))
        dterm = int (input("What is the difference between the terms>>"))
        fterm = gterm - ((numterm-1)*dterm)
        print('Steps to solve')
        print("firsrt term = give  term - (number of giver term - 1)*d")
        print( 'The first term is' ,fterm, )    

    elif ap == "last term": 
        qtype = input("is the first term given>>")
        if qtype ==  "yes": #Possibilty 1 - last term of ap when a and d is given
            fterm = int(input('what is the first term of the AP>>'))
            dterm = int(input("what is the difference between terms>>"))
            nterms = int(input("what is the number of terms in the ap>>")) 
            lterm = fterm + (nterms-1)*dterm
            print(f"The last term is {lterm}")
            
        elif qtype ==  "no": #Possibilty 2 - last term of ap when any term and d is given
            gterm = int(input('what is the given term of the AP>>'))
            numterm = int(input("what is the number of given term>>"))
            dterm = int(input("what is the difference between terms>>"))
            nterms = int(input("what is the number of terms in the ap>>")) 
            fterm = gterm - ((numterm-1)*dterm)      
            lterm = fterm + (numterm-1)*dterm
            print(f"The last term is {lterm}")

    elif ap == "any term": 
        qtype = input("Is the first term given?>>")
        if qtype=="yes": 
            numterm = int(input("Which term is required>> "))
            aterm = int(input("First Term>> "))
            dterm= int(input("Difference between the terms>> "))  
            rterm = aterm + (numterms-1)*dterm
            print(f'The required term is {rterm}')         

        elif qtype == "no":
            numterm = int(input("Which term is required>> "))
            lterm = int(input("last Term>> "))
            dterm= int(input("Difference between the terms>> "))  
            rterm = lterm - (numterm-1)*dterm
            print(f'The required term is {rterm}')        
        
elif query == 'area realted to circle' or 'circle related area':
    carea = input("What do ypu want to find out(area of a circle, circumference, radius, area of a sector,\n circumference of a sector, angle of a sector>>)")

    if carea == "area of a circle":
        qtype = input("Is the circumference given>>")

        if qtype == "yes":
            circum= float(input("what is the circumference>>"))
            pi = (input("What should pi be taken as>>"))

            if pi == '22/7':
                r = circum*(7/22)*(1/2)
                area = (22/7)*(r**2) 
                print(f"The area is {area}")

            elif pi == "3.14":
                r = circum*(1/3.14)*(1/2)
                area = (3.14)*(r**2)
                print(f"The area is {area}")
            else:
                print("Please enter a valid value of pi")         
        
        elif qtype == 'no':
            r = float(input("What is the radius>>"))
            pi = (input("What should pi be taken as>>"))
            if pi == '22/7':
                area = (22/7)*(r*r)
                print(f"The area is {area}")

            elif pi == "3.14":
                    area = (3.14)*(r**2)
                    print(f"The area is {area}")
            else:
                print("enter a valid value of pi")
        
    elif carea == "circumference":
        qtype= input("Is the area given>> ")
        
        if qtype == "yes":
            area = float(input("What is the area>>")) 
            pi = input("What is the value of pi>>")

            if pi == '22/7':
                r = (area *(7/22))**(0.5)
                circum = 2*(22/7)*(r)
                print(f"The circumference is {circum}") 
            elif pi == '3.14':
                r = (area*(1/3.14))**(0.5)
                circum = (2*(3.14))*(r)
                print(f"The circumference is {circum}") 
            else:
                print("Please enter a valid value of pi")                    
        if qtype == "no":
            r = float(input("What is the radius>>")) 
            pi = input("What is the value of pi>>")

            if pi == '22/7':
                circum = 2*(22/7)*(r)
                print(f"The circumference is {circum}") 
            elif pi == '3.14':
                circum = 2*(3.14)*(r)
                print(f"The circumference is {circum}") 
            else:
                print("Please enter a valid value of pi")

    elif carea == "radius":
        qtype = input("Is the area given>> ")
        if qtype == "yes":
            area = float(input ("What is the area?"))
            pi = input("What is the value of pi>>")

            if pi == '22/7':
                r = (area *(7/22))**(0.5)
                print(f"The value of r is {r}")
            elif pi == '3.14':
                r = (area*(1/3.14))**(0.5)
                print(f"The value of r is {r}")
            else:
                print("Please enter a valid value of pi")  

        if qtype == "no":
            circum = float(input ("What is the circumference?"))
            pi = input("What is the value of pi>>")

            if pi == '22/7':
                r = (circum/2) * (7/22) 
                print(f"The value of r is {r}")
            elif pi == '3.14':
                r = r = (circum/2) * (1/3.14)
                print(f"The value of r is {r}")
            else:
                print("Please enter a valid value of pi")          

    elif carea == "area of sector":
        theta = int(input("What is the value of theta or angle>>"))
        r = float(input("What is the radius>>"))
        pi = input("What is the value of pi>>")

        if pi == '22/7':
            area = (theta/360)*(22/7)*(r**2)
            print(f"The value of area is {area}")
        elif pi == '3.14':
            area = (theta/360)*(3.14)*(r**2)
            print(f"The value of area is {area}")
        else:
            print("Please enter a valid value of pi") 

    elif carea == "circumference of sector":
        theta = int(input("What is the value of theta or angle>>"))
        r = int(input("What is the radius>>"))
        pi = input("What is the value of pi>>")

        if pi == '22/7':
            circum = (theta/360)*(22/7)*r*2
            print(f"The value of circumference is {circum}")
        elif pi == '3.14':
            circum = (theta/360)*(3.14)*r*2
            print(f"The value of circumference is {circum}")
        else:
            print("Please enter a valid value of pi") 

    elif carea == "angle of sector" or "theta":
        qtype = input("is the area given>>")
        if qtype == "yes":
            area = float(input("what is the area>>"))
            r = float(input('What is the raduis>>'))
            pi = input("What is the value of pi>>")

            if pi == '22/7':
                theta = ((area/(r*r))*(7/22))*360
                print(f"The value of angle is {theta}")
            elif pi == '3.14':
                theta = ((area/(r*r))*(1/3.14))*360
                print(f"The value of angle is {theta}")
            else:
                print("Please enter a valid value of pi") 


        elif qtype == 'no':   
            circum = float(input("what is the circumference>>"))
            r = float(input('What is the raduis>>'))
            pi = input("What is the value of pi>>")

            if pi == '22/7':
                theta = (circum/2)*(7/22)*(1/r)*360
                print(f"The value of angle is {theta}")
            elif pi == '3.14':
                theta = (circum/2)*(1/3.14)*(1/r)*360
                print(f"The value of amgle is {theta}")
            else:
                print("Please enter a valid value of pi") 
