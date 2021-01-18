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

            
    elif (anga + angb + angc) != 180 or anga<=0:   
        print ("This triangle is not valid")


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

        
    elif (anga + angb + angc) != 180 or angb<=0:   
        print ("This triangle is not valid") 


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

            
    elif (anga + angb + angc) != 180 or angb<=0:   
        print ("This triangle is not valid") 
