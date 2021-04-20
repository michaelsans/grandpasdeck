from django.shortcuts import render
import requests
import csv
import random
from lor_deckcodes import LoRDeck, CardCodeAndCount

singleton = False

def home(request):
    return render(request,'trueHome.html')

def about(request):
    return render(request,'about.html')

def button(request):
    return render(request,'standard.html')

def output(request):
    for x in range(8):
        try:
            with open ('cartas.csv') as csv_file:
                listaCarta = list(csv.reader(csv_file))
            #aqui está a lógica que vai criar um deck aleatorio com 40 cartas
            #iniciando listas e contadores       
            listaDeck = []
            novodeck = []
            #imagem dos Campeoes
            a = {}
            #imagem dos Feiticos
            b = {}
            #imagem das Unidades
            c = {}
            copias = []
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
                            a[str(listaCarta[pos][5]) + str(listaCarta[pos][0])] = (listaCarta[pos][6])
                        elif listaCarta[pos][2] != 'Champion' and listaCarta[pos][4] == 'Unit':
                            c[str(listaCarta[pos][5]) + str(listaCarta[pos][0])] = (listaCarta[pos][6])
                        elif listaCarta[pos][2] != 'Champion' and listaCarta[pos][4] == 'Spell':
                            b[str(listaCarta[pos][5]) + str(listaCarta[pos][0])] = (listaCarta[pos][6])
                        cartaENumDeCartas = str(numeroDeCartas) + ':' + str(listaCarta[pos][3])
                        novodeck.append(cartaENumDeCartas)
            deck = LoRDeck(novodeck[:len(novodeck)])
            data = deck.encode()
            str_error = None
        except:
            pass
    
    # ordenar as cartas
    imagemCampeoes = []
    for key in sorted(a):
        imagemCampeoes.append(a[key])
    imagemFeiticos = []
    for key in sorted(b):
        imagemFeiticos.append(b[key])
    imagemUnidades = []
    for key in sorted(c):
        imagemUnidades.append(c[key])
    
    return render(request,'standard.html',{'data':data,'imagemCampeoes':imagemCampeoes, 'imagemFeiticos':imagemFeiticos, 'imagemUnidades':imagemUnidades, 'copias':copias})

def Singleton(request):
    for x in range(8):
        try:
            with open ('cartas.csv') as csv_file:
                listaCarta = list(csv.reader(csv_file))
            #aqui está a lógica que vai criar um deck aleatorio com 40 cartas
            #iniciando listas e contadores       
            listaDeck = []
            novodeck = []
            #imagem dos Campeoes
            a = {}
            #imagem dos Feiticos
            b = {}
            #imagem das Unidades
            c = {}
            copias = []
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
                    #escolhe 1 carta
                    numeroDeCartas = 1
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
                            a[str(listaCarta[pos][5]) + str(listaCarta[pos][0])] = (listaCarta[pos][6])
                        elif listaCarta[pos][2] != 'Champion' and listaCarta[pos][4] == 'Unit':
                            c[str(listaCarta[pos][5]) + str(listaCarta[pos][0])] = (listaCarta[pos][6])
                        elif listaCarta[pos][2] != 'Champion' and listaCarta[pos][4] == 'Spell':
                            b[str(listaCarta[pos][5]) + str(listaCarta[pos][0])] = (listaCarta[pos][6])
                        
                        listaDeck.append(listaCarta[pos][0])
                        cartaENumDeCartas = str(numeroDeCartas) + ':' + str(listaCarta[pos][3])
                        copias.append(str(numeroDeCartas))
                        novodeck.append(cartaENumDeCartas)
                        #print(numeroDeCartas)
            if len(novodeck) == 40:
                deck = LoRDeck([novodeck[0],novodeck[1],novodeck[2],novodeck[3],novodeck[4],novodeck[5],novodeck[6],novodeck[7],novodeck[8],novodeck[9],novodeck[10],novodeck[11],novodeck[12],novodeck[13],novodeck[14],novodeck[15],novodeck[16],novodeck[17],novodeck[18],novodeck[19],novodeck[20],novodeck[21],novodeck[22],novodeck[23],novodeck[24],novodeck[25],novodeck[26],novodeck[27],novodeck[28],novodeck[29],novodeck[30],novodeck[31],novodeck[32],novodeck[33],novodeck[34],novodeck[35],novodeck[36],novodeck[37],novodeck[38],novodeck[39]])	 
            #returns encoded string 
            data = deck.encode()
            str_error = None
        except:
            pass
    
    # ordenar as cartas
    imagemCampeoes = []
    for key in sorted(a):
        imagemCampeoes.append(a[key])
    imagemFeiticos = []
    for key in sorted(b):
        imagemFeiticos.append(b[key])
    imagemUnidades = []
    for key in sorted(c):
        imagemUnidades.append(c[key])
       
    #print(contador) 
    #print(novodeck)
    return render(request, 'Singleton.html',{'data':data, 'imagemCampeoes':imagemCampeoes, 'imagemFeiticos':imagemFeiticos, 'imagemUnidades':imagemUnidades, 'copias':copias})

  