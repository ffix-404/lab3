X=int(input("enter a number of repetitions"))

def repetitions (func):
    def inside():
        for _ in range(0,X):
          func()
    return inside    

            
@repetitions
def hello():
    print("hello")
hello()    



