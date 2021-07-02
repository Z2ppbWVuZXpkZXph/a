#MODULOS
import os, sys, time
from sympy.crypto.crypto import encipher_affine, decipher_affine
from sympy.crypto.crypto import encipher_shift, decipher_shift

#COLORES                                                                                                                                                
GL = "\033[96;1m" # Blue aqua
BB = "\033[34;1m" # Blue light
YY = "\033[33;1m" # Yellow light                                                                                                                        
GG = "\033[32;1m" # Green light
WW = "\033[0;1m"  # White light                                                                                                                         
RR = "\033[31;1m" # Red light
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33;1m"  # Yellow
G = "\033[32m"    # Green
W = "\033[0;1m"   # White
R = "\033[31m"    # Red
C = "\033[36;1m"  # Cyan
M = "\033[35;1m"  # Morado

#Funciones affine
def op():
        os.system("sleep 1")
        print (CC+"\n¿Que es lo que quieres hacer ahora mismo?")
        print (YY+"1) " + BB+"Cifrar\n" + YY +"2) " + BB+"Descifrar\n" + YY+"3) " + BB+"Salir\n")
        ca = int(input(GG+"\nEscoge una opcion: " + WW))
        if ca == 1:
                cipher()
        elif ca == 2:
                decipher()
        elif ca == 3:
                skip()

def decipher():
        print (RR+"\n             Descifrador de frases")
        ba = input(GG+"Escribe la frase para descifrar\n>>> " + WW)
        bb = int(input(GG+"Escribe la llave: " + WW))
        bk = (5,bb)
        bc = decipher_affine(ba, bk)
        print (RR+"\nPalabra descifrada!\n>>> " + WW, bc)
        op()

def cipher():
        print (RR+"\n             Cifrador de frases")
        aa = input(GG+"Escribe la frase\n>>> " + WW)
        ab = int(input(GG+"Escribe la llave: " + WW))
        ak = (5,ab)
        ac = encipher_affine(aa, ak)
        print (RR+"\nFrase cifrada!\n>>> " + WW, ac)
        op()

def sutil(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(12. / 150)
def skip():
        sutil(M+"\nSaliendo del programa... ")
        os.system("sleep 1;clear;figlet Valletta")

os.system("clear")
print (RR+"            CIPHER VTA")
print (CC+"\nQue es lo que deseas hacer?")
print (YY+"1) " + BB+"Cifrar\n" + YY +"2) " + BB+"Descifrar\n" + YY+"3) " + BB+"Salir\n")
rp = int(input(GG+"Escoje una opcion: " + WW))

if rp == 1:
        cipher()
elif rp == 2:
        decipher()
elif rp == 3:
        skip()
