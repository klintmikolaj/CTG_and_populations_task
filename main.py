import matplotlib
import numpy as np
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

tab_n = [1, 2, 5, 10] # Liczba zmiennych losowych w jednym podciągu (długość podciągu)
m = 0

while m not in range(1, 1000000):
    m = int(input("Podaj liczbę podciągów z zakresu od 1 do 1000000:"))
def normal_distr_values(n, distribution_type='normal'):
    if distribution_type == 'normal':
        return np.random.randn(n)

def calculate_avg(values):
    total = sum(values)
    size = len(values)
    avg = total/size
    if avg != 0:
        return avg
    else:
        print("Błąd podczas liczenia średniej")

def chart(values, n, m):
    plt.figure(figsize=(10, 8))
    num, border, bars = plt.hist(values, bins='auto', rwidth=0.8, color='#5a9dfa')
    for i in range(len(border) - 1):
        if border[i] <= 0 < border[i + 1]:
            bars[i].set_fc('#006bff')
            break
    plt.xlabel('Wartość średnia')
    plt.ylabel('Częstotliwość')
    plt.title(f'Histogram średnich z {m} podciągów o długości {n}')
    plt.show()


for i in tab_n:
    values = []
    for j in range(m):
        sample = normal_distr_values(i)
        value = calculate_avg(sample)
        values.append(value)
    chart(values, i, m)