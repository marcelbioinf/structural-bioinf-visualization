import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./3.5_dataset.txt', sep=',', header=0)

dna_list, rna_list = [], []
methods = ['X-ray', 'NMR', 'EM', 'Other']
for method in methods:
    dna_list.append(len(df[ (df['method'] == method) & (df['polyclass'] == 'DNA') ]))
    rna_list.append(len(df[ (df['method'] == method) & (df['polyclass'] == 'RNA') ]))

print(dna_list)
print(rna_list)

plt.bar(methods, dna_list, color='teal')
plt.bar(methods, rna_list, bottom=dna_list, color='coral')
plt.xlabel("Metoda")
plt.ylabel("Liczba struktór")
plt.legend(["DNA", "RNA"])
plt.title("Liczba rozwiązywanych strukrór DNA i RNA różnymi metodami")
plt.show()

