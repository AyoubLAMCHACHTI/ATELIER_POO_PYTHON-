# La definition de la classe 
class Vecteur2D:
    x=0
    y=0
    def __init__(self,arg1=0,arg2=0): # le constructeur qui initialise 
                                      # les données si les parametres ne sont pas passés
        self.x=arg1
        self.y=arg2
    def display(self):
        print(" les coordonnees cartesinnes sont : ( ",self.x," ; ",self.y," )")
    def combinateVECT(self,vect2):
        tmp=Vecteur2D()
        tmp.x=self.x+vect2.x
        tmp.y=self.y+vect2.y
        return tmp

# let's test it 

N=Vecteur2D(12.6,-66)
M=Vecteur2D(3,9)
print("\n\n\n########################## la somme de 2 vecteurs ###############")
sum=N.combinateVECT(M)
sum=sum.display()