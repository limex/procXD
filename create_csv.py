import csv
import random

# Generate 20 pairs of random integers between 1 and 40
pairs = [(random.randint(1, 10), random.randint(1, 10)) for _ in range(25)]

# Write the pairs to a CSV file
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(pairs)
