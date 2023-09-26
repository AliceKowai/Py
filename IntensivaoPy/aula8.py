#import aula3
#from aula3 import somar
import datetime
import json
with open('C:/Users/alice/Documents/Py/IntensivaoPy/aula8.json') as f: #pegar json externo
    jogador=json.load(f)
#aula3.soma()
#somar()


#data em python
data=datetime.datetime.now() #data atual com hora e minuto
nasc=datetime.datetime(1993,6,16)
print(data)
print(data.day,"/",data.month,"/", data.year)
print(nasc.strftime("%d"))
#outras opções para strtime
#dia da semana "%A", dia da semana completo "%a", dia do mes "%d", texto mes abreviado "%b" numero do mes "%n", etc

#json

gatos_json='{"Nome":"Floki", "Peso":"5kg", "cor":"Branco"}'

gatos=json.loads(gatos_json) #json sendo convertido para dicionario

for k,v in gatos.items(): #gatos.items(): gatos.values():
    print(k,v)

#gatos_json=json.dumps(gatos) isso é transformando um dicionario para json

#list = array = tupla
#nomeDaVariavel= json. dumps(listOuTuplaQueQueroConverter)
personagens={
    "Nome": "Sakura",
    "Cabelo":"Rosa",
    "Inteligente":"Sim",
    "Time": "Time 7",
    "Colegas de Time":["Naruto", "Sasuke", "Kakashi"],
    "Habilidades":[
        {"tipo":"Ninjutsu", "Nivel":8},
        {"tipo":"Taijutsu","Nivel":1},
        {"tipo":"Genjutsu", "Nivel":1}
    ]
}
personagens_json = '{"Nome": "Sakura", "Cabelo": "Rosa", "Inteligente": "Sim", "Time": "Time 7", "Colegas de Time": ["Naruto", "Sasuke", "Kakashi"], "Habilidades": [{"tipo": "Ninjutsu", "Nivel": 8}, {"tipo": "Taijutsu", "Nivel": 1}, {"tipo": "Genjutsu", "Nivel": 1}]}'
personagens_j = json.dumps(personagens, indent=8, separators=(":","----"), sort_keys=True) #formatar para json
personagens_dic = json.loads(personagens_json)
print(personagens_j)
print(personagens_dic)

for v in personagens_dic["Habilidades"]:
    print(v["tipo"])

for v in jogador.items():
    print(v)