##################################################################
#---------> WHILE

x = 1
while(x <= 5):
    print(x)
    x = x + 1

##################################################################
#---------> Exercico 01

inicial = int(input('Qual valor deseja iniciar a contagem?'))
final = int(input('Qual valor desejada encerrar a contagem?'))

x = inicial
while(x <= final):
    if(x % 2 == 0):
        print(x)
    x = x + 1

##################################################################
#---------> Exercico 02

soma = 0
cont = 1
while(cont <=5)
    x = float(input('Digite a {}ª nota: '.format(cont)))
    soma = soma + x #--> soma += x
    cont = cont + 1 #--> soma += 1
media = soma / 5
print('Média final: {}'.format(media))

##################################################################
#---------> Exercico 03

x = int(input('Digite um valor maior do que zero '))
while (x<=0):
    x = int(input('Digite um valor maior do que zero: '))
print('Voçê digitou {}. Encerrando o programa.....'.format(x))


##################################################################
#---------> Exercico 04

print('Digite uma mensagem que irei repetir para você!')
print('Para encerrar escreva "sair"')
while True:
    print(texto)
    if texto == 'sair':
        break
print('Encerrando o programa.....')

##################################################################
#---------> Exercico 05

while True:
    nome = input('Qual o seu nome? ')
    if(nome != 'Lenhadorzinho'):
        continue
    senha = input('Qual a sua senha? ')
    if (senha == 'uninter'):
        break
prit('Acesso concedido')

##################################################################
#---------> Exercico 06

nome = ''
while not nome:
    nome = input('Digite seu nome: ')
valor = int(input('Digite um valor diferente de zero.'))
if valor:
    print('Voce digitou um valor difrente de zero')
else:
    print('Voce digitou zero')

##################################################################
#---------> Exercico 08 COMMAND ----> FOR

for i in range(6):
    print(i)

##################################################################
#---------> Exercico 09 COMMAND ----> FOR

for i in range(1,6,1):
    print(i)

##################################################################
#---------> Exercico 10 COMMAND ----> FOR

for i in range(10,0,-2):
    print(i)

##################################################################
#---------> Exercico 11 COMMAND ----> FOR

soma = 0
qtd = 0
for i in range(1,101,1):
    if(i%2 == 0):
        soma += i
        qtd += 1
media = soma / qtd
print('A média dos pares de 1 até 100 é: {}'.format(media))

##################################################################
#---------> Exercico 12 COMMAND ----> FOR
#----> Usando WHILE
tabuada = 1
while tabuada <= 10:
    print('Tabuada do {}:'.format(tabuada))
    i = 1
    while i <= 10:
        print('{} x {} = {}'.format(tabuada, i, tabuada * i))
        i += 1
    tabuada += 1

#----> Usando FOR
for tabuada in range(1, 11, 1):
    print('Tabuada dp {}: '.format(tabuada))
    for i in range(1, 11, 1):
        print('{} X {} = {}'.format(tabuada, i, tabuada*i))

#----> Usando WHILE + FOR
tabuada = 1
while tabuada <= 10:
    print('tabuada do{}'.format(tabuada))
    for i in range(1, 11, 1):
        print('{} x {} = {}'.format(tabuada, i, tabuada * i))
    tabuada += 1