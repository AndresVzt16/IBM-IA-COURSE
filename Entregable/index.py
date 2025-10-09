""" declaracion de menu de chatbot """
menuChat = {
    "Titulo": "Titulo",
    "Problema": "Problema",
    "Solucion": "Solucion",
    "Caracteristicas": "Caracteristicas",
    "Pasos": "Pasos",
    "Diagrama de flujo": "Diagrama de flujo",
    "Pseudocodigo": "Pseudocodigo",
    "Ejecucion del programa": "Ejecucion del programa"
}

""" lectura de datos de readme """
with open("readme.md", "r", encoding="utf-8") as file:
    data = file.read()
    sections = data.split('--- IGNORE ---')
    title = sections[0].strip().replace("# ", "")
    menuChat["Titulo"] = title  
    menuChat["Problema"] = sections[1].strip().replace("# ", "")
    menuChat["Solucion"] = sections[2].strip().replace("# ", "")
    menuChat["Caracteristicas"] = sections[3].strip().replace("# ", "")
    menuChat["Pasos"] = sections[4].strip().replace("# ", "")
    menuChat["Diagrama de flujo"] = sections[5].strip().replace("# ", "")
    menuChat["Pseudocodigo"] = sections[6].strip().replace("# ", "")
    menuChat["Ejecucion del programa"] = sections[7].strip().replace("# ", "")
    file.close()
""" fin lectura de datos de readme """