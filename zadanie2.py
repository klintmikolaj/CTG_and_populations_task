import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind
from scipy.stats import ttest_1samp
from scipy.stats import norm
import math
import json

matplotlib.use('TkAgg')

csv_data = pd.read_csv("6.csv", header=None)

data = []
for index, row in csv_data.iterrows():
    sublist = [row[0], row[1]]
    data.append(sublist)

# Podpunkt 1
population_1 = [i[0] for i in data]
population_2 = [i[1] for i in data]


# Podpunkt 2
def plot_histograms(pop1: list, pop2: list):
    plt.figure(figsize=(14, 7))

    # Pierwszy histogram
    plt.subplot(1, 2, 1)
    count1, bins1, ignored1 = plt.hist(pop1, bins='auto', color='blue', alpha=0.7, rwidth=0.85, density=True)
    mu1, std1 = norm.fit(pop1)
    p1 = norm.pdf(bins1, mu1, std1)
    plt.plot(bins1, p1, 'r-', linewidth=2)
    plt.axvline(mu1, color='red', linewidth=2)
    plt.title('Histogram populacji 1')
    plt.xlabel('Wartości średnie')
    plt.ylabel('Częstotliwość występowania')

    # Drugi histogram
    plt.subplot(1, 2, 2)
    count2, bins2, ignored2 = plt.hist(pop2, bins='auto', color='black', alpha=0.7, rwidth=0.85, density=True)
    mu2, std2 = norm.fit(pop2)
    p2 = norm.pdf(bins2, mu2, std2)
    plt.axvline(mu2, color='red', linewidth=2)
    plt.plot(bins2, p2, 'r-', linewidth=2)
    plt.title('Histogram populacji 2')
    plt.xlabel('Wartości średnie')
    plt.ylabel('Częstotliwość występowania')
    plt.tight_layout()
    plt.show()


# Podpunkt 3
def calculate_avg(pop: list):
    return sum(pop) / len(pop)


def calculate_median(pop: list):
    pop.sort()
    if len(pop) % 2 == 0:
        median = (pop[int(len(pop) / 2) - 1] + pop[int(len(pop) / 2)]) / 2
    else:
        median = pop[int(len(pop) / 2)]
    return median


def find_mode(pop: list):
    max_count = max(set(pop), key=pop.count)
    if max_count != max(pop) and max_count != min(pop):
        return max_count
    else:
        print("Unable to find the mode!")


def find_sample_range(pop: list):
    return max(pop) - min(pop)


def calculate_variance(pop: list):
    if len(pop) == 0:
        return 0
    avg = sum(pop) / len(pop)
    sum_of_squares = sum((x - avg) ** 2 for x in pop)
    variance = sum_of_squares / len(pop)
    return variance


def calculate_standard_deviation(variance: float):
    return math.sqrt(variance)


def find_quartile(pop: list, quartile_type: str):
    if not pop:
        return None
    sorted_pop = sorted(pop)
    n = len(sorted_pop)
    if quartile_type == "l":
        quartile_index = (n - 1) * 0.25
    elif quartile_type == "h":
        quartile_index = (n - 1) * 0.75
    else:
        raise ValueError("Typ musi wynosić 'l' dla dolnego kwartyla i 'h' dla górnego")
    lower_index = int(quartile_index)
    upper_index = lower_index + 1
    weight = quartile_index - lower_index
    if upper_index < n:
        return sorted_pop[lower_index] * (1 - weight) + sorted_pop[upper_index] * weight
    else:
        return sorted_pop[lower_index]


def set_rates(pop: list):
    answer_dict = {"average": calculate_avg(pop),
                   "median": calculate_median(pop),
                   "mod": find_mode(pop),
                   "sample range": find_sample_range(pop),
                   "variance": calculate_variance(pop),
                   "standard deviation": calculate_standard_deviation(calculate_variance(pop)),
                   "lower quartile": find_quartile(pop, "l"),
                   "higher quartile": find_quartile(pop, "h"),
                   "inter quartile range": find_quartile(pop, "h") - find_quartile(pop, "l")}
    return answer_dict


# Podpunkt 4

def pop_difference_test():
    # alfa = 0.05
    # Test t dla dwóch niezależnych próbek
    t_stat, p_val = ttest_ind(population_1, population_2)
    print(f"Wartość statystyki T: {t_stat}, P-wartość: {p_val}")

    if p_val < 0.05:
        print("Odrzucamy hipotezę zerową")
    else:
        print("Przyjmujemy hipotezę zerową")


def pop_equals_value_test(x):
    # alfa = 0.05
    # Test dla populacji 1
    t_stat_pop1, p_val_pop1 = ttest_1samp(population_1, x)

    # Test dla populacji 2
    t_stat_pop2, p_val_pop2 = ttest_1samp(population_2, x)
    print(f"Populacja 1: Wartość statystyki T: {t_stat_pop1}, P-wartość: {p_val_pop1}")
    if p_val_pop1 < 0.05:
        print("Odrzucamy hipotezę zerową")
    else:
        print("Przyjmujemy hipotezę zerową")
    print(f"\nPopulacja 2: Wartość statystyki T: {t_stat_pop2}, P-wartość: {p_val_pop2}")
    if p_val_pop2 < 0.05:
        print("Odrzucamy hipotezę zerową")
    else:
        print("Przyjmujemy hipotezę zerową")


def print_answers():
    RED = '\033[31m'
    RESET = '\033[0m'
    plot_histograms(population_1, population_2)
    print(f"\n{RED}----- Rates population 1 -----{RESET}")
    print(f"{json.dumps(set_rates(population_1), indent=4)}")
    print(f"\n{RED}----- Rates population 2 -----{RESET}")
    print(f"{json.dumps(set_rates(population_2), indent=4)}")
    last_index_number_digit = 6
    print(f"\n{RED}------ Test H0: μ1 = 6 / Test H0: μ2 = 6 -----{RESET}")
    pop_equals_value_test(last_index_number_digit)
    print(f"\n{RED}------ Test H0: μ1 - μ2 = 0 -----{RESET}")
    pop_difference_test()

print_answers()
