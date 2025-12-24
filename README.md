# 🏎️ Mario Kart - Jeu de Course Python
<img width="997" height="788" alt="image" src="https://github.com/user-attachments/assets/cd5d1d35-6241-4549-9a8d-3333febd7c8f" />


Un jeu de course inspiré de Mario Kart développé en Python avec Tkinter. Collectez des pièces, débloquez de nouvelles voitures et évitez les obstacles !

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📸 Aperçu

Un jeu de course 2D vue de dessus où vous contrôlez différents personnages de Mario Kart, collectez des pièces dorées et évitez les obstacles pour obtenir le meilleur score !

## ✨ Fonctionnalités

- 🏁 **6 personnages jouables** : Mario, Luigi, Peach, Bowser, Yoshi et Toad
- 💰 **Système de pièces** : Collectez des pièces pour débloquer de nouvelles voitures
- 🚗 **Voitures uniques** : Chaque personnage a ses propres caractéristiques de vitesse
- 🎮 **Contrôles fluides** : Accélération, freinage et direction réactifs
- 📊 **Système de score** : Gagnez des points en évitant les obstacles et en collectant des pièces
- 🔓 **Progression** : Débloquez des voitures plus rapides avec vos pièces

## 🎮 Contrôles

| Touche | Action |
|--------|--------|
| ⬅️ Flèche Gauche | Tourner à gauche |
| ➡️ Flèche Droite | Tourner à droite |
| ⬆️ Flèche Haut | Accélérer |
| ⬇️ Flèche Bas | Freiner |

## 🚀 Installation

### Prérequis

- Python 3.7 ou supérieur
- Tkinter (généralement inclus avec Python)

### Étapes d'installation

1. Clonez ce repository :
```bash
git clone https://github.com/votre-username/mario-kart-python.git
cd mario-kart-python
```

2. Vérifiez que Python est installé :
```bash
python --version
```

3. Lancez le jeu :
```bash
python mario_kart.py
```

> **Note** : Tkinter est généralement préinstallé avec Python. Si ce n'est pas le cas :
> - **Ubuntu/Debian** : `sudo apt-get install python3-tk`
> - **Fedora** : `sudo dnf install python3-tkinter`
> - **macOS** : Tkinter devrait être inclus avec Python
> - **Windows** : Tkinter est inclus dans l'installateur officiel de Python

## 🏎️ Personnages et Statistiques

| Personnage | Couleur | Vitesse Max | Coût |
|------------|---------|-------------|------|
| 🔴 Mario | Rouge | 8.0 | Gratuit |
| 🟢 Luigi | Vert | 7.5 | 50 💰 |
| 🩷 Peach | Rose | 7.0 | 100 💰 |
| 🟠 Bowser | Orange | 9.0 | 150 💰 |
| 🟢 Yoshi | Vert citron | 8.5 | 200 💰 |
| 🔵 Toad | Bleu | 7.0 | 250 💰 |

## 🎯 Comment Jouer

1. **Démarrage** : Lancez le jeu et vous verrez le menu principal
2. **Sélection** : Cliquez sur "JOUER" pour choisir votre voiture
3. **Déblocage** : Utilisez vos pièces pour débloquer de nouvelles voitures dans le garage
4. **Course** : Évitez les autres voitures et collectez un maximum de pièces
5. **Progression** : Plus vous collectez de pièces, plus vous débloquez de véhicules rapides !

### Conseils de jeu

- 💰 Chaque pièce collectée rapporte **+5 points** et **1 pièce**
- 🚗 Éviter un obstacle rapporte **+10 points**
- ⚡ Bowser est la voiture la plus rapide mais coûte cher
- 🏆 Les pièces sont conservées entre les parties, continuez à jouer pour tout débloquer !

## 📁 Structure du Projet

```
mario-kart-python/
│
├── mario_kart.py          # Fichier principal du jeu
├── README.md              # Ce fichier
└── LICENSE                # Licence MIT
```

## 🛠️ Technologies Utilisées

- **Python 3.7+** : Langage de programmation principal
- **Tkinter** : Bibliothèque GUI pour l'interface graphique
- **Math** : Pour les calculs de rotation et de mouvement

## 🤝 Contribution

Les contributions sont les bienvenues ! Pour contribuer :

1. Forkez le projet
2. Créez votre branche de fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. Committez vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Poussez vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

## 📝 Idées d'Améliorations

- [ ] Ajouter des power-ups (champignons, étoiles, carapaces)
- [ ] Système de niveaux avec difficultés croissantes
- [ ] Musique et effets sonores
- [ ] Classement des meilleurs scores
- [ ] Mode multijoueur local
- [ ] Différents circuits/pistes
- [ ] Animations plus fluides
- [ ] Sauvegarde persistante des scores

## 🐛 Problèmes Connus

- Le jeu nécessite une fenêtre active pour les contrôles
- Pas de sauvegarde persistante des pièces (réinitialisation au redémarrage)

## 📜 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 👨‍💻 Auteur

Créé avec ❤️ par un développeur passionné de jeux rétro

## 🙏 Remerciements

- Inspiré par le jeu original Mario Kart de Nintendo
- Merci à la communauté Python pour les excellentes bibliothèques
- Tkinter pour rendre le développement GUI accessible

---

⭐ Si vous aimez ce projet, n'hésitez pas à lui donner une étoile sur GitHub !

🎮 Amusez-vous bien et que le meilleur pilote gagne ! 🏁
