# Graphic Pandoc – Convertisseur graphique pour Pandoc

Un outil graphique minimaliste (Tkinter) pour interagir avec [Pandoc](https://pandoc.org/) sans passer par la ligne de commande.

> ✨ Conçu pour des usages éditoriaux et scientifiques : prise en charge des bibliographies, styles CSL, et formats multiples (Markdown, LaTeX, PDF, DOCX, etc.).

---

## 🖥️ Fonctionnalités

- Sélection du fichier source via interface graphique
- Choix du format d’entrée et de sortie
- Export en `.pdf`, `.html`, `.docx`, `.odt`, `.epub`, etc.
- Ajout d’une bibliographie BibTeX (`.bib`)
- Application d’un style CSL (`.csl`)
- Options Pandoc disponibles :
  - `--standalone`
  - `--toc`
  - `--citeproc` (activé automatiquement si `.bib` fourni)

---

## 🚀 Installation

### 1. Installer Python (si ce n’est pas déjà fait)

Téléchargez-le depuis : [https://www.python.org/downloads/](https://www.python.org/downloads/)

### 2. Cloner le dépôt

```bash
git clone https://github.com/tonygheeraert/pandoc-gui.git
cd pandoc-gui

### 3. Installer Pandoc

Téléchargez Pandoc depuis le site officiel :  
👉 [https://pandoc.org/install.html](https://pandoc.org/install.html)

> ✅ Assurez-vous que la commande `pandoc` fonctionne dans votre terminal :

```bash
pandoc --version

## ▶️ Lancer l’application

Dans le terminal, à la racine du projet, exécutez :

```bash
python pandoc_gui.py

L’interface graphique s’ouvre et vous permet de sélectionner vos fichiers et options de conversion.

## 📦 Dépendances

Ce projet repose sur :

- **Python 3.x**
- **Tkinter** (inclus par défaut avec Python)
- **Pandoc** (à installer séparément)

> ✅ Aucune dépendance externe via `pip` n’est requise.

---

## 📚 Exemple d’usage

- Fichier source : `mon_article.md`
- Bibliographie : `biblio.bib`
- Style CSL : `apa.csl`
- Format de sortie : `PDF`

L’application génère automatiquement une commande Pandoc équivalente à :

```bash
pandoc mon_article.md -f markdown -t pdf -o mon_article.pdf \
  --standalone --toc --bibliography biblio.bib --csl apa.csl --citeproc

## 🔧 Développements prévus

- Ajout de templates personnalisés (`--template`)
- Prise en charge des filtres Lua (`--lua-filter`)
- Enregistrement et chargement de profils de conversion (`.json`)
- Conversion en lot de plusieurs fichiers
- Prévisualisation du rendu HTML dans une fenêtre

---

## 📄 Licence

**MIT** — Utilisation, modification et redistribution autorisées.

---

## ✉️ Contact

Développé par **Tony Gheeraert** (Université de Rouen Normandie) à partir de [Pandoc](https://pandoc.org/)

