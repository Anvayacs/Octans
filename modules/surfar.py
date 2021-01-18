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
            print ("The Volume of the given cube would be" ,volcube)

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
                aside = volcube**(1./3.)
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
                aside = volcube**(1./3.)
                print ("The edge in this instance is " ,tsacub)
        

    elif sa == 'cylinder':
        tysa2= input("Which formula would u like to use (tsa/csa/volume)>> ")
        if tysa2 == 'tsa':
            rcyl = int(input("What is the value of the radius>> "))
            hcyl = int(input("What is the value of the height>> "))
