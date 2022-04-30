
# print('----------------------------------------------------------------------------------------------------------')
        # octets_decs = [octet_dec, octet_dec, octet_dec, octet_dec]
        # print(f'octets:\n{octets_decs}')
        # print('----------------------------------------------------------------------------------------------------------')
        # print(f'bits:\n{list_octs}')
        # print('---------------------------------------------------------------------------------------------------------')
        # print(
        #     f'ip:{octets_ipv4[0]: ^22}||{octets_ipv4[1]: ^24}||{octets_ipv4[2]: ^24}||{octets_ipv4[3]: ^24}')
        # print('----------------------------------------------------------------------------------------------------------')

        # for v in range(4):
        #     for index in range(8):
        #         if index == 7:
        #            print(f'/{octet_dec[index]}', end='  ||  ')

        #         else:
        #             print(f'/{octet_dec[index]}', end='')

        # # print('')

        # for oct_ in list_octs:
        #     for bit in range(8):
        #         if bit == 7:
        #             print(f'/{oct_[bit]}', end='   ||  ')
        #         elif octet_dec[bit] < 16:
        #             print(f'/{oct_[bit]}', end='')
        #         else:
        #             print(f'/ {oct_[bit]}', end='')

        # # print('')

# print('----------------------------------------------------------------------------------------------------------')
# print('|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-||')
# print('----------------------------------------------------------------------------------------------------------')


# def calcmask(octets_masK):
#     bits_rede = 0
#     bits_maq = 0
#     list_octs_bits_mask = []
#     for oct_mk in octets_mask:
#         bits_mask = []
#         bit_dec = 256 - int(oct_mk)
#         for index in range(len(octet_dec)):
#             if int(oct_mk) == 255:
#                 bits_rede += 1
#                 bits_mask.append(1)
#             elif bit_dec <= octet_dec[index]:
#                 bits_rede += 1
#                 bits_mask.append(1)
#             else:
#                 bits_maq += 1
#                 bits_mask.append(0)
#         list_octs_bits_mask.append(bits_mask)

#     print(f'mascara: {octets_mask}')
#     print(f'bits de rede: {bits_rede}')
#     print(f'bits de máquina: {bits_maq}')
#     print('----------------------------------------------------------------------------------------------------------')

#     print(f'octetos de bits:\n{list_octs_bits_mask}')
#     print(
#         f'mask:{octets_mask[0]: ^20}||{octets_mask[1]: ^24}||{octets_mask[2]: ^24}||{octets_mask[3]: ^24}')
#     print('----------------------------------------------------------------------------------------------------------')

#     for v in range(4):
#         for index in range(8):
#             if index == 7:
#                 print(f'/{octet_dec[index]}', end='  ||  ')

#             else:
#                 print(f'/{octet_dec[index]}', end='')

#     print('')

#     for moct_ in list_octs_bits_mask:
#         for bit in range(8):
#             if bit == 7:
#                 print(f'/{moct_[bit]}', end='   ||  ')
#             elif octet_dec[bit] < 16:
#                 print(f'/{moct_[bit]}', end='')
#             else:
#                 print(f'/ {moct_[bit]}', end='')


# calcmask(octets_mask)





# print('----------------------------------------------------------------------------------------------------------')
# print('|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-||')
# print('----------------------------------------------------------------------------------------------------------')


# def intervalip(ipv4_, mask_):
#     ipv4_ = int(ipv4_)
#     mask_ = int(mask_)
# --------------------------------------------------
# append, insert, pop, del, clear, extend, +
