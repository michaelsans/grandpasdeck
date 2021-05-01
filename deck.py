import csv
import random
from lor_deckcodes import LoRDeck, CardCodeAndCount

result = None
with open ('swindecks.csv') as csv_file:
        listaCarta = list(csv.reader(csv_file))
        pos = random.randint(1, len(listaCarta)-1)
        nomedeck = listaCarta[pos][0]
        codigodeck = listaCarta[pos][1]
        guiadeck = listaCarta[pos][3]
        carta1 = listaCarta[pos][4]
        carta2 = listaCarta[pos][5]
        carta3 = listaCarta[pos][6]
    return

for x in range(8):
    try:
        with open ('cartas.csv') as csv_file:
            listaCarta = list(csv.reader(csv_file))
        #aqui está a lógica que vai criar um deck aleatorio com 40 cartas
        #iniciando listas e contadores       
        listaDeck = []
        novodeck = []
        imagemCampeoes = {}
        imagemFeiticos = {}
        imagemUnidades = {}
        contador = 1
        contadordeCampeos = 0
        cor = ['Freljord', 'Demacia', 'Ionia', 'ShadowIsles', 'PiltoverZaun', 'Noxus', 'Targon', 'Shurima', 'Vazio']
        #escolhe 2 regiões aleatoriamentes, tem uma chance de escolher apenas uma região
        escolhaCor = random.choices(cor, k = 2)


        #loop que escolhe uma carta aleatoria, há restrições nas escolhas
        while contador < 41:
            
            
            #escolhe uma carta aleatoria
            pos = random.randint(1, len(listaCarta))
            for x in listaDeck:
                    if x == listaCarta[pos][0]:
                        pos = random.randint(1, len(listaCarta))
            #a carta deve pertencer à alguma das regiões escolhidas anteriormente e deve ser colecionável
            if listaCarta[pos][2] != 'None' and (listaCarta[pos][1] == escolhaCor[0] or listaCarta[pos][1] == escolhaCor[1]):
                #escolhe um valor entre 1 e 3, esse valor vai ser a quantidade de cópias da carta escolhida
                numeroDeCartas = random.randint(1, 3)
                contador += numeroDeCartas
                #checa se uma carta com nome igual ja esta no deck
                #o numero maximo de campeoes é 6
                if listaCarta[pos][2] == "Champion" and contadordeCampeos <= 5:
                    contadordeCampeos = numeroDeCartas
                
                #o numero de cartas no deck não pode ser maior do que 40 e o numero de campeoes nao pode ser maior que 6
                if contador > 41 or contadordeCampeos > 6:
                    contador -= numeroDeCartas

                #esse laço continua ate completar o deck com 40 cartas
                elif contador <= 41:
                    if listaCarta[pos][2] == 'Champion':
                        imagemCampeoes[str(listaCarta[pos][5]) + str(listaCarta[pos][0])] = (listaCarta[pos][6])
                    elif listaCarta[pos][2] != 'Champion' and listaCarta[pos][4] == 'Unit':
                        imagemUnidades[str(listaCarta[pos][5]) + str(listaCarta[pos][0])] = (listaCarta[pos][6])
                    elif listaCarta[pos][2] != 'Champion' and listaCarta[pos][4] == 'Spell':
                        imagemFeiticos[str(listaCarta[pos][5]) + str(listaCarta[pos][0])] = (listaCarta[pos][6])
                    listaDeck.append(listaCarta[pos][0])
                    cartaENumDeCartas = str(numeroDeCartas) + ':' + str(listaCarta[pos][3])
                    novodeck.append(cartaENumDeCartas)

        deck = LoRDeck(novodeck[:len(novodeck)])
        result = str(deck.encode())   

        str_error = None
    except Exception:
        pass

a = []
for key in sorted(imagemUnidades):
        a.append(imagemUnidades[key])

print(result)
        
        