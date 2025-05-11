from math import factorial

n = 7

total_permutations = 1

for i in range(n):
    total_permutations *= (2 * (n - i))  # Multiplique por 2 para considerar os sinais

print("O número de permutações de comprimento 7 é:", total_permutations)
