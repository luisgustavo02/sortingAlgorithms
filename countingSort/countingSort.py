def couting(vector):
    max = vector[0]
    for i in vector:
        if i > max:
            max = i

    count = [0] * (max + 1)

    for i in vector:
        for j in range(0, len(count)):
            if i == j:
                count[j] += 1

    for j in range(0, len(count) - 1):
        count[j+1] += count[j]

    newVector = [0] * len(vector)

    for i in range(len(vector) -1 , -1, -1):
        newVector[count[vector[i]] - 1] = vector[i]
        count[vector[i]] -= 1

    for i in range(len(vector)):
        vector[i] = newVector[i]

def info():
    print("Counting Sort é um Algoritmo de Ordenação\n\n"
          "Para o Tempo de Complexidade:\n"
          "Melhor Resultado: \u03A9(n + k)\n"
          "Resultado Médio: \u03F4(n + k)\n"
          "Pior Resultado: O(n + k)\n\n"
          "Sobre seu Espaço de Complexidade:\n"
          "Pior caso: O(k)")
    
