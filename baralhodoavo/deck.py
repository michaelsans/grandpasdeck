import csv
import random
from lor_deckcodes import LoRDeck, CardCodeAndCount

result = None

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

            #[0]nome [1]região [2]raridade [3]codigo da carta
            #Proibido escolher a mesma carta duas vezes
            for x in listaDeck:
                nomedacarta = listaCarta[pos][0]
                if x == nomedacarta:
                    pos = random.randint(1, len(listaCarta) -1)
            
            #a carta deve pertencer à alguma das regiões escolhidas anteriormente e deve ser colecionável
            if listaCarta[pos][2] != 'None' and (listaCarta[pos][1] == escolhaCor[0] or listaCarta[pos][1] == escolhaCor[1]):
                #escolhe um valor entre 1 e 3, esse valor vai ser a quantidade de cópias da carta escolhida
                numeroDeCartas = random.randint(1, 3)
                contador += numeroDeCartas

                #o numero maximo de campeoes é 6
                if listaCarta[pos][2] == "Champion" and contadordeCampeos <= 6:
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

print(a)
        
        