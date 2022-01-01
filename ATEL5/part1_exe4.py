# la defintion de la classe point 
class Point :
    Px=0.0
    Py=0.0
    # le constructeur 
    def __init__(self,arg1=0.0,arg2=0.0):
        self.Px=arg1
        self.Py=arg2

# la classe segment 
class Segment :
     orig=Point()
     extrem=Point()
     def __init__(self,x=0,y=0,z=0,t=0):
        self.orig.Px=x
        self.orig.Py=y
        self.extrem.Px=z
        self.extrem.Py=t
     def display(self):
         print(" Voila un segment :",end=' ')
         for i in range(1,self.extrem.Px-self.orig.Px +1 ):
             if(i==1 or  i==self.extrem.Px-self.orig.Px  ):
                 print("*",end='')
             else:
                 print("-",end='')
         print("\n")

# une methode auto-test qui n'apparient pas à une classe 
def auto_test():
    test=Segment(1,2,3,4)
    test.display()

# le programme principale : appel a la methode auto-test pour test la classe 

print("******************** testing a pyhton programme ****************************")
auto_test()
print("******************** The end ***********************************************")


