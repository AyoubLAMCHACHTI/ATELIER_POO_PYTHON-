class Etudiant:

    #constructeur
    def init(self,nom,prenom,age,cne,moyenne):
          self.nom=nom
          self.prenom=prenom
          self.age=age
          self.cne=cne
          self.moyenne=moyenne





def TRIPARAGE(liste):
  permut = True
  while (permut==True):
    permut = False
    for j in range(0,len(liste)-1):
      if (liste[j].age < liste[j+1].age) :
       tmp = liste[j+1]
       liste[j+1] = liste[j]
       liste[j] = tmp
       permut = True



def TRIPARMOY(liste): 
  permut = True
  while (permut==True):
    permut = False
    for j in range(0,len(liste)-1):
      if (liste[j].moyenne > liste[j+1].moyenne) :
       tmp = liste[j+1]
       liste[j+1] = liste[j]
       liste[j] = tmp
       permut = True



#lise vide
Etu_list=[]

#Remplissage du liste au hasard
Etu_list.append(Etudiant("Said","Nassim",30,"KB121314",12.40))
Etu_list.append(Etudiant("Ouadie","Dada",20,"KB123314",17.80))
Etu_list.append(Etudiant("Siham","Wissal",34,"KB212134",9.40))
Etu_list.append(Etudiant("Omar","Barcelona",33,"KB111344",20.00))
#Tri du liste selon l'age
TRIPARAGE(Etu_list)
print("==============================Tri selon l'age===================================")
for etudiant in Etu_list:
    print("Nom : ",etudiant.nom)
    print("Preom : ",etudiant.prenom)
    print("CNE : ",etudiant.cne)
    print("Age: ",etudiant.age,"ans")
    print("Moyenne : ",etudiant.moyenne)
    print("-----------------------------------------------------------------------------------------------")
print("===============================================================================================")

#Tri la liste selon la moyenne
TRIPARMOY(Etu_list)
print("==============================Tri selon la moyenne=================================")
for etudiant in Etu_list:
    print("Nom : ",etudiant.nom)
    print("Preom : ",etudiant.prenom)
    print("CNE : ",etudiant.cne)
    print("Age: ",etudiant.age,"ans")
    print("Moyenne : ",etudiant.moyenne)
    print("-----------------------------------------------------------------------------------------------")
print("===============================================================================================")
