#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 19:30:15 2016

@author: Tristan
"""

class C:  #definition de la classe norme commence par une majuscule
    x = 1
    
I = C()  # création d'une instance de class

C.__dict__ #espace de nommage de la class grace à l'attribut __dict__

I.__dict__ #espace de nommage de l'instance

I.x #ramene 1 qui es la valeur de l'attribut de class

I.__class__ # identifie à quelle classe appartient l'attribut

C.y = 10
C.x = 5 # la classe est un objet mutable

C.__dict__ #liste les variables de C

I.x  # I herite des variables ajoutées à C
I.y  # la résolution d'attribut est fait au moment de l'appel

"""methode = fonction de class 
necessite un paramètre self qui représente l'instance
"""
class C:
    x = 1
    def f(self, a):
        print (self.x)
        self.x=a

I = C()
I.f(5)   # 2 appels identiques
C.f(I,5) # 2 appels indentiques


class Personne:
    """Une personne possède un nom, un âge et une adresse e-mail"""
    
    def __init__(self, nom, age, email):
        self.nom = nom
        self.age = age
        self.email = email
        
    def __repr__(self):
        return "[{nom}, {age} ans, email:{email}]".\
            format(**vars(self)) 
        #la fonction vars retourne le dictionnaire des attributs d'un objets

personnes = [
    # on se fie à l'ordre des arguments dans le créateur
    Personne('pierre', 25, 'pierre@foo.com'),
    # ou bien on peut être explicite
    Personne(nom='paul', age=18, email='paul@bar.com'),
    # ou bien on mélange
    Personne('jacques', 52, email='jacques@cool.com'),
]
print (personnes)            
vars(personnes[0])
index_par_nom = {personne.nom: personne for personne in personnes}

print (index_par_nom['pierre'])

#on peut ajouter une fonction dynamiquement
def anniversaire(self): #on definit la fonction de la meme façon que dans la classe
    "Incrémente l'âge de la personne"
    self.age += 1

Personne.anniversaire = anniversaire #on ajoute la fonction à la classe
# on affecte la fonction ainsi définie à l'attribut anniversaire de l'objet classe

'''
0n peut attacher, au choix, à une instance ou à une classe, des attributs 
représentant n'importe quel objet, et la recherche de ces attributs se 
fait dans l'ordre instance puis classe '''

#Une instance herite d'une classe
#une classe peut heriter d'autres classes alors nommées superclasses
# la recherche des attributs va remonté l'arbre d'héritage
# Instance -> Classe --> Super Classe (dans l'autre sens classe/sous classe)

class C:
    def set_x(self, x):
        self.x=x
    def get_x(self):
        print (self.x)

class sousC(C): #si herite de plusieurs classe, priorité à gauche pour l'arbre
    def get_x(self):
        print ('x est :', self.x)

sc = sousC()


sousC.__bases__ #retourne un tuple de toutes les super classe d'une classe
# à partir de l'instance, l'interpreteur determine la classe avec l'argument
sc.__class__
#puis remonte toutes l'abre d'héritage avec bases

""" heritage
Une méthode héritée peut être rangée dans une de ces trois catégories :
    implicite : si la classe fille ne définit pas du tout la méthode,
    redéfinie : si on récrit la méthode entièrement,
    modifiée : si on récrit la méthode dans la classe fille, mais en utilisant le code de la classe mère.
"""
# Une classe mère
class Fleur(object):
    def implicite(self):
        print ('Fleur.implicite')
    def redefinie(self):
        print ('Fleur.redefinie')
    def modifiee(self):
        print ('Fleur.modifiee')

# Une classe fille
class Rose(Fleur):
    # on ne definit pas implicite
    # on redefinit complement redefinie
    def redefinie(self):
        print ('Rose.redefinie')
    def modifiee(self):
        Fleur.modifiee(self)
        print ('Rose.modifiee apres Fleur') 
        
"""Composition"""
# Une classe avec qui on n'aura pas de relation d'héritage
class Tige(object):
    def implicite(self):
        print 'Tige.implicite'
    def redefinie(self):
        print 'Tige.redefinie'
    def modifiee(self):
        print 'Tige.modifiee'

# on n'hérite pas
# mais on fait ce qu'on appelle un composition
# avec la classe Tige
class Rose(object):
    # mais pour chaque objet de la classe Rose
    # on va créer un objet de la classe Tige
    # et le conserver dans un champ
    def __init__(self):
        self.externe = Tige()

    # le reste est presque comme tout à l'heure
    # sauf qu'il faut definir implicite
    def implicite(self):
        self.externe.implicite()
        
    # on redefinit complement redefinie
    def redefinie(self):
        print 'Rose.redefinie'
        
    def modifiee(self):
        self.externe.modifiee()
        print 'Rose.modifiee apres Tige'  

Rose.mro() # affiche l'arbre de recherche dans l'ordre ou il va être executé
#MRO (Method Resolution Order)
# à noter que le MRO doit aboutir pour pouvoir créer une classe....

#Pour qu'une classe soit iterable il faut
#       une methode __iter__ 
#       une méthode __next__

"""Surcharge d'opérateur 
80 opérateurs peuvent être surchargés
ex print in +,-,*,/  <,>,== [], .....
"""
class C:
    def __init__(self, a): #constructeur d'instance
        print ('dans C')
        self.x = a
    def set_x(self, x):
        self.x=x
    def get_x(self):
        print (self.x)
    def __str__(self):    #methode d'affichage appellée par print
        return str(self.x)

class D(C):
    def __init__(self): #constructeur d'instance, pas d'héritage pas défaut
        C.__init__(self,100) #on rappelle l'init de C avec une constance
        print ('dans D')

class E(C):
    def __init__(self,a): #constructeur d'instance, pas d'héritage pas défaut
        C.__init__(self,a) #on rappelle l'init de C avec une var
        print ('dans E')
#le __str__ est hérité par défaut
__repr__(self) #retourne ce qu'affiche le terminal lors de l'appel de l'instance
__add__(self, other) #surcharge l'addition de 2 instances, permet de beneficier de sum()
__nonzero__(self) #retourn un booléen permettant de savoir si l'objet est null 
__eq__ __ne__(self, other) #surcharge == et <>
__lt__ __le__ __gt__ __ge__ (self, other)# surcharge < <= > >= (si OK, on peut appeler min et max)
__mul__(self, other) __rmul__(self,alpha) # surcharge la *, ou la multi de a  par une instance à droite (a*I)
__contains__ (self, item) # in, prend un objet et un item et retourne un bouleen
__len__(self) #surcharge le len (longueur d'un objet)
__getitem__(self, index) #permet d'acceder s&quentiellement
__getitem__(self, key) #pour gere le slice
if isinstance(key, slice): #je traite le slice
elif isinstance(key, int): #je traite l'acces par index
__call(self, *args)__ # rend l'objet appelable "callable", on peut donc ecrire objet(arg1,arg2)

