import streamlit as st


st.image("assets/banner.png", use_container_width=True)
st.title("Application de détection du cancer du sein à partir de la mammographie")
st.markdown("""
    ### Ensemble de données

    Pour construire notre modèle de détection du cancer du sein, nous avons utilisé un ensemble de **7 632 mammographies**. Ces images ont été divisées en trois ensembles : **3 816 pour l'entraînement**, **1 908 pour la validation**, et **1 908 pour les tests**. Chaque image a été normalisée pour garantir une cohérence dans les données, ce qui permet au modèle de mieux apprendre les motifs distinctifs des cas bénins et malins. Toutes les images ont été redimensionnées à une résolution de **224×224 pixels**, assurant une compatibilité optimale avec notre pipeline.

    ### Architecture du modèle

    Nous avons conçu un réseau de neurones convolutif (CNN) axé sur la classification binaire. L'architecture comprend trois blocs de convolution suivis de couches de max-pooling pour extraire les caractéristiques importantes des mammographies. Ces caractéristiques sont ensuite aplaties et passées dans des couches entièrement connectées, avec un mécanisme de régularisation pour éviter le surapprentissage. Enfin, une couche de sortie avec une activation sigmoïde permet de prédire la probabilité qu'une image appartienne à la classe bénigne ou maligne.

    ### Entraînement du modèle

    Le modèle a été entraîné sur **25 époques**, avec un suivi minutieux des métriques de performance, telles que la perte et l'exactitude, pour l'ensemble d'entraînement et l'ensemble de validation. Grâce à un processus d'optimisation rigoureux, le modèle a progressivement appris à différencier les cas bénins et malins avec une précision croissante. Après l'entraînement, le modèle a atteint une précision de **90,2 %** sur l'ensemble de test, montrant une capacité significative à généraliser sur des données non vues.
""")
