from collections import defaultdict

class Population:
    def __init__(self, value, year_from=None, year_to=None):
        self.value = value
        self.year_from = year_from
        self.year_to = year_to

def find_largest_population(peoples):
    changes = defaultdict(lambda:0)

    for birth, death in peoples:
        changes[birth] += 1
        changes[death+1] -= 1

    # sort years
    years = [y for y in changes.keys()]
    years.sort()

    population = Population(0)
    max_populations = []

    for y in years:
        if changes[y] == 0:
            continue

        if changes[y] < 0:
            population.year_to = y - 1
            if len(max_populations) == 0:
                max_populations.append(population)
            elif population.value == max_populations[-1].value:
                max_populations.append(population)
            elif population.value > max_populations[-1].value:
                max_populations = [population]

        value = population.value + changes[y]
        population = Population(value, y)

    return max_populations

peoples = [(1908, 1909), (1900, 2000), (1910, 1920), (1945, 1945)]
ps = find_largest_population(peoples)
print([(p.value, p.year_from, p.year_to) for p in ps])

# 
# changes = {
#     1908: 1,
#     1910: 0,
#     1900: 1,
#     2001: -1,
#     1921: -1,
#     1945: 1,
#     1946: -1,
# }
# 
# years = [1900, 1908, 1910, 1921, 1945, 1946, 2001]
# 
# population = Population(1, 1946, 2000)
# max_populations = [Population(2, 1908, 1920), Population(2, 1945, 1945)]
