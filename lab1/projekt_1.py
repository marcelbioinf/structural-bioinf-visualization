from matplotlib import pyplot as plt

#easier - case-specific 
#combined_seq = ''
# with open("./RF00001.fasta.txt") as my_file:
#     for line in my_file:
#        if not line.startswith('>):
#           combined_seq+=line


#universal case
with open("./RF00001.fasta.txt") as my_file:
    sequences = my_file.read().split('>')
    sequences.pop(0)
    seqs = []
    for sequence in sequences:
        header, *content = sequence.splitlines()
        seq = ''.join(content)
        seqs.append(seq)

counts = list(map(''.join(seqs).count, "ACGU"))           #print(*(seq.count(nuc) for nuc in "ACGT")) 
counts_dict = {}
for i, key in enumerate("ACGU"):
    counts_dict[key] = counts[i]



## THIS IS BASIC ONE ##
# fig = plt.figure(figsize =(10, 7))
# plt.pie(counts_dict.values(), labels = counts_dict.keys(), explode=[0.03, 0.03, 0.03, 0.03], colors=['skyblue','steelblue','darkcyan', 'paleturquoise'], autopct='%1.1f%%')
# plt.title('Frequency of nucleotides across 5S ribosomal RNA family Rfam seed alignment')
# plt.show()

#more advanced
fig, ax = plt.subplots(figsize =(10, 7))
wedges, texts, autotexts = ax.pie(counts_dict.values(), 
autopct = '%1.1f%%',
explode = [0.03, 0.03, 0.03, 0.03], 
labels = counts_dict.keys(),
shadow = False,
colors = ['skyblue','steelblue','darkcyan', 'paleturquoise'],
startangle = 90,
wedgeprops  = { 'linewidth' : 1, 'edgecolor' : "grey" },
textprops = dict(color ="black"))
 
 
plt.setp(autotexts, size = 8, weight ="bold")
ax.set_title("Frequency of nucleotides across 5S ribosomal RNA family Rfam seed alignment")
 
plt.show()






