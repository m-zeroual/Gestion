def Ajouter_un_personne():
    t=[]
    nom_et_prenom=input("donner le nom et prénom :")
    cin=input("donner le CIN :")
    salaire=float(input("donner le salaire :"))
    t.append(nom_et_prenom)
    t.append(cin)
    t.append(salaire)
    f=open("les_personne.txt","a")
    for i in range (0,3):
        lis=t[i]
        f.write(str(t[i])+ "\t"+"\t")
    f.write("\n")
    f.close()
    print("le personne et Ajouter")
def rechercher():
    cin=input("donner un CIN :")
    f=open("les_personne.txt","r")
    lis=(f.read())
    if cin in lis:
        print("Ce CIN et déja")
        f.close()
    else:
        print("Ce CIN ni pas dans ce fichier")

def supprimer():
    cin=input("donner un CIN :")
    f=open("les_personne.txt","r")
    lis=(f.readlines())
    f.close()
    for i in lis:
        if cin in i:
            lis.remove(i)
    f=open("les_personne.txt","w")       
    for i in lis:
        f.write(i)
    f.close()
    
def afficher_tous():
    f=open("les_personne.txt","r")
    l=(f.read())
    for i in l:
        print(i ,end="")
def menu():
    print("----------MENU----------")
    print("")
    print("1-Ajouter un personne ")
    print("2-Rechercher")
    print("3-supprimer")
    print("4-Afficher tous ")
    print("5-Quitter")
    
check = True
while(check):
    menu()
    n=int(input("donner votre choix :"))
    if (n>0 and n==1) :
        Ajouter_un_personne()
    elif n>0 and n==2 :
        rechercher()
    elif n>0 and n==3 :
        supprimer()
    elif n>0 and n==4 :
        afficher_tous()
    elif n>0 and n==5 :
        check = False
    else:
        print("votre choix incourect")
    
