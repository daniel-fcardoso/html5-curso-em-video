# Bibliotecas
import os
import sys


# Conteúdo dos arquivos

conteudo_readme = """# Flask Generator

A simple Python script that automatically creates the basic structure of a Flask project.
"""

conteudo_layout = """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}Meu Site{% endblock %}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
    <link rel="icon" href="{{ url_for('static', filename='favicon.ico') }}" type="image/x-icon">
    <script src="{{ url_for('static', filename='js/script.js') }}"></script>
</head>
<body>

<header>
    <h1>Cabeçalho Fixo</h1>
</header>

<main>
    {% block content %}{% endblock %}
</main>

<footer>
    <p>Rodapé Fixo</p>
</footer>

</body>
</html>
"""


conteudo_index = """{% extends "layout.html" %}

{% block title %}Página Inicial{% endblock %}

{% block content %}
<h2>Bem-vindo à página inicial!</h2>
<p>Este conteúdo fica dentro da tag main.</p>
{% endblock %}
"""


conteudo_app = """from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
"""


conteudo_gitignore = """
__pycache__/
*.pyc
.venv/
.env
.vscode/
instance/
"""


conteudo_requirements = """Flask
"""


# Pegar nome do projeto
def get_project_name():

    if len(sys.argv) < 2:
        print("Usage: python flask_generator.py project_name")
        sys.exit()

    return sys.argv[1]


# Criar caminhos
def create_paths(project_name):

    flask_project = project_name

    paths = {
        "project": flask_project,
        "templates": os.path.join(flask_project, "templates"),
        "static": os.path.join(flask_project, "static"),
        "img": os.path.join(flask_project, "static", "img"),
        "css": os.path.join(flask_project, "static", "css"),
        "js": os.path.join(flask_project, "static", "js"),

        "layout": os.path.join(flask_project, "templates", "layout.html"),
        "index": os.path.join(flask_project, "templates", "index.html"),
        "app": os.path.join(flask_project, "app.py"),
        "readme": os.path.join(flask_project, "README.md"),
        "gitignore": os.path.join(flask_project, ".gitignore"),
        "requirements": os.path.join(flask_project, "requirements.txt"),
        "env": os.path.join(flask_project, ".env"),

        "styles": os.path.join(flask_project, "static", "css", "styles.css"),
        "script": os.path.join(flask_project, "static", "js", "script.js")
    }

    return paths



# Criar pastas
def create_folders(paths):

    os.makedirs(paths["templates"], exist_ok=True)
    os.makedirs(paths["static"], exist_ok=True)
    os.makedirs(paths["img"], exist_ok=True)
    os.makedirs(paths["css"], exist_ok=True)
    os.makedirs(paths["js"], exist_ok=True)



# Escrever arquivos
def write_file(path, content=""):

    with open(path, "w", encoding="utf-8") as file:
        file.write(content)



def create_project(paths):

    write_file(paths["layout"], conteudo_layout)
    write_file(paths["index"], conteudo_index)
    write_file(paths["app"], conteudo_app)
    write_file(paths["readme"], conteudo_readme)
    write_file(paths["gitignore"], conteudo_gitignore)
    write_file(paths["requirements"], conteudo_requirements)

    write_file(paths["styles"])
    write_file(paths["script"])
    write_file(paths["env"])



# Execução

project_name = get_project_name()

paths = create_paths(project_name)

create_folders(paths)

create_project(paths)


print(f"""
🔥 Flask project created successfully!

Project: {project_name}

Created:
✓ app.py
✓ templates/
✓ static/
✓ README.md
✓ requirements.txt
✓ .gitignore
✓ .env
""")