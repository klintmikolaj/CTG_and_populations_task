import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

matplotlib.use('TkAgg')  # Wyświetlanie wykresów w osobnym oknie

m = 0
while m not in range(11, 10000000):
    print("Ranges: m (11-10000000)")
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
    elements, edges, ignored = plt.hist(avg, bins='auto', density=True, color='blue', alpha=0.5)

    # Obliczanie średniej i odchylenia standardowego
    expected_val = np.mean(avg)
    sigma = np.std(avg)
    plt.axvline(expected_val, color='red', linewidth=1)

    # Tworzenie wykresu rozkładu normalnego
    density_func = norm.pdf(edges, expected_val, sigma)
    plt.plot(edges, density_func, linewidth=1, color='red')
    if m == 1:
        plt.title(f'Histogram symulacji CTG dla {m} podciągu o długości {n}')
    else:
        plt.title(f'Histogram symulacji CTG dla {m} równych podciągów o długości {n}')
    plt.ylabel('Częstotliwość występowania')
    plt.xlabel('Wartość średnia')
    elements, edges, ignored = plt.hist(avg, bins='auto', density=True, color='blue', alpha=0.5, edgecolor='black')

    # Rysowanie linii rozkładu normalnego
    expected_val = np.mean(avg)
    sigma = np.std(avg)
    density_func = norm.pdf(edges, expected_val, sigma)
    plt.plot(edges, density_func, linewidth=1, color='red')
    plt.show()


n_list = [1, 2, 5, 10]
a = 0  # Dolna granica zakresu
b = 1  # Górna granica zakresu

# Generowanie całej puli zmiennych losowych
random_vars = random_uniform_distr_values(a, b, m)

# Tworzenie 4 histogramów
for n in n_list:
    # Dzielimy 'random_vars' na podciągi o długości 'n'
    sub_sequences = split_sequences(random_vars, n)
    # Obliczamy średnie dla każdego podciągu
    averages = calculate_avg(sub_sequences)
    # Tworzymy histogram dla obliczonych
    plt.figure(figsize=(10, 8))
    draw_chart(averages, m, n)


"""
Wnioski:
Symulacja z wykorzystaniem rozkładu jednostajnego w zakresie 0-1, który spełnia założenia CTG
potwierdza CTG, które opisuje zjawisko zbliżania się rozkładu średnich z danego ciągu zmiennych
losowych dowolnego rozkładu (również spełniającego założenia CTG) do rozkładu normalnego.
Wraz ze wzrostem liczby n rozkład coraz bardziej zdaje się przypominać normalny, ponieważ
zwiększamy przez to dokładność średniej i zmniejszamy wariancję (rozproszenie wokół średniej)próbki
Wzrost liczby m również pozwala na coraz dokładniejsze zobrazowanie kształtu dzwonu z rozkładu
normalnego z racji wykorzystania coraz większej liczby próbek. 

"""
