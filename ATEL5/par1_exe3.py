# La definition de la classse 
 
class Rectangle :
    nom="name"
    hauteur=0
    largeur=0
    # constructeur no parametré
    def __init__(self):
        self.hauteur=8
        self.largeur=5
        self.nom="rectangle"
    # affichage de la forme 
    def draw(self):
        if( self.hauteur==0 and self.largeur==0):
            print("impossible de dessiner la forme ")
        else:
            print("Voila une forme de "+self.nom)
            for i in range(0,self.largeur):
                for j in range(0,self.hauteur):
                    if(i==0 or i== self.largeur -1 or j==0 or j== self.hauteur-1):
                        print("*   ",end='')
                    else:
                        print("    ",end='')
                print("\n")
    # la surface 
    def area(self):
        return self.hauteur * self.largeur 
    # la finde la classe mere ( recrtangle )
# la classe heritée carree 
class Carre(Rectangle):
    def __init__(self):
        self.hauteur=self.largeur=4
        self.nom="Carree"
         

# les instances 
ABCD=Rectangle()
abcd=Carre()
ABCD.draw()
print(" sa surface est : ",ABCD.area())
abcd.draw()
print(" sa surface est : ",abcd.area())
