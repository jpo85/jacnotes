# convert_md_to_html.py

import os
import markdown

# Percorso alla cartella con i file markdown
input_dir = '.'
output_dir = 'output'

# Crea la directory di output se non esiste
os.makedirs(output_dir, exist_ok=True)

# Scorri tutti i file nel repository
for root, dirs, files in os.walk(input_dir):
    for file in files:
        if file.endswith('.md'):
            # Leggi il file markdown
            with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                text = f.read()
            # Converti markdown in HTML
            html = markdown.markdown(text)
            # Nome del file di output
            output_file = os.path.join(output_dir, file.replace('.md', '.html'))
            # Scrivi l'output in un file HTML
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(html)
