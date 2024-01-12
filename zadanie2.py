import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
import math

matplotlib.use('TkAgg')

csv_data = pd.read_csv("6.csv", header=None)

data = []
for index, row in csv_data.iterrows():
    sublist = [row[0], row[1]]
    data.append(sublist)


population_1 = [i[0] for i in data]
population_2 = [i[1] for i in data]


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
        raise ValueError("Type must be 'l' for lower or 'h' for higher quartile")
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


print(set_rates(population_1))
print(set_rates(population_2))


def plot_histograms(pop1: list, pop2: list):
    plt.figure(figsize=(14, 7))

    # First histogram and normal distribution
    plt.subplot(1, 2, 1)
    count1, bins1, ignored1 = plt.hist(pop1, bins='auto', color='blue', alpha=0.7, rwidth=0.85, density=True)
    mu1, std1 = norm.fit(pop1)  # Fit a normal distribution to the data
    p1 = norm.pdf(bins1, mu1, std1)  # Probability density function for the normal distribution
    plt.plot(bins1, p1, 'r-', linewidth=2)
    plt.title('Histogram dla populacji 1')
    plt.xlabel('Wartości')
    plt.ylabel('Częstotliwość')

    # Second histogram and normal distribution
    plt.subplot(1, 2, 2)
    count2, bins2, ignored2 = plt.hist(pop2, bins='auto', color='green', alpha=0.7, rwidth=0.85, density=True)
    mu2, std2 = norm.fit(pop2)  # Fit a normal distribution to the data
    p2 = norm.pdf(bins2, mu2, std2)  # Probability density function for the normal distribution
    plt.plot(bins2, p2, 'r-', linewidth=2)
    plt.title('Histogram dla populacji 2')
    plt.xlabel('Wartości')
    plt.ylabel('Częstotliwość')

    plt.tight_layout()
    plt.show()

# plot_histograms(population_1, population_2)
