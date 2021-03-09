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
import math

query = input("Which chapter or formula do you want to solve>> ")

if query == 'real numbers':
    qtype = input('what do you want to find out>> LCM, HCF, Proof of irrationality, other term when hcf and lcm given>> ')
    if qtype == 'LCM':
        qtype2 = input('is hcf also given with terms>> (yes or no) ')
        if qtype2 == 'yes':
            hcf = int(input('what is the hcf>> '))
            t1 = int(input('What is the first term>> '))
            t2 = int(input('what is the second term>> '))
            lcm = (t1*t2)/hcf
            print(f'The lcm is {lcm}')

        if qtype2 == 'no':
            t1 = int(input('What is the first term>> '))
            t2 = int(input('what is the second term>> '))
            lcm = lcm(t1,t2)
            print(f'The lcm is {lcm}')

    if qtype == 'HCF':
        qtype2 = input('Is lcm given with the terms>> (yes or no) ')
        if qtype2 == 'yes':
            lcm = int(input('what is the lcm>> '))
            t1 = int(input('What is the first term>> '))
            t2 = int(input('what is the second term>> '))
            hcf = (t1*t2)/lcm
            print(f'The lcm is {hcf}')

        if qtype2 == 'no':
            t1 = int(input('What is the first term>> '))
            t2 = int(input('what is the second term>> '))
            hcf = math.gcd(t1, t2)
            print(f'The lcm is {hcf}')

    if qtype == 'proof of irrationality':
        qtype2 = input('What is the type of question (root x, root x + y, root x -y)')
        if qtype2 == 'root x':
            x = int(input('what is the value of x>> '))
            print("following are the steps>> ")
            print(f"Bye method of contradiction: \nlet root {x} = p/q \n where p and q are co-prime and q is not equal to 0")
            print(f'=> {x} = p^2/q^2 \n=> {x}*q^2 = p^2\n=>p^2 is a multiple of {x} \n=> p is a multiple of {x}--->(1)\n=> p can be written as {x}a')
            print(f'=> p = {x**2}a^2\n=> {x}*q^2 = {x**2}a^2 => p^2 = {x}a^2 \n=> p^2 is a multiple of x \n=> p is  a multiple of x--->(2)')
            print(f'=>By 1 and 2 we get that p and q are not co prime \n hence our assumption of root{x} as rational was incorrect')
            print(f'Therefore root{x} is irrational') 

    if qtype == 'other term when hcf and lcm given':
        hcf = int(input('what is the hcf>> '))
        lcm = int(input('what is the lcm>> '))
        t1 = int(input('what is the given term>> '))
        t2 = (lcm*hcf)/t1
        print(f'The other term is {t2}')
