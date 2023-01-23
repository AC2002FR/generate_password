#Ce programme génère un mot de passe aléatoire de 30 caractère avec, au minimum : 1 majuscule, 1 minuscule, 1 chiffre et 1 caractère spécial.
import random 
#donne des fonctions pour générer des nombres aléatoires et sélectionner des éléments aléatoires d'une chaîne 
import string 
#donne des constantes utiles pour travailler avec des chaînes de caractères 
import pyperclip 
#copie dans le presse-papier automatique 
import time 
import os 
os.system('cls' if os.name == 'nt' else 'clear') 
#efface les lignes "PS C:\Users\andre> & "C:/Program Files/WindowsApps/PythonSoftwareFoundation.Python.3.10_3.10.2544.0_x64__qbz5n2kfra8p0/python3.10.exe" c:/Users/andre/Documents/Programmation/Python/generate_password.py" du terminal 
from termcolor import colored 
#pour mettre du texte en couleur dans le terminal 



def generate_password(): #définit une fonction qui sera utilisée pour générer un mot de passe aléatoire 
    upper_chars = string.ascii_uppercase #définit une variable qui contient toutes les lettres majuscules (uppercase) de l'alphabet ASCII 
    lower_chars = string.ascii_lowercase #définit une variable qui contient toutes les lettres minuscules (lowercase) de l'alphabet ASCII 
    numbers = string.digits #définit une variable qui contient tous les chiffres de 0 à 9 inclus 
    special_chars = string.punctuation.replace(" ", "") #définit une variable qui contient tous les caractères de ponctuation sauf l'espace 

    all_chars = upper_chars + lower_chars + numbers + special_chars #définit une variable qui contient tous les caractères définis ci-dessus 
    password = random.sample(all_chars, 30) #fonction qui sélectionne 30 caractères aléatoires de la chaîne "all_chars" et les affecte à "password" 
    password = "".join(password) #utilise la méthode "join()"" pour joindre les caractères sélectionnés pour créer un string affecté à "password"
    pyperclip.copy(password) #copie dans le presse-papier automatiquement 
    return password #retourne le mot de passe généré aléatoirement 



print("PASSWORD AUTO COPY IN THE CLIPBOARD ;)") 
print("") 
print(colored(generate_password(), 'yellow')) #affiche le mot de passe généré en jaune 
print("") 

for i in range(11, -1, -1): #décompte de 11 secondes avant de faire tourner la boucle 
    print("CLEAR IN : ",str(i).zfill(2)," seconds", end='\r', flush=True)
        #zfill permet de décaller les chiffres du décompte pour pas que les unités se retrouves sur les dizaines 
        #flush=True permet de forcer l'affichage de la sortie sans attendre un retour à la ligne (+ esthétique car sur 1 ligne) 
    time.sleep(1)
    if i == 0:
        os.system('cls' if os.name == 'nt' else 'clear') #efface les lignes affiché dans le terminal 
        break #arrete la boucle après le premier décompte 

print("PASSWORD AUTO COPY IN THE CLIPBOARD ;)")
print("")
print("_____E__N__D_____") 
