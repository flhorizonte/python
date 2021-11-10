
#making 6x6 matriz
def matriz():
    matriz = []
    for i in range(0, 6):
        matriz.append([])
    cont = 0
    #colunas
    while cont < len(matriz):
        for x in range(len(matriz)):
            matriz[x].append(x)
        cont = cont + 1
    return matriz

def pattern():
    #iterar o array
    arr = matriz()
    linha = 0
    pattern = []
    
    coluna = 0
    while linha < len(arr):
        posi = 0
        while posi <= 3:
            limite = 0
            arr_sw = []
            for coluna in range(posi, len(arr)):
                if limite >= 3:
                    break
                arr_sw.append(arr[linha][coluna])
                limite = limite + 1
            posi = posi + 1
        pattern.append(arr)   


        linha = linha + 1
        
    print(pattern)

pattern()