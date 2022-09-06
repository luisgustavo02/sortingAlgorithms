def bubble(vector):
    for i in range(0, len(vector)):
        for j in range(0, len(vector)):
            if i != j and vector[i] > vector[j]:
                aux = vector[i]
                vector[i] = vector[j]
                vector[j] = aux
    return vector

def info():
    print("Bubble Sort é um Algoritmo de Ordenação\n\n"
          "Para o Tempo de Complexidade:\n"
          "Melhor Resultado: \u03A9(n)\n"
          "Resultado Médio: \u03F4(n²)\n"
          "Pior Resultado: O(n²)\n\n"
          "Sobre seu Espaço de Complexidade:\n"
          "Pior caso: O(1)")
