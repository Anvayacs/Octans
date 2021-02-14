
#possibilities 
#area
#cicumference
#sector area
#sector cicumference
#theta 
#area when circum given 
#circumference when area given

query = input("what do you want ot solve>>")
if query == 'area realted to circle' or 'circle related area':
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
