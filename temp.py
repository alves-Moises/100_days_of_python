max_digt = 6
valores = list()
valores_final = list()
for i in range(6000):
    str_i = str(i) 
    valido = True

    for j in str_i:
        if   int(j) > max_digt:
            valido = False


    if valido:
        valores.append(str_i)


for valor in valores:
    soma = 0    

    for i in valor:

        soma += int(i)
    if soma == 21:
        print(soma)
        valores_final.append(valor)
        


for i in valores_final:
    print(i)
