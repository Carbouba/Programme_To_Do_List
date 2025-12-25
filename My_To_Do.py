# Les fonctions
def charge_taches():
    try:
        with open("Cahier_tâches", "r") as f:
            # for tache in f:
                tache = f.read()
                taches.append(tache)
    except FileNotFoundError:
        return 0
    except ValueError:
        print("❌ Erreur : Aucune tâche ajouté pour le moment !")

def sauver_taches(nouvelle_tache):
    with open("Cahier_tâches", "a") as f:
            f.write(f"{nouvelle_tache}\n")
    return

def ajouter():
    print("\n===== ➕ Ajout d'une nouvelle tâche ➕ =====")
    nom_tache = input("Nom de la tâche : ")
    if nom_tache.lower() in taches:
        print("❌ Erreur : La tâche existe déjâ.")
    else:
        taches.append(nom_tache.lower())
        print("✅ Nouvelle tâche ajouté avec succée !")

        sauver_taches(nom_tache)
    return

def supprimer():
    return
def voir_taches():
    nombre_taches = len(taches)
    if nombre_taches == 0:
        print("❌ Erreur : Aucune tâche ajouté pour le moment !")
    else:
        print("===== Liste des tâches =====")
        for tache in taches:
            print(f"{tache}")
        print("====================")
    return

# Programme pricipale
taches = []
charge_taches()

while True:
    try:
        
        print("\n\n====== MENU ======\n")
        print("1. Voir les tâches")
        print("2. Ajouter une tâche ")
        print("3. Supprimer une tâche")
        print("4. Vider toute la liste")
        print("5. Quitter")
        print("====================")

        option = int(input("\nVeuillez choisir une option : "))
        print("\n")
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
