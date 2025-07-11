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
# PARTIE 3 : VISUALISATION - Configuration et affichage du graphe
# =====================================================================
import networkx as nx
import matplotlib.pyplot as plt

def configurer_couleurs():
    """Définit la palette de couleurs pour les types de nœuds"""
    return {
        'client': '#FF9999',     # Rouge clair
        'entreprise': '#9999FF', # Bleu clair
        'ville': '#99FF99',      # Vert clair
        'pays': '#FFCC99',       # Orange clair
        'numero': '#CCCCCC',     # Gris
        'produit': '#FF99FF',    # Rose
        'employe': '#FFFF99',    # Jaune
        'livreur': '#99FFFF',    # Cyan
        'magasin': '#FFCCCC'     # Rose pâle
    }

def afficher_graphe(G, node_colors):
    """Crée et affiche la visualisation du graphe"""
    plt.figure(figsize=(14, 10))
    
    # Utiliser une disposition automatique
    pos = nx.spring_layout(G, seed=42, k=0.8)
    
    # Dessin des nœuds
    for node_type, color in node_colors.items():
        nodelist = [node for node, data in G.nodes(data=True) if data.get('type') == node_type]
        if nodelist:
            nx.draw_networkx_nodes(
                G, pos, 
                nodelist=nodelist, 
                node_color=color, 
                node_size=2000, 
                label=node_type
            )
    
    # Dessin des étiquettes de nœuds
    nx.draw_networkx_labels(G, pos, font_size=9)
    
    # Dessin des arêtes avec des flèches
    nx.draw_networkx_edges(
        G, pos, 
        edgelist=G.edges(), 
        arrowstyle='->', 
        arrowsize=25, 
        edge_color='gray',
        width=1.5,
        node_size=2000
    )
    
    # Dessin des étiquettes de relations
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
    
    # Légende et titre
    plt.legend(scatterpoints=1)
    plt.title("Graphe de la gestion d'une Entreprise")
    plt.axis("off")
    plt.tight_layout()
    plt.show()
    
    print("==========================================================================")
    print("Graphe généré avec succès")
    print("==========================================================================")

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