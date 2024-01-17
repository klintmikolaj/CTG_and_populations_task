import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

matplotlib.use('TkAgg')  # Wyświetlanie wykresów w osobnym oknie

m = 0
while m not in range(1, 100000):
    m = int(input("Podaj liczbę podciągów 'm': "))  # Na ile podciągów dzielimy cały ciąg zmiennych losowych


def random_uniform_distr_values(a, b, count):
    return np.random.uniform(a, b, count)


def split_sequences(seq, n):
    # Oblicz długość jednego podciągu
    sebseq_len = n
    subsec_list = []  # Pusta lista na podciągi

    for i in range(0, len(seq), sebseq_len):
        sub_sequence = seq[i:i + sebseq_len]
        subsec_list.append(sub_sequence)

    return subsec_list


def calculate_avg(subsec):
    avg = []  # Lista na średnie
    for sub_sequence in subsec:
        # Średnia dla każdego podciągu
        average = np.mean(sub_sequence)
        avg.append(average)
    return avg


def draw_chart(avg, m, n):

    elements, edges, ignored = plt.hist(avg, bins='auto', density=True, color='blue', alpha=0.7)
    # Obliczanie średniej i odchylenia standardowego
    exp_val = np.mean(avg)
    sigma = np.std(avg)
    plt.axvline(exp_val, color='red', linewidth=1)
    # Tworzenie wykresu rozkładu normalnego
    pdf = norm.pdf(edges, exp_val, sigma)
    plt.plot(edges, pdf, linewidth=1, color='red')
    if m == 1:
        plt.title(f'Histogram symulacji CTG dla {m} podciągu o długości {n}')
    else:
        plt.title(f'Histogram symulacji CTG dla {m} równych podciągów o długości {n}')
    plt.ylabel('Częstotliwość występowania')
    plt.xlabel('Wartość średnia')
    elements, edges, ignored = plt.hist(avg, bins='auto', density=True, color='blue', alpha=0.7, edgecolor='black')
    # Rysowanie linii rozkładu normalnego
    exp_val = np.mean(avg)
    sigma = np.std(avg)
    pdf = norm.pdf(edges, exp_val, sigma)
    plt.plot(edges, pdf, linewidth=1, color='red')
    plt.show()


n_list = [1, 2, 5, 10]
total_random_vars = 100000  # Łączna liczba wygenerowanych zmiennych losowych do testu
a = 0  # Dolna granica zakresu
b = 1  # Górna granica zakresu

# Generowanie całej puli zmiennych losowych
random_vars = random_uniform_distr_values(a, b, total_random_vars)

# Tworzenie 4 histogramów
for n in n_list:
    # Dzielimy 'random_vars' na podciągi o długości 'n'
    sub_sequences = split_sequences(random_vars, n)
    # Obliczamy średnie dla każdego podciągu
    averages = calculate_avg(sub_sequences)
    # Tworzymy histogram dla obliczonych
    plt.figure(figsize=(10, 8))
    draw_chart(averages, m, n)
