import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os

FORMATS = [
    "markdown", "html", "latex", "docx", "pdf", "odt", "epub", "tei", "txt"
]

def choisir_fichier():
    fichier = filedialog.askopenfilename()
    if fichier:
        entree_entry.delete(0, tk.END)
        entree_entry.insert(0, fichier)

def choisir_bib():
    fichier = filedialog.askopenfilename(filetypes=[("BibTeX", "*.bib")])
    if fichier:
        bib_entry.delete(0, tk.END)
        bib_entry.insert(0, fichier)

def choisir_csl():
    fichier = filedialog.askopenfilename(filetypes=[("Citation Style Language", "*.csl")])
    if fichier:
        csl_entry.delete(0, tk.END)
        csl_entry.insert(0, fichier)

def convertir():
    source = entree_entry.get().strip()
    sortie = sortie_entry.get().strip()
    format_entree = entree_format_var.get()
    format_sortie = sortie_format_var.get()
    options = []

    if standalone_var.get():
        options.append("--standalone")
    if toc_var.get():
        options.append("--toc")

    # Ajout des fichiers bib et csl
    bibfile = bib_entry.get().strip()
    if bibfile:
        options.extend(["--bibliography", bibfile, "--citeproc"])

    cslfile = csl_entry.get().strip()
    if cslfile:
        options.extend(["--csl", cslfile])

    if not os.path.exists(source):
        messagebox.showerror("Erreur", "Le fichier source est introuvable.")
        return

    cmd = [
        "pandoc", source,
        "-f", format_entree,
        "-t", format_sortie,
        "-o", sortie
    ] + options

    try:
        subprocess.run(cmd, check=True)
        messagebox.showinfo("Succès", f"Fichier converti :\n{sortie}")
    except subprocess.CalledProcessError:
        messagebox.showerror("Erreur", f"La conversion a échoué.\n\nCommande :\n{' '.join(cmd)}")

# Interface
racine = tk.Tk()
racine.title("Convertisseur Pandoc avec bibliographie")

# Source
tk.Label(racine, text="Fichier source :").grid(row=0, column=0, sticky="e", padx=5, pady=5)
entree_entry = tk.Entry(racine, width=50)
entree_entry.grid(row=0, column=1, padx=5)
tk.Button(racine, text="Parcourir...", command=choisir_fichier).grid(row=0, column=2, padx=5)

# Format d'entrée
tk.Label(racine, text="Format d’entrée :").grid(row=1, column=0, sticky="e", padx=5)
entree_format_var = tk.StringVar(value="markdown")
tk.OptionMenu(racine, entree_format_var, *FORMATS).grid(row=1, column=1, sticky="w", padx=5)

# Format de sortie
tk.Label(racine, text="Format de sortie :").grid(row=2, column=0, sticky="e", padx=5)
sortie_format_var = tk.StringVar(value="pdf")
tk.OptionMenu(racine, sortie_format_var, *FORMATS).grid(row=2, column=1, sticky="w", padx=5)

# Nom du fichier de sortie
tk.Label(racine, text="Fichier de sortie :").grid(row=3, column=0, sticky="e", padx=5, pady=5)
sortie_entry = tk.Entry(racine, width=50)
sortie_entry.grid(row=3, column=1, padx=5)

# Bibliographie
tk.Label(racine, text="Fichier .bib :").grid(row=4, column=0, sticky="e", padx=5)
bib_entry = tk.Entry(racine, width=50)
bib_entry.grid(row=4, column=1, padx=5)
tk.Button(racine, text="Choisir...", command=choisir_bib).grid(row=4, column=2, padx=5)

# CSL
tk.Label(racine, text="Fichier .csl :").grid(row=5, column=0, sticky="e", padx=5)
csl_entry = tk.Entry(racine, width=50)
csl_entry.grid(row=5, column=1, padx=5)
tk.Button(racine, text="Choisir...", command=choisir_csl).grid(row=5, column=2, padx=5)

# Options
standalone_var = tk.BooleanVar()
tk.Checkbutton(racine, text="--standalone", variable=standalone_var).grid(row=6, column=1, sticky="w", padx=5)

toc_var = tk.BooleanVar()
tk.Checkbutton(racine, text="--toc (table des matières)", variable=toc_var).grid(row=7, column=1, sticky="w", padx=5)

# Convertir
tk.Button(racine, text="Convertir", command=convertir, bg="#4CAF50", fg="white").grid(row=8, column=1, pady=10)

racine.mainloop()
