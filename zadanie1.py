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
        # Oblicz średnią dla każdego podciągu i dodaj do listy średnich
        average = np.mean(sub_sequence)
        avg.append(average)
    return avg


def draw_chart(avg, m, n):
    # Rysowanie histogramu
    count, bins, ignored = plt.hist(avg, bins='auto', density=True, color='blue', alpha=0.7)

    # Obliczanie średniej i odchylenia standardowego dla rysowanej próbki
    mu = np.mean(avg)
    sigma = np.std(avg)
    plt.axvline(mu, color='red', linewidth=1)
    # Tworzenie linii na podstawie rozkładu normalnego
    pdf = norm.pdf(bins, mu, sigma)
    plt.plot(bins, pdf, linewidth=1, color='red')
    if m == 1:
        plt.title(f'Histogram symulacji CTG dla {m} podciągu o długości {n}')
    else:
        plt.title(f'Histogram symulacji CTG dla {m} równych podciągów o długości {n}')
    plt.ylabel('Częstotliwość wystąpienia')
    plt.xlabel('Wartość średnia')

    # Rysowanie histogramu
    count, bins, ignored = plt.hist(avg, bins='auto', density=True, color='blue', alpha=0.7, edgecolor='black')

    # Rysowanie linii rozkładu normalnego
    mu = np.mean(avg)
    sigma = np.std(avg)
    pdf = norm.pdf(bins, mu, sigma)
    plt.plot(bins, pdf, linewidth=1, color='red')
    plt.show()


n_list = [1, 2, 5, 10]
total_random_var = 100000  # Łączna liczba wygenerowanych zmiennych losowych do testu
a = 0  # Dolna granica zakresu
b = 1  # Górna granica zakresu

# Generowanie całej puli zmiennych losowych
random_vars = random_uniform_distr_values(a, b, total_random_var)

# Dla każdej wartości 'n' z listy 'n_list' tworzymy histogramy
for n in n_list:
    # Dzielimy 'random_vars' na podciągi o długości 'n'
    sub_sequences = split_sequences(random_vars, n)
    # Obliczamy średnie dla każdego podciągu
    averages = calculate_avg(sub_sequences)
    # Tworzymy histogram dla obliczonych
    plt.figure(figsize=(10, 8))
    draw_chart(averages, m, n)
