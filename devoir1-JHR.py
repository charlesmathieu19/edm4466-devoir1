### BONJOUR CHARLES, ICI JEAN-HUGUES ROY
### TOUS MES COMMENTAIRES SERONT EN MAJUSCULES ET PRÉCÉDÉS DE 3 # (HASHTAGS)

# coding : utf-8

campus = []
for m in range(20000, 30151):
    url = 'https://montrealcampus.ca?p={}'.format(m)
    campus.append(url)
print(*campus, sep='\n') ### WOAH! VOILÀ DES PARAMÈTRES DE "PRINT" QUE JE NE CONNAISSAIS PAS! MERCI!
### COMME DIRAIT NEIL DEGRASSE TYSON: "There’s no shame in admitting what you don’t know. The only shame is pretending you know all the answers."
print(type(campus), len(campus))

### RIEN À AJOUTER! VOILÀ EXACTEMENT DE QUE JE VOUS DEMANDAIS DE FAIRE!
### NE MANQUAIT QUE DES COMMENTAIRES POUR EXPLIQUER CE QUE TON CODE FAIT.
### C'EST UNE BONNE HABITUDE À PRENDRE SI TU TRAVAILLES EN ÉQUIPE AFIN DE PERMETTRE AUX AUTRES DE COMPRENDRE TON CODE.