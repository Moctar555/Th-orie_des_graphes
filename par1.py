import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# =====================================================================
# PARTIE 1 : INITIALISATION - Structures de données et configuration
# =====================================================================
def initialiser_structures():
    """Initialise les structures de données et relations prédéfinies"""
    print("==========================================================================")
    print("Bienvenue vous pouvez commencer la création de votre graphe d'entreprise")
    print("==========================================================================")
    
    # Types de nœuds et relations prédéfinies
    node_types = ['client', 'entreprise', 'ville', 'pays', 'numero', 'produit', 'employe', 'livreur', 'magasin']
    
    relations = {
        ('client', 'entreprise'): 'contact',
        ('client', 'ville'): 'vie à',
        ('client', 'numero'): 'à un',
        ('client', 'produit'): 'commande',
        ('entreprise', 'ville'): 'est dans',
        ('ville', 'pays'): 'se trouve',
        ('employe', 'ville'): 'habite à',
        ('livreur', 'ville'): 'vie à',
        ('employe', 'entreprise'): 'travail dans',
        ('livreur', 'entreprise'): 'travail avec',
        ('produit', 'magasin'): 'stocker dans',
        ('magasin', 'entreprise'): 'gérer par',
        ('employe', 'employe'): 'collabore avec'
    }
    
    # Dictionnaire pour stocker les nœuds
    nodes = {t: [] for t in node_types}
    
    return node_types, relations, nodes


# =====================================================================
# PARTIE 2 : SAISIE UTILISATEUR - Nœuds et relations
# =====================================================================

import networkx as nx

def saisir_noeuds(node_types, nodes):
    """Demande à l'utilisateur de saisir les nœuds"""
    for node_type in node_types:
        count = int(input(f"Entrer le nombre de nœuds pour le type '{node_type}': "))
        if count > 0:
            print(f"Entrer les nœuds pour {node_type}:")
            for i in range(1, count + 1):
                node_name = input(f"{node_type} {i}: ").strip()
                nodes[node_type].append(node_name)
    return nodes

def saisir_relations(nodes, relations):
    """Demande à l'utilisateur de définir les relations entre les nœuds"""
    G = nx.DiGraph()
    
    # Ajout des nœuds avec leurs types
    for node_type, node_list in nodes.items():
        for node in node_list:
            G.add_node(node, type=node_type)
    
    print("\nDéfinir les relations (tapez 'fin' pour terminer)")
    while True:
        source = input("\nSource: ").strip()
        if source.lower() == 'fin':
            break
        cible = input("Cible: ").strip()
        
        # Trouver les types des nœuds
        src_type = next((t for t, lst in nodes.items() if source in lst), None)
        cbl_type = next((t for t, lst in nodes.items() if cible in lst), None)
        
        if not src_type or not cbl_type:
            print("Erreur: Nœud(s) inconnu(s)")
            continue
        
        # Trouver la relation appropriée
        relation = relations.get((src_type, cbl_type))
        if relation:
            G.add_edge(source, cible, label=relation)
            print(f"{source} -----{relation}-----> {cible}")
        else:
            print(f"Aucune relation prédéfinie entre {src_type} et {cbl_type}")
            custom_rel = input("Entrer le nom de la relation personnalisée: ").strip()
            if custom_rel:
                G.add_edge(source, cible, label=custom_rel)
                print(f"{source} -----{custom_rel}-----> {cible}")
            else:
                print("Relation non ajoutée")
    
    return G


# =====================================================================
# PARTIE 4 : PROGRAMME PRINCIPAL - Orchestration des fonctions
# =====================================================================

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def main():
    # Initialisation des structures
    node_types, relations, nodes = initialiser_structures()
    
    # Saisie des nœuds
    nodes = saisir_noeuds(node_types, nodes)
    
    # Saisie des relations
    G = saisir_relations(nodes, relations)
    
    # Configuration des couleurs
    node_colors = configurer_couleurs()
    
    # Affichage du graphe
    afficher_graphe(G, node_colors)

if __name__ == "__main__":
    main()