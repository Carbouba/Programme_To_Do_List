# Les fonctions
def charge_taches():
    try:
        with open("Cahier_taches.txt", "r") as f:
            for ligne in f:
                lign_propre = ligne.strip()
                taches.append(lign_propre)
    except FileNotFoundError:
        return 0
    except ValueError:
        print("❌ Erreur : Aucune tâche ajouté pour le moment !")

def sauver_taches():
    with open("Cahier_taches.txt", "w") as f:
            for tache in taches:
                f.write(f"{tache}\n")
    return

def ajouter():
    print("\n===== ➕ Ajout d'une nouvelle tâche ➕ =====")
    nom_tache = input("Nom de la tâche : ")
    if nom_tache.lower() in taches:
        print("❌ Erreur : La tâche existe déjâ.")
    else:
        taches.append(nom_tache.lower())
        print("✅ Nouvelle tâche ajouté avec succée !")

        sauver_taches()
    return

def supprimer():
    nombre_taches = len(taches)
    if nombre_taches == 0:
        print("❌ Erreur : Aucune tâche ajouté pour le moment !")
        return
    else:
        print("===== Liste des tâches =====")
        for i, tache in enumerate(taches, start= 1):
            print(f"N°{i} : {tache.capitalize()}")
        print("====================")
    try:
        tache_supp = int(input("\nVeuillez saisir le numéro de la tache a supprimer : "))
        index = tache_supp - 1
        if 0 <= index < len(taches):
            tache_enlevee = taches.pop(index)        
            print(f"🗑️ Tâche '{tache_enlevee}' supprimée !")
            sauver_taches()
        else:
            print("❌ Erreur : Ce numéro n'existe pas.")
    except ValueError:
        print("\n❌ Erreur : Vous devez entré un  CHIFFRE, pas une lettre.")


def voir_taches():
    nombre_taches = len(taches)
    if nombre_taches == 0:
        print("❌ Erreur : Aucune tâche ajouté pour le moment !")
    else:
        print("===== Liste des tâches =====")
        for i, tache in enumerate(taches, start= 1):
            print(f"N°{i} : {tache.capitalize()}")
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
        print("4. Quitter")
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
