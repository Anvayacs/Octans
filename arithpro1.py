def ap_sum():
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

def ap_firstTerm():
    gterm = int(input("What is the given term>>"))
    numterm = int(input("which number of term is given ? >>"))
    dterm = int (input("What is the difference between the terms>>"))
    fterm = gterm - ((numterm-1)*dterm)
    print('Steps to solve')
    print("firsrt term = give  term - (number of giver term - 1)*d")
    print( 'The first term is' ,fterm, )    


def ap_lastTerm():
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


def ap_anyTerm():
    qtype = input("Is the first term given?>>")
    if qtype=="yes": 
        numterm = int(input("Which term is required>> "))
        aterm = int(input("First Term>> "))
        dterm= int(input("Difference between the terms>> "))  
        rterm = aterm + (numterm-1)*dterm
        print(f'The required term is {rterm}')         

    elif qtype == "no":
        numterm = int(input("Which term is required>> "))
        lterm = int(input("last Term>> "))
        dterm= int(input("Difference between the terms>> "))  
        rterm = lterm - (numterm-1)*dterm
        print(f'The required term is {rterm}')                
