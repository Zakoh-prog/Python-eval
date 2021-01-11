a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


def getMinusNumbers(nb):
    b=[]
    for i in range(0,len(a)):
        if a[i] < nb :
            b.append(a[i])
    return b

def start():
    try:
        reponse= input("Enter a number: ")
        print(getMinusNumbers(int(reponse)))
        
    except ValueError:
       print("Oops!  That was no valid number.  Try again...")
       start()
    

start()



