import math

print("Voici un calculateur Python de Pythagore!")
reponse_choix = input("Que voulez-vous connaitre !(hypothènuse [h] ou  cathète [c])")
a = int(input("Quelle est la longueur du premier cathètes ?"))
if reponse_choix.lower() == "h":
    b = int(input("Quelle est la longueur du deuxième cathètes ?"))
    x = a**2 + b**2
    x = math.sqrt(x)
    print(f"L'hypothènuse vaut: {x}")

if reponse_choix.lower() == "c":
    b = int(input("Quelle est la longueur de l'hypothènuse ?"))
    x = b**2 - a**2
    x = math.sqrt(x)
    print(f"Le deuxième cathète vaut: {x}")
