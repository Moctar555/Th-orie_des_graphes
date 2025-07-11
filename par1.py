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
