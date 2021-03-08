"""
#  ask for what do you want to find 
#  v u f magnification power
#  v
#  if magnification given?
#  mirror or lens?
#  u  
#  if magnification is given ?
#  mirror or lense?
 f 
 is v and u given or dioptre?
 mirror or lens
 ask what is given for magnification
 ask if height is given or distance is given
 power
 """
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
            """
            if qtype2 == 'no':
                u = float(input('please enter object distance>> '))
                f = float(input('please enter the focal length>> ')) 
                v = 1/((1/u)+(1/f))
                print(f'the value of image distance is {round(v)} units')
            if qtype2 == 'yes':
                m = float(input('what is the magnification>> '))
                u = float(input('please enter object distance>> '))
                v = (m)*u
                print(f'the value of image distance is {round(v)} units')
            """    
    if qtype == 'object distance':
        qtype2 = input('Is the magnification given>> (yes or no) ')
        optic() 
        if qtype2 == 'no':
            v = float(input('please enter image distance>> '))
            f = int(input('please enter the focal length>> ')) 
            u = 1/((1/f)-(1/v))
            print(f'the value of object distance is {u}')

        if qtype2 == 'yes':
            m = float(input('what is the magnification>> '))
            v = float(input('please enter image distance>> '))
            u = (-m)*v
            print(f'the value of object distance is {u}')

    if qtype == 'focal length':
        pass

