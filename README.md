# Rodark 🤖

**Rodark** est un assistant virtuel intelligent basé sur Python, conçu pour interagir via la voix, fournir des informations en temps réel et contrôler des périphériques matériels (comme des LEDs APA102). 

Que ce soit pour jouer de la musique, consulter la météo, rechercher des informations sur Wikipédia ou simplement discuter, Rodark est là pour vous aider.

---

## 🌟 Fonctionnalités

- 🎙️ **Reconnaissance Vocale** : Utilise Google Speech Recognition pour comprendre vos commandes.
- 🗣️ **Synthèse Vocale (TTS)** : Répond vocalement via `pyttsx3` ou `gTTS`.
- 🎵 **Divertissement** :
  - Joue n'importe quelle chanson directement sur YouTube.
  - Raconte des blagues pour détendre l'atmosphère.
- ℹ️ **Informations & Recherche** :
  - Résumés Wikipédia sur n'importe quel sujet ou personne.
  - Recherche Google intégrée avec traduction automatique.
  - Rapports météo détaillés (température, humidité, météo actuelle).
- 🕒 **Utilitaires** : Donne l'heure et la date actuelle.
- 💡 **Rétroaction Visuelle** : Support pour les LEDs APA102 (DotStar) pour indiquer les états de l'assistant (écoute, réflexion, parole).
- ⚙️ **Commandes Système** : Possibilité de redémarrer le système à la voix.

---

## 🏗️ Structure du Projet

Le projet est divisé en plusieurs modules clés :

- **`main.py`** : Le point d'entrée principal. Il gère la boucle d'écoute et la logique de base des commandes.
- **`action.py`** : Contient la logique complexe pour les recherches Google, Wikipédia, la météo et la gestion du temps.
- **`pixels.py`** : Gère les effets lumineux des LEDs APA102 pour une interaction visuelle.
- **`valib.py`** : Un module alternatif utilisant `gTTS` pour une synthèse vocale plus naturelle (notamment en français).
- **`apa102.py`** : Interface de bas niveau pour le matériel LED.

---

## 🛠️ Installation

### Prérequis

- Python 3.x
- Un microphone fonctionnel
- (Optionnel) Matériel LED APA102 (pour le support visuel)

### Étapes

1. **Cloner le projet** :
   ```bash
   git clone <url-du-repo>
   cd Rodark
   ```

2. **Créer un environnement virtuel** (recommandé) :
   ```bash
   python -m venv venv
   source venv/bin/activate  # Sur Windows: venv\Scripts\activate
   ```

3. **Installer les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```

4. **Configuration additionnelle** :
   Certaines bibliothèques comme `PyAudio` peuvent nécessiter des dépendances système supplémentaires (ex: `portaudio`).

---

## 🚀 Utilisation

Pour lancer l'assistant, exécutez simplement :

```bash
python main.py
```

### Exemples de commandes

- *"Play Bohemian Rhapsody"* -> Lance la chanson sur YouTube.
- *"Tell me the time"* -> Rodark vous donne l'heure actuelle.
- *"Who is Albert Einstein"* -> Donne un résumé Wikipédia.
- *"Tell me a joke"* -> Rodark vous raconte une blague.
- *"How is the weather in Paris"* -> (Fonctionnalité en cours d'intégration dans la boucle principale).

---

## 📝 Notes

Le projet est actuellement en cours de développement ("in construction"). Il peut y avoir des erreurs occasionnelles ou des fonctionnalités partiellement implémentées (comme la gestion complète de la météo dans `main.py`).
