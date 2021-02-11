
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

    if carea == "area of circle" or "circle area":
        qtype = input("Is the circumference given>>")

        if qtype == "Yes" or "yes":
            circum= float(input("what is the circumference>>"))
            pi = int(input("What should pi be taken as>>"))

            if pi == '22/7':
                r = circum*(7/22)*(1/2)
                area = (22/7)*(r**2) 
                print(f"The area is {area}")

            elif pi == "3.14":
                r = circum*(1/3.14)*(1/2)
                area = (22/7)*(r**2)
                print(f"The area is {area}")
            else:
                print("Please enter a valid value of pi")         
        
        elif qtype == 'No' or 'no':
            r = input("What is the radius>>")
            pi = (input("What should pi be taken as>>"))
            if pi == '22/7':
                area = (22/7)*(r**2)

            elif pi == "3.14":
                    area = (3.14)*(r**2)
        
    if carea == "circumference":
        qtype= input("Is the area given>> ")
        
        if qtype == "yes":
            area = float(input("What is the area>>")) 
            pi = input("What is the value of pi>>")

            if pi == '22/7':
                r = area *(7/22)**(0.5)
                circum = 2*(22/7)*(r) 
            elif pi == '3.14':
                r = area*(1/3.14)**(0.5)
                circum = 2*(3.14)*(r) 
            else:
                print("Please enter a valid value of pi")                    
    
    if carea == "radius":
        qtype = input("Is the area given>> ")
        if qtype == "yes":
            area = input ("What is the area?")
            pi = input("What is the value of pi>>")

            if pi == '22/7':
                r = area *(7/22)**(0.5)
                print(f"The value of r is {r}")
            elif pi == '3.14':
                r = area*(1/3.14)**(0.5)
                print(f"The value of r is {r}")
            else:
                print("Please enter a valid value of pi")  

        if qtype == "no":
            circum = input ("What is the circumference?")
            pi = input("What is the value of pi>>")

            if pi == '22/7':
                r = (circum/2) * (7/22) 
                print(f"The value of r is {r}")
            elif pi == '3.14':
                r = r = (circum/2) * (1/3.14)
                print(f"The value of r is {r}")
            else:
                print("Please enter a valid value of pi")          

    if carea == "area of sector":
        theta = input("What is the value of tehta or angle>>")
        r = input("What is the radius>>")
        pi = input("What is the value of pi>>")

        if pi == '22/7':
            area = (theta/360)*(22/7)*(r**2)
            print(f"The value of area is {area}")
        elif pi == '3.14':
            area = (theta/360)*(3.14)*(r**2)
            print(f"The value of area is {area}")
        else:
            print("Please enter a valid value of pi") 

    if carea == "cicumference of sector":
        theta = input("What is the value of tehta or angle>>")
        r = input("What is the radius>>")
        pi = input("What is the value of pi>>")

        if pi == '22/7':
            circum = (theta/360)*(22/7)*r*2
            print(f"The value of circumference is {circum}")
        elif pi == '3.14':
            circum = (theta/360)*(3.14)*r*2
            print(f"The value of circumference is {circum}")
        else:
            print("Please enter a valid value of pi") 

    if carea == "angle of sector":
        qtype = input("is the area given>>")
        if qtype == "yes":
            area = input("what is the area>>")
            r = input('Whta is the raduis>>')
            pi = input("What is the value of pi>>")

            if pi == '22/7':
                theta = area *(7/22)**(0.5)*360
                print(f"The value of angle is {theta}")
            elif pi == '3.14':
                theta = area*(1/3.14)**(0.5)*360
                print(f"The value of angle is {theta}")
            else:
                print("Please enter a valid value of pi") 


        elif qtype == 'no':   
            circum = input("what is the circumference>>")
            r = input('Whta is the raduis>>')
            pi = input("What is the value of pi>>")

            if pi == '22/7':
                theta = circum*(7/22)*(0.5)*360
                print(f"The value of angle is {theta}")
            elif pi == '3.14':
                theta = circum*(1/3.14)*(0.5)*360
                print(f"The value of amgle is {theta}")
            else:
                print("Please enter a valid value of pi") 
