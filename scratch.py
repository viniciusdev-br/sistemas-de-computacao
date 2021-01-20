memoria = []; endereço = []
for i in range(0,16):
    endereço.append('{0:04b}'.format(i))
for i in range(0, len(endereço)):
    memoria.append("00000000")
print(*memoria)
print(*endereço)
entrada = input("Digite W para escrever, R para ler, L para listar toda a memória: ")
while entrada == 'W' or entrada == 'R' or entrada == 'L':
    if entrada == 'W':
        posiçao = input("Digite o endereço de 4 bits: ")
        novoValor = input('Digite o valor de 8 bits: ')
        for i in range(0, len(endereço)):
            if endereço[i] == posiçao:
                posiçao = i
                break
        for i in range(0, len(memoria)):
            if i == posiçao:
                memoria[i] = novoValor
                break
    elif entrada == 'L':
        print(*memoria)
    elif entrada == 'R':
        posiçao = input('Digite o endereço de 4 bits: ')
        for i in range(0, len(endereço)):
            if endereço[i] == posiçao:
                posiçao = i
                break
        for i in range(0, len(memoria)):
            if i == posiçao:
                print('Valor encontrado {}'.format(memoria[i]))
    entrada = input("Digite W para escrever, R para ler, L para listar toda a memória: ")

