import json

arquivo =  open('Prova_Infra.json')
__json = json.load(arquivo)
json_formatado = json.dumps(__json, indent=4)
arquivo.close()

print(json_formatado)