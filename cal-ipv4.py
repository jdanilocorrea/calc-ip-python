# No cálculo ipv4 temos 4 octetos de 8 bits
# em que cada bit representa um valor na posição sequencial
# os respectivos valores são: 128 64 32 16 8 4 2 1
# Em observação o valor posterior é a metade do antecesso

# Aqui temos os intervalos de classes representativa
# O valor do primeiro octeto representa a classe

# "Classe A de 10.0.0.0 - 10.255.255.255"
# "Classe B 172.16.0.0 - 172.31.255.255"
# "Classe C 192.168.0.0 - 192.168.255.255"

from email.mime import base


ipv4 = input(r'digite um ip valido "com pontos": ')
# my_mask = input(r'digite uma maskara *"com pontos"*')

octet_ipv4 = ipv4.split('.')
tipo_classe = ''

#     =>  8    7   6   5  4  3  2  1
octet = [128, 64, 32, 16, 8, 4, 2, 1]

octet1 = int(octet_ipv4[0])
octet2 = int(octet_ipv4[1])
octet3 = int(octet_ipv4[2])
octet4 = int(octet_ipv4[3])
# --------------------------------------------------------------

# ---------------------------------------------------------------------------------------
if octet1 > 0 and octet1 < 128:
    if octet1 == 127:
        print('IP  Reservado para testes internos dispositivo loopback - "localhost"')

    else:
        tipo_classe = 'A'
        print('Classe A')
# ---------------------------------------------------------------------------------------
if octet1 > 127 and octet1 < 192:
    tipo_classe = 'B'
    print('Classe B')
# ---------------------------------------------------------------------------------------
if octet1 > 191 and octet1 < 224:
    tipo_classe = 'C'
    print('Classe C')
# ---------------------------------------------------------------------------------------
if octet1 > 223 and octet1 < 240:
    tipo_classe = 'D'
    print('Classe D')
# ---------------------------------------------------------------------------------------
if octet1 > 239 and octet1 < 256:
    tipo_classe = 'E'
    print('Classe E')

for v in range(4):
    for index in range(8):
        if index == 7:
            print(f'/{octet[index]}', end='  ||  ')

        else:
            print(f'/{octet[index]}', end='')

print('')

classe_oct = octet1
soma_bit = 0
bit = []
for index in range(8):
    if octet[index] <= classe_oct:
        res = classe_oct % octet[index]
        bit.append(1)
        soma_bit += octet[index]
        if res == octet[index]:
            break
        classe_oct = res
    else:
        bit.append(0)


# print(bit)
# print(soma_bit)


for index in range(8):
    if index == 7:
        print(f'/{bit[index]}', end='   ||  ')
    elif octet[index] < 16:
        print(f'/{bit[index]}', end='')
    else:
        print(f'/ {bit[index]}', end='')


# --------------------------------------------------
# append, insert, pop, del, clear, extend, +
