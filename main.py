cf74 = '/Users/arthurbinda/Desktop/TrabRI/cf74'
cf75 = '/Users/arthurbinda/Desktop/TrabRI/cf75'
cf76 = '/Users/arthurbinda/Desktop/TrabRI/cf76'
cf77 = '/Users/arthurbinda/Desktop/TrabRI/cf77'
cf78 = '/Users/arthurbinda/Desktop/TrabRI/cf78'
cf79 = '/Users/arthurbinda/Desktop/TrabRI/cf79'

vocabulario = dict({})
tagRn = 'RN'
tagPn = 'PN'
tagImportante = ['AU','TI','MJ','MN','AB','EX']
documentos = []
palavrasDocumento = []
identidadeDocumento = []
aux = 0
vetorDeDocumentos = {cf74,cf75,cf76,cf77,cf78,cf79}
#FUNCAO PARA INSERIR AS PALAVRAS NA HASH, PASSA A PALAVRA E O ID DO DOCUMENTO. ID DO DOCUMENTO EH O RN
def cadastraPalavras(palavrita,iddoc):
    word = palavrita
    veja = 0
    top = False
    if(word in vocabulario):
        tuplaRetornada = vocabulario[word]
        for i in range(0,len(tuplaRetornada)):
            #SE A CHAVE JA EXISTE, INCREMENTA O RF
            if (tuplaRetornada[i][0] == iddoc):
                neo = (iddoc,tuplaRetornada[i][1]+1)
                tuplaRetornada[i] = neo
                #amigo = amigo + 1
                #i = (iddoc,amigo)
                #vocabulario[word] = [i]
                top = True
                break
        if not top:
            vocabulario[word].append([iddoc,1])
    else:
            #SENAO ELE SO INSERE COM RF 1
        vocabulario[word] = [(iddoc,1)]

#AQUI COMECA TUDO
for doc in vetorDeDocumentos:
    with open(doc,'r') as D1:
        teste = D1.readlines()
        for line in teste:
            line = line.strip("\n").split(" ")
            #VERIFICA SE A LINHA QUE EU TO VENDO NA VDD E UMA TAG
            if (line[0] != ''):
                biu = line[0]
            #VERIFICA SE EH UM RN, ENTAO GUARDA NO VETOR O NUM DO DOCUMENTO E O INDICE
            if(biu == tagRn):
                cont = 0
                idDoc = line[1]
                identidadeDocumento.append(idDoc)
                cont = cont + 1
            #VERIFICA SE A TAG Q EU PEGUEI PRESTA PRA ALGUMA COISA, SE SIM GUARDA NUM VETOR DE DOCUMENTOS TUDO QUE ESTA ENTRE UMA TAG RELEVANTE E UMA IRRELEVANTE
            if(biu in tagImportante):
                palavrasDocumento += line
            elif(biu == 'PN' and palavrasDocumento != []):
                documentos.append([i.strip(".,:\n)(").lower() for i in palavrasDocumento if( i != ' ')])
                palavrasDocumento = []
#AQUI QUE A MAGIA COMECA, INDEXO UM DOCUMENTO DA LISTA DE DOCUMENTOS
for documento in documentos:
    #PASSO UMA PALAVRA DE CADA VEZ DE CADA DOCUMENTO
    for palavra in documento:
        #CADASTRO CADA PALAVRA ENQUANTO ESTA NO MESMO DOCUMENTO
        cadastraPalavras(palavra,identidadeDocumento[aux])
    aux = aux + 1

for x in vocabulario:
    print(x,"-",vocabulario[x])