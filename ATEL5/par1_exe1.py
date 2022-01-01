 # La definition de la classe 
class Vecteur2D:
    x=0
    y=0
    def __init__(self,arg1=0,arg2=0): # le constructeur qui initialise 
                                      # les données si les parametres ne sont pas passés
        self.x=arg1
        self.y=arg2

# on va tester la classe avec des objet X, Y
X=Vecteur2D()
Y=Vecteur2D(12.0,-5)
# voila un vecteur 2D nul
print(" les coordonnees cartesinnes sont : ( ",X.x," ; ",X.y," )")

# voila un vecteur 2D dans le plan 
print(" les coordonnees cartesinnes sont : ( ",Y.x," ; ",Y.y," )")


    