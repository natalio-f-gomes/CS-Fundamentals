def Fibonacci(nterms):
    n1,n2 = 0,1
    count=0
    if nterms<0:
        print("Please input a positve number! ")
    elif nterms==1:
        print(n1)
    else:
        while count<nterms:
            print(n1)
            count +=1
            nth = n1+n2
            n1 = n2
            n2 = nth
            
            
nterms = eval(input("Enter number o terms you would like to print: "))

Fibonacci(nterms)
