# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 16:40:48 2020

@author: utilisateur
"""
import re
import random

print('Bienvenu sur le mini chat bot !')
print('--> tapez \'sortir\' pour quitter')


bonjour = ('bonjour|bjr|salut|slt')

meteo_user = ('temps|meteo|temperature')
meteo_bot = ('Ici il fait beau !','Le ciel est couvert ici sur la Lune forestière d\'Endor')

message_bot = ('Vous pouvez formuler la quesiton autrement ?','Je ne réponds pas à cette quetion')

humeur_user = ('(ca va|ça va|va bien)')
humeur_bot = ('Les droids vont toujours bien','Heureux quand vous êtes la mon maître')

nom_user = ('(.ton nom.*)|(.ton prenom.*)|(.comment tu t\'appelles.*)|(.ton prenom.*)')
nom_bot = ('Je m\'appelle R2D2 le Droid, pour vous servir')

lieu_vie_user= ('(où habite.*|où es-tu.*|où vis.*)')

flag= True

while flag == True:

    x = input("-> ")
    x = x.lower()         
    if x == 'sortir':
        print('A bientôt')
        flag=False
        
    elif (re.fullmatch(bonjour,x)):
        print('Salut, c\'est moi R2D2, le petit ChatBot, et vous ?')
        x = input("-> ")
        print('Bonjour {}, en quoi puis-je vous aider ?'.format(x))
        x = input("-> ")
        
    elif (re.fullmatch(meteo_user,x)):
        print(random.choice(meteo_bot))
        
    elif (re.search(humeur_user,x)):
        print(random.choice(humeur_bot))
        
    elif (re.fullmatch(nom_user,x)):
        print(nom_bot)
        
    elif (re.search(lieu_vie_user,x)):
        print('Je suis actuellement sur Lune forestière d\'Endor, en mission secrète')
                
    else:
        print(random.choice(message_bot))
        
    