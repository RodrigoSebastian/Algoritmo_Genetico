# Program done by: RSDLA & ISH
# Date: 26/05/2022
# Version: 1.0
# Description: Genetic Algorithm
# References: Class presentation by Prof. MLBC

from cmath import sin
import random

# Configuración
longitud_cromosoma = 4
prob_ceros = 0.5
prob_cruzamiento = 0.7
prob_mutacion = 0.3
indexX = 0
indexY = 1
vueltas = 0
limite_vueltas = 300
x = 0

conjunto = []

individuo1 = []
individuo2 = []

def funcion_aptitud(x):
    return abs((x-5)/(2+sin(x)))

def generar_individuo(individuo):
    individuo_final = []
    for x in individuo:
        if x <= prob_ceros:
            individuo_final.append(0)
        else:
            individuo_final.append(1)

    return individuo_final

def generar_conjunto(_conjunto, tam_poblacion):
    for x in range(0, tam_poblacion):
        individuo = []
        for i in range(longitud_cromosoma * 2):
            individuo.append(round(random.uniform(0, 1), 2))

        _conjunto.append(individuo)

def incrementar_index():
    global indexX
    global indexY
    global conjunto

    indexX = indexX + 1
    if(indexX > 7):
        indexX = 0
        indexY = indexY + 1
        if(indexY > (len(conjunto)-1)):
            conjunto.clear()
            generar_conjunto(conjunto, 4)
            print("\nNuevo conjunto generado")
            for x in conjunto:
                print(x)

            print("\n")
            indexY = 0

def calcular_probabilidad_cruzamiento(individuo1, individuo2):
    if(individuo1 == 0 and individuo2 == 0):
        return 0
    return individuo1 / (individuo1 + individuo2)

print("Generando conjunto de individuos...")
generar_conjunto(conjunto,4)
for x in conjunto:
    print(x)

print("\nSeparando individuos...")
individuo1 = conjunto[0][0:longitud_cromosoma]
individuo2 = conjunto[0][longitud_cromosoma:]

print("Individuo 1: ", individuo1)
print("Individuo 2: ", individuo2)

print("\nPasando individuos a binario...")
individuo1 = generar_individuo(individuo1)
individuo2 = generar_individuo(individuo2)

while x != 11:
    print("\nVuelta: ", vueltas + 1, " =========================================")
    print("Individuo 1: ", individuo1, " = ", int(
        ''.join(str(e) for e in individuo1), 2))
    print("Individuo 2: ", individuo2, " = ", int(
        ''.join(str(e) for e in individuo2), 2))
    print("\nCalculando aptitud de individuos...")
    aptitud1 = round(funcion_aptitud(int(''.join(str(e)
                                                 for e in individuo1), 2)), 4)
    aptitud2 = round(funcion_aptitud(int(''.join(str(e)
                                                 for e in individuo2), 2)), 4)
    print("Aptitud 1: ", aptitud1)
    print("Aptitud 2: ", aptitud2)

    if (aptitud1 > aptitud2):
        x = int(''.join(str(e) for e in individuo1), 2)
        print("\nIndividuo 1 es el mejor, x :", x)
    else:
        x = int(''.join(str(e) for e in individuo2), 2)
        print("\nIndividuo 2 es el mejor, x :", x)

    if(x == 11):
        print("\nValor encontrado en la vuelta: ", vueltas + 1)
        break

    print("\nCalculando probabilidad de cruzamiento...")
    prob_cruzamiento_1 = round(
        calcular_probabilidad_cruzamiento(aptitud1, aptitud2), 2)
    prob_cruzamiento_2 = round(
        calcular_probabilidad_cruzamiento(aptitud2, aptitud1), 2)
    print("Probabilidad de cruzamiento 1: ", prob_cruzamiento_1)
    print("Probabilidad de cruzamiento 2: ", prob_cruzamiento_2)

    print("\nVerificando cruzamiento...")
    prob_1 = conjunto[indexY][indexX]
    incrementar_index()
    prob_2 = conjunto[indexY][indexX]
    incrementar_index()
    prob_gen = conjunto[indexY][indexX]
    incrementar_index()
    zona_corte = conjunto[indexY][indexX]
    incrementar_index()
    print("Probabilidad 1: ", prob_1)
    print("Probabilidad 2: ", prob_2)
    print("Probabilidad gen: ", prob_gen)

    if zona_corte >= 0 and zona_corte <= 1/3:
        zona_corte = 1
    elif zona_corte > 1/3 and zona_corte <= 2/3:
        zona_corte = 2
    elif zona_corte > 2/3 and zona_corte <= 1:
        zona_corte = 3

    print("Zona de corte: ", zona_corte)

    copia1 = individuo1.copy()
    copia2 = individuo2.copy()

    if(prob_1 <= prob_cruzamiento):
        print("\nEsta generación es apta para cruzamiento...")
        if(prob_1 >= 0 and prob_1 <= prob_cruzamiento_1):
            print("\tIndividuo 1 es apto para cruzar...")
            print("\t\tCruzando...")
            print("\t\tIndividuo 1: ", individuo1, " = ",
                  int(''.join(str(e) for e in individuo1), 2))
            print("\t\tIndividuo 2: ", copia2, " = ",
                int(''.join(str(e) for e in copia2), 2))
            print("\t\t========================================")
            individuo1[zona_corte:] = copia2[zona_corte:]
            print("\t\tNuevo individuo 1: ", individuo1, " = ",
                  int(''.join(str(e) for e in individuo1), 2))

        if(prob_2 <= 1 and prob_2 >= prob_cruzamiento_2):
            print("\n\tIndividuo 2 es apto para cruzar...")
            print("\t\tCruzando...")
            print("\t\tIndividuo 2: ", individuo2, " = ",
                  int(''.join(str(e) for e in individuo2), 2))
            print("\t\tIndividuo 1: ", copia1, " = ",
                  int(''.join(str(e) for e in copia1), 2))
            print("\t\t========================================")
            individuo2[zona_corte:] = copia1[zona_corte:]
            print("\t\tNuevo individuo 2: ", individuo2, " = ",
                  int(''.join(str(e) for e in individuo2), 2))
    else:
        print("Esta generación no es apta para cruzamiento...")

    print("\nVerificando mutación...")

    prob_muta_1 = []

    for i in range(indexX, indexX + longitud_cromosoma):
        prob_muta_1.append(conjunto[indexY][indexX])
        incrementar_index()

    prob_muta_2 = []
    for i in range(indexX, indexX + longitud_cromosoma):
        prob_muta_2.append(conjunto[indexY][indexX])
        incrementar_index()

    print("Probabilidad mutación 1: ", prob_muta_1)
    print("Probabilidad mutación 2: ", prob_muta_2)
    print("\tMutando...")
    print("\t   Individuo 1   : ", individuo1, " = ",
          int(''.join(str(e) for e in individuo1), 2))
    for i, c in enumerate(prob_muta_1):
        if(c <= prob_mutacion):
            if(individuo1[i] == 0):
                individuo1[i] = 1
            else:
                individuo1[i] = 0
    print("\tNuevo individuo 1: ", individuo1, " = ",
          int(''.join(str(e) for e in individuo1), 2))
    print("\t========================================")
    print("\t   Individuo 2   : ", individuo2, " = ",
          int(''.join(str(e) for e in individuo2), 2))

    for i, c in enumerate(prob_muta_2):
        if(c <= prob_mutacion):
            if(individuo2[i] == 0):
                individuo2[i] = 1
            else:
                individuo2[i] = 0

    print("\tNuevo individuo 2: ", individuo2, " = ",
          int(''.join(str(e) for e in individuo2), 2))
    print("\t========================================")

    vueltas = vueltas + 1
    if(vueltas == limite_vueltas):
        print("\nLímite de vueltas alcanzado...")
        break