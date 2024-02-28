import sys
import math
from Bio.PDB.PDBParser import PDBParser
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def get_euclid_dist(a,b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2 + (a[2] - b[2])**2)


parser = PDBParser(QUIET=True)

# if len(sys.argv) < 3:
#     raise Exception('No files given as parameters. Please add file paths to command line')

# file_path_1 = sys.argv[1]
# file_path_2 = sys.argv[2]

s1 = parser.get_structure("s1", './1_bujnicki_1_rpr.pdb')[0]
s2 = parser.get_structure("s1", './1_das_4_rpr.pdb')[0]

if len(list(s1.get_residues())) != len(list(s2.get_residues())):
    raise Exception('Structures diifer in length')

def get_atoms_c(structure, at):
    atoms = []
    for atom in structure.get_atoms():
        if atom.id == at:
            atoms.append(atom.get_coord())
    return np.array(atoms)

s1_atoms = get_atoms_c(s1, "C4'")
s2_atoms = get_atoms_c(s2, "C4'")


###DŁUGA METODA - bambikowo
# ds1 = {}
# for i in range(len(s1_atoms)):
#     ds1[i] = []
#     for j in range(len(s1_atoms)):
#         ds1[i].append(get_euclid_dist(s1_atoms[i], s1_atoms[j]))
#moglbym też stworzyc pustego df: df = pd.DataFrame(index=range(numRows),columns=range(numCols)) i wypełniac w tej petli pokoli komorki 

s1_distances = [[get_euclid_dist(s1_atoms[i],s1_atoms[j]) for i in range(len(s1_atoms))] for j in range(len(s1_atoms))]
#s1_distances = {index: list for index,list in enumerate(s1_distances)}
s1_distances= dict(zip(range(len(s1_distances)), s1_distances))
df_s1 = pd.DataFrame(s1_distances)

s2_distances = [[get_euclid_dist(s2_atoms[i],s2_atoms[j]) for i in range(len(s2_atoms))] for j in range(len(s2_atoms))]
s2_distances= dict(zip(range(len(s2_distances)), s2_distances))
df_s2 = pd.DataFrame(s2_distances)

sns.heatmap(df_s1, cmap='Greens')
plt.xlabel('Nucleotide')
plt.title("Distance between C4' atoms of adjacent nucelotides")
plt.ylabel("Nucleotide")
plt.show()

sns.heatmap(df_s2, fmt="g", cmap='Blues')
plt.xlabel('Nucleotide')
plt.title("Distance between C4' atoms of adjacent nucelotides")
plt.ylabel("Nucleotide")
plt.show()

df_3 = df_s1 - df_s2

sns.heatmap(df_3, fmt="g")
plt.xlabel('Nucleotide')
plt.title("Distance between C4' atoms of adjacent nucelotides")
plt.ylabel("Nucleotide")
plt.show()






#THIS ONLY GIVES YOU DISTANCES FOR 1,2;2,3;3,4 nucleotides etc.
# s1_distances = [get_euclid_dist(i,j) for i,j in zip(s1_atoms, s1_atoms[1:])]
# s2_distances = [get_euclid_dist(i,j) for i,j in zip(s2_atoms, s2_atoms[1:])]

# df = pd.DataFrame(list(zip(s1_distances,s2_distances)), columns=['s1', 's2'])
# df_s1 = df.drop(columns=['s2'])
# df_s2 = df.drop(columns=['s1'])



################## wrong version ######################

# def get_atoms_c(structure, at):
#     atoms = []
#     for chain in structure:
#         tmp = []
#         for atom in chain.get_atoms():
#             if atom.id == at:
#                 tmp.append(atom.get_coord())
#         atoms.append(tmp)
#     return np.array(atoms)

#s1_atoms = get_atoms_c(s1, "C4'")
#s1_atoms[1] = s1_atoms[1][::-1]

# s2_atoms = get_atoms_c(s2, "C4'")
# s2_atoms[1] = s2_atoms[1][::-1]

# s1_distances = [get_euclid_dist(i,j) for i,j in zip(s1_atoms[0], s1_atoms[1])]
# s2_distances = [get_euclid_dist(i,j) for i,j in zip(s2_atoms[0], s2_atoms[1])]

# df = pd.DataFrame(list(zip(s1_distances,s2_distances)), columns=['s1', 's2'])
# df_s1 = df.drop(columns=['s2'])
# df_s2 = df.drop(columns=['s1'])

# sns.heatmap(df_s1, fmt="g", cmap='viridis')
# plt.xlabel('Structrure')
# plt.title("Distance between C4 atoms of paired nucleotides")
# plt.ylabel("Pair")
# plt.show()

# sns.heatmap(df_s2, fmt="g", cmap='viridis')
# plt.xlabel('Structrure')
# plt.title("Distance between C4 atoms of paired nucleotides")
# plt.ylabel("Pair")
# plt.show()

# hm = sns.heatmap(data = df) 
# plt.xlabel('Structure')
# plt.title('Distance between C4 atoms of paired nucleotides in 2 RNA structures')
# plt.ylabel("Pair")
# plt.show()
