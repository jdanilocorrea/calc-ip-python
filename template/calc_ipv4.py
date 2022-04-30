# No cálculo ipv4 temos 4 octetos de 8 bits
# em que cada bit representa um valor na posição sequencial
# os respectivos valores são: 128 64 32 16 8 4 2 1
# Em observação o valor posterior é a metade do antecesso

# Aqui temos os intervalos de classes representativa
# O valor do primeiro octeto representa a classe

# "Classe A de 10.0.0.0 - 10.255.255.255"
# "Classe B 172.16.0.0 - 172.31.255.255"
# "Classe C 192.168.0.0 - 192.168.255.255"

octet_dec = [128, 64, 32, 16, 8, 4, 2, 1]
class_redes = ['Class A','Class B','Class C']

class CalculateIP:    
# ---------------------------------------------------------------------------------------
    @classmethod
    def classRede(cls,octet1):
        octet1 = int(octet1)
        if octet1 > 0 and octet1 < 128:
            if octet1 == 127:
                return 'loopback/localhost'
            else:
                return class_redes[0]
        # ---------------------------------------------------------------------------------------
        if octet1 > 127 and octet1 < 192:
            return class_redes[1]
        # ---------------------------------------------------------------------------------------
        if octet1 > 191 and octet1 < 224:
            return class_redes[2]
        # ---------------------------------------------------------------------------------------
        if octet1 > 223 and octet1 < 240:
            return 'Class D'
        # ---------------------------------------------------------------------------------------
        if octet1 > 239 and octet1 < 256:
            return 'Class E'

    
    

    @classmethod
    def ipConvertBits(cls, octets_ipv4):
        list_octs = []
        soma_bit = 0
        for oct in octets_ipv4:
            oct = int(oct)
            list_bits = []
            for index in range(8):
                if octet_dec[index] <= oct:
                    res = oct % octet_dec[index]
                    list_bits.append(1)
                    soma_bit += octet_dec[index]
                    if res == octet_dec[index]:
                        break
                    oct = res
                else:
                    list_bits.append(0)

            list_octs.append(list_bits)
        return list_octs
    
    @classmethod
    def maskConvertBits(cls, octets_mask):
        bits_rede = 0
        bits_maq = 0
        list_octs_bits_mask = []
        for oct_mk in octets_mask:
            bits_mask = []
            bit_dec = 256 - int(oct_mk)
            for index in range(len(octet_dec)):
                if int(oct_mk) == 255:
                    bits_rede += 1
                    bits_mask.append(1)
                elif bit_dec <= octet_dec[index]:
                    bits_rede += 1
                    bits_mask.append(1)
                else:
                    bits_maq += 1
                    bits_mask.append(0)
            list_octs_bits_mask.append(bits_mask)
        return list_octs_bits_mask    
    
    @classmethod
    def totalBitsHost(cls, octs_bits_mask):
        host_bits = [ bit for oct in octs_bits_mask for bit in oct if bit == 0 ]
        totalbitshost = len(host_bits)
        return totalbitshost

    @classmethod
    def totalBitsRede(cls, octs_bits_mask):
        host_bits = [ bit for oct in octs_bits_mask for bit in oct if bit == 1 ]
        totalbitshost = len(host_bits)
        return totalbitshost 

    #Numero de hosts por redes
    @classmethod
    def totalHostRede(cls,list_octs_bits_mask,cl_rede):
        for index in range(len(class_redes)):
            if cl_rede == class_redes[index]:
                index_oct = index+1
                oct_bits_host = [bit for pos, oct in enumerate(list_octs_bits_mask) for bit in oct if pos >=  index_oct ]
                bit_host = [bit for bit in oct_bits_host if bit == 0]
                num_host = 2 ** len(bit_host) 
                return num_host

    #Numero de rede de grupos hosts
    @classmethod
    def totalRede(cls,list_octs_bits_mask,cl_rede):      
        for index in range(len(class_redes)):
            if cl_rede == class_redes[index]:
                index_oct = index+1
                oct_bits_host = [bit for pos, oct in enumerate(list_octs_bits_mask) for bit in oct if pos >=  index_oct ]
                bit_rede = [bit for bit in oct_bits_host if bit == 1]
                num_rede = 2 ** len(bit_rede) 
                return num_rede               




# testes
# cl_rede = 'Class C'
# mask = [255,255,255,0]
# conv_bits_mask = CalculateIP.maskConvertBits(mask)
# print(conv_bits_mask)

# CalculateIP.totalHostRede(conv_bits_mask, cl_rede)
# CalculateIP.totalRede(conv_bits_mask, cl_rede)