import json

def carregar_biblioteca():
    try:
        with open('biblioteca.json','r') as file:
            return json.load(file)

    except FileNotFoundError:
        return []
    
    except json.JSONDecodeError:
        return []

def salvar_biblioteca(biblioteca):
    with open("biblioteca.json", "w") as arquivo:
        json.dump(biblioteca, arquivo, indent=4)
