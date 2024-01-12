
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.stats import norm
matplotlib.use('TkAgg') # Wyświetlanie wykresów w osobnym oknie

substrings = 0 # Liczba podciągów
tab_n = [1, 2, 5, 10]  # Liczba zmiennych losowych w jednym podciągu (długość podciągu)
while substrings not in range(1, 1000000):
    substrings = int(input("Podaj liczbę podciągów z zakresu od 1 do 1000000: "))
def get_normal_dist_values(n):
    return np.random.randn(n)

def calculate_avg(data):
    total = sum(data)
    size = len(data)
    avg = total / size
    if avg != 0:
        return avg
    else:
        print("Błąd podczas liczenia średniej")

def draw_chart(data, n, m):
    plt.figure(figsize=(10, 8))
    num, border, bars = plt.hist(data, bins='auto', rwidth=0.8, color='#5a9dfa')

    # Wartość oczekiwana
    for i in range(len(border) - 1):
        if border[i] <= 0 < border[i + 1]:
            bars[i].set_fc('#006bff')
            break

    mean = np.mean(data)
    std = np.std(data, ddof=1)
    x = np.linspace(min(data), max(data), 100)
    y = norm.pdf(x, mean, std) * m * np.diff(border[:2])[0]
    plt.plot(x, y, 'r', linewidth=2)

    plt.xlabel('Wartość średnia')
    plt.ylabel('Częstotliwość występowania')
    plt.title(f'Histogram symulacji CTG z {m} podciągów o długości {n}')
    plt.grid(color='grey', linestyle='-', linewidth=0.25)
    plt.show()

for n in tab_n:
    values = [calculate_avg(get_normal_dist_values(n)) for _ in range(substrings)]
    draw_chart(values, n, substrings)