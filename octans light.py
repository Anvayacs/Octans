def optic():
    print('Please enter all the values according to the type of mirror/lens')

query = input('what do you want to do>> ')
if query == 'light':
    qtype = input('what do you want to find>> (image distance, object distance, focal length \n magnification, power)')
    if qtype == 'image distance':
        qtype2 = input('Is the magnification given>> (yes or no) ')
        qtype3 = input('is it mirror or lens>> ')
        optic() 
        if qtype3 == 'mirror':
            if qtype2 == 'no':
                u = float(input('please enter object distance>> '))
                f = int(input('please enter the focal length>> ')) 
                v = 1/((1/f)-(1/u))
                print(f'the value of image distance is {v}')

            if qtype2 == 'yes':
                m = float(input('what is the magnification>> '))
                u = float(input('please enter object distance>> '))
                v = (-m)*u
                print(f'the value of image distance is {round(v)} units')
        if qtype3 == 'lens':
            
            if qtype2 == 'no':
                u = float(input('please enter object distance>> '))
                f = float(input('please enter the focal length>> ')) 
                v = 1/((1/f)+(1/u))
                print(f'the value of image distance is {round(v)} units')
            if qtype2 == 'yes':
                m = float(input('what is the magnification>> '))
                u = float(input('please enter object distance>> '))
                v = (m)*u
                print(f'the value of image distance is {round(v)} units')
                
    if qtype == 'object distance':
        qtype3 = input('is it a mirror or a lens>> ')
        qtype2 = input('Is the magnification given>> (yes or no) ')
        optic()
        if qtype3 == 'mirror': 
            if qtype2 == 'no':
                v = float(input('please enter image distance>> '))
                f = int(input('please enter the focal length>> ')) 
                u = 1/((1/f)-(1/v))
                print(f'the value of object distance is {round(u)}')

            if qtype2 == 'yes':
                m = float(input('what is the magnification>> '))
                v = float(input('please enter image distance>> '))
                u = (-v)/m
                print(f'the value of object distance is {round(u)}')

        if qtype3 == 'lens': 
            if qtype2 == 'no':
                v = float(input('please enter image distance>> '))
                f = float(input('please enter the focal length>> ')) 
                u = -1/((1/f)-(1/v))
                print(f'the value of object distance is {round(u)} units')
            if qtype2 == 'yes':
                m = float(input('what is the magnification>> '))
                v = float(input('please enter image distance>> '))
                u = v/m
                print(f'the value of image distance is {round(u)} units')

    if qtype == 'focal length':
        qtype2 = input('Is the device a mirror or a lens>>> ')
        
        if qtype2 == 'mirror':
            v = int(input('Please enter the image distance>>>' )) 
            u = int(input('Please enter the object distance>>>' ))
            f = 1/((1/v) + (1/u))   
            print(f'the focal lenght of the mirror is {f}')
        if qtype2 == 'lens':
            v = int(input('Please enter the image distance>>>' )) 
            u = int(input('Please enter the object distance>>>' ))
            f = 1/((1/v) - (1/u))   
            print(f'the focal lenght of the lens is {f}')

    if qtype == 'magnification':
        qtype3 = input('are heights given>>>(yes/no)')
        if qtype3 == 'yes':
            imageHeight = int(input('please enter image height>> '))
            objectHeight = int(input('please enter image height>> '))
            m = imageHeight/objectHeight
            print('the magnification is' ,m)
        else:
            qtype2 = input('Is the device a mirror or a lens>>> ')
            if qtype2 == 'mirror':
                v = int(input('Please enter the image distance>>>' )) 
                u = int(input('Please enter the object distance>>>' ))
                m = -v/u 
                print(f'the focal lenght of the mirror is {m}')
            if qtype2 == 'lens':
                v = int(input('Please enter the image distance>>>' )) 
                u = int(input('Please enter the object distance>>>' ))
                m = v/u  
                print(f'the focal lenght of the lens is {m}')

    if qtype == 'power':
        f = int(input('Please enter focal length in meters'))
        d = 1/f 
        print(f'the focal lenght of the mirror is {d} dioptres')