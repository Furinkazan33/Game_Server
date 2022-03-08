#!/usr/bin/env python3
if __name__ == "__main__":
    import sys
    sys.path.append("./common")

    import Util
    from Item import *
    from Player import *
    from Map import *
    from Loader import Loader
    from event import *



    print("Demarrage du serveur")

    # Chargement de la carte
    map_main = Map()
    map_main.load("./data/map4020.txt")

    # chargement des items
    items = Loader.load(Item, "./data/items.txt")

    # main_loop()
        # Pour chaque connection de joueur:
            #ajout du joueur à la liste
            #envoi de la carte
            #envoi des items
            #envoi des positions des autres joueurs

        # A chaque maj de joueur (item/position):
            #envoi aux autres

        # Envois des messages serveurs aux joueurs

    #
    # Arrêt du serveur
    #
    # Envoi message de redémarrage aux joueurs

    # Sauvegarde des items et de la carte
    Loader.save(items, "./data/items.txt", ":")
    map_main.save("./data/_bak_map4020.txt")
    
    
