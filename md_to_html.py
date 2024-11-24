import sys
import markdown

# Parametri da riga di comando
input_file = sys.argv[1]
output_file = sys.argv[2]

# CSS da includere
css = '<link rel="stylesheet" href="styles1.css">'

# Conversione da Markdown a HTML
with open(input_file, 'r') as f:
    md_content = f.read()

html = markdown.markdown(md_content)
html_with_css = f'{css}\n{html}'

# Salva il risultato come file HTML
with open(output_file, 'w') as f:
    f.write(html_with_css)
