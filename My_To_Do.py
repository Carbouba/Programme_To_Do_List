# Les fonctions
def charge_taches():
    return
def sauver_taches():
    return
def ajouter():
    print("===== Nouvelle tâche =====")
    nom_tache = input("Nom de la tâche : ")
    for tache in taches:
        if tache in taches:
            print("La tâche existe déjâ.")

    return
def supprimer():
    return
def voir_taches():
    return

# Programme pricipale
taches = []
while True:
    try:
        
        print("\n\n====== MENU ======\n")
        print("1. Voir les tâches")
        print("2. Ajouter une tâche ")
        print("3. Supprimer une tâche (C'est le défi !")
        print("4. Vider toute la liste")
        print("5. Quitter")
        print("====================")

        option = int(input("\nVeuillez choisir une option (1-3) : "))
    except ValueError:
        print("\n❌ Erreur : Vous devez entré un  CHIFFRE, pas une lettre.")
        continue

    match option:
        case 1:
            voir_taches()
        case 2:
            ajouter()
        case 3:
            supprimer()
        case 4:
            print("\nAu revoir ! ")
            break
