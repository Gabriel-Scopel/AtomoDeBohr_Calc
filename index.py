from math import *


he = 4.136e-15
hj = 6.626e-34
c = 3e8


def P_a():
    n = int(input("Digite o valor de n: "))
    r = n**2*5.29e-11
    v = 2.187e6/n
    K = 13.6/n**2
    U = -27.2/n**2
    E = -13.6/n**2
    lamb = (hj/(9.11e-31*v))

    print(f"Raio: {r:.3e} m")
    print(f"Velocidade: {v:.3e} m/s")
    print(f"Comprimento de onda de De Broglle: {lamb:.3e} m")
    print(f"Energia cinetica: {K:.3f} eV")
    print(f"Energia potencial: {U:.3f} eV")
    print(f"Energia total: {E:.3f} eV")



def Foton():
    ni = int (input("Digite o valor de n inicial: "))
    nf = int (input("Digite o valor de n final: "))
    #n = sqrt((ni-nf)**2)
    Ei = -13.6/ni**2
    Ef = -13.6/nf**2
    if (nf < ni):
        Eemis = Ei - Ef
        lambE = he*c/Eemis
        freqE = Eemis/he
        print(f"Energia emissao foton: {Eemis:.3f} eV")
        print(f"Comprimento de onda emissao do foton: {lambE:.3e} m")
        print(f"Frequencia emissao do foton: {freqE:.3e} H/z" )
    elif (nf > ni): 
        Eabs = Ef - Ei
        lambA = he*c/Eabs
        freqA = Eabs/he
        print(f"Energia absorvida foton: {Eabs:.3f} eV")
        print(f"Comprimento de onda absorvida do foton: {lambA:.3e} m ")
        print(f"Frequencia absorvida do foton: {freqA:.3e} H/z" )
    
def absorcaof():
    ni = int (input("Digite o valor de n inicial: "))
    count = input("Digite F receber o valor com frequência ou L para receber com lambda\n")
    if count == "F":
        freq = float (input("Digite o valor da frequencia: "))
        Effreq = he*freq
        Ei = -13.6/ni**2
        Ef = Ei + Effreq
    elif count == "L":    
        lamb = float (input("Digite o valor de lambda: "))
        Eflamb = he*c/lamb
        Ei = -13.6/ni**2
        Ef = Ei + Eflamb
    else: 
        print("Você digitou um comando inválido.")
    nf = (-13.6/Ef)**0.5
    if (nf-0.1<nf<nf+0.1):
        nf = round(nf)
        print(f"nivel final é: {nf} ")
    else:
        print("deu ruim")
        

def absorcaoi():
    nf = int (input("Digite o valor de n final: "))
    count = input("Digite F receber o valor com frequência ou L para receber com lambda\n")
    if count == "F":
        freq = float (input("Digite o valor da frequencia: ")) 
        Effreq = he*freq
        Ef = -13.6/nf**2
        Ei = Ef - Effreq
    elif count == "L":
        lamb = float (input("Digite o valor de lambda: "))
        Eflamb = he*c/lamb
        Ef = -13.6/nf**2
        Ei = Ef - Eflamb
    else:
        print("Você digitou um comando inválido.")
    ni = (-13.6/Ei)**0.5  # ei = ef - effreq
    if (ni-0.1<ni<ni+0.1):
        ni = round(ni)
        print(f"nivel inicial é: {ni} ")
    else:
        print("deu ruim")


def emissaof():
    ni = int (input("Digite o valor de n inicial: "))
    count = input("Digite F receber o valor com frequência ou L para receber com lambda\n")
    if count == "F":
        freq = float (input("Digite o valor da frequencia: "))
        Effreq = he*freq
        Ei = -13.6/ni**2
        Ef = Ei - Effreq
    elif count == "L":    
        lamb = float (input("Digite o valor de lambda: "))
        Eflamb = he*c/lamb
        Ei = -13.6/ni**2
        Ef = Ei - Eflamb
    else: 
        print("Você digitou um comando inválido.")
    nf = (-13.6/Ef)**0.5
    if (nf-0.1<nf<nf+0.1):
        nf = round(nf)
        print(f"nivel final é: {nf} ")
    else:
        print("deu ruim")



def emissaoi():
    nf = int (input("Digite o valor de n final: "))
    count = input("Digite F receber o valor com frequência ou L para receber com lambda\n")
    if count == "F":
        freq = float (input("Digite o valor da frequencia: "))
        Effreq = he*freq
        Ef = -13.6/nf**2
        Ei = Ef + Effreq
    elif count == "L":    
        lamb = float (input("Digite o valor de lambda: "))
        Eflamb = he*c/lamb
        Ef = -13.6/nf**2
        Ei = Ef + Eflamb
    else: 
        print("Você digitou um comando inválido.")
    ni = (-13.6/Ei)**0.5
    if (ni-0.1<ni<ni+0.1):
        ni = round(ni)
        print(f"nivel final é: {ni} ")
    else:
        print("deu ruim")



def main():
    print("Autores do código:")
    print("Gabriel de Souza Scopel")
    print("Matheus Arcanjo")
    print("Kayque da Silva Fernandes")
    print("Murilo Carvalho Povoa da Silva")
    print()
    print("Este programa tem por finalidade realizar cálculos envolvendo modelo de Bohr para o átomo de hidrogênio e quantização.")
    print("Nele é possível calcular número quântico, Energia do fóton absorvido/emitido, frequência do fóton absorvido/emitido, comprimento de onda do fóton absorvido/emitido, raio da órbita, velocidade, energia cinética, energia potencial, energia total e comprimento de onda do elétron. \n")
    print("Todas as unidades de medida devem ser inseridas no sistemas internacional\n")
    print("O que voce deseja calcular?")
    print("Entrada pelo teclado:")
    print("1 - Propriedades do átomo de H")
    print("2 - Emissão/absorção de fóton com saída em Ef, Ff, lambidaf")
    print("3 - Absorção de fóton com saída em Nf")
    print("4 - Absorção de fóton com saída em Ni ")
    print("5 - Emissão de fóton com saída em Nf ")
    print("6 - Emissão de fóton com saída em Ni ")
    print("Entrada: ")
    print()
    count = input('qual formula? ')
    
    if count == '1':
        P_a()
    elif count == '2':
        Foton() 
    elif count == '3':
        absorcaof()
    elif count == '4':
        absorcaoi()
    elif count == '5':
        emissaof()
    elif count == '6':
        emissaoi()
    else:
        print("Você digitou um comando inválido.")

main()