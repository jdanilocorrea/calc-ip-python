# No cálculo ipv4 temos 4 octetos de 8 bits
# em que cada bit representa um valor na posição sequencial
# os respectivos valores são: 128 64 32 16 8 4 2 1
# Em observação o valor posterior é a metade do antecesso


# Aqui temos os intervalos de classes representativa
# O valor do primeiro octeto representa a classe


from turtle import clear


classA = "Classe A de 10.0.0.0 - 10.255.255.255"
classB = "Classe B 172.16.0.0 - 172.31.255.255"
classC = "Classe C 192.168.0.0 - 192.168.255.255"

#         8    7   6   5  4  3  2  1
octet = [128, 64, 32, 16, 8, 4, 2, 1]

for v in range(4):
    for index in range(8):
        if index == 7:
            print(f'/{octet[index]}', end='  ||  ')

        else:
            print(f'/{octet[index]}', end='')

print('')

for v in range(4):
    for index in range(8):
        if index == 7:
            print(f'/{0}', end='   ||  ')
        elif octet[index] < 16:
            print(f'/{0}', end='')
        else:
            print(f'/ {0}', end='')


# my_ipv4 = input(r'digite um ip valido *"com pontos"*')
# my_mask = input(r'digite uma maskara *"com pontos"*')
