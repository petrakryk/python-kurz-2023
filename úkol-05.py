import statistics

teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

prumer = [statistics.mean(den) for den in teploty]
rano = [den[0] for den in teploty]
noc = [den[-1] for den in teploty]
poledne_a_noc = [[den[1], den[-1]] for den in teploty]

print(prumer)
print(rano)
print(noc)
print(poledne_a_noc)