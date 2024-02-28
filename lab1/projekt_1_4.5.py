import sys
import math
from Bio.PDB.PDBParser import PDBParser
import seaborn as sns
import matplotlib.pyplot as plt


def get_euclid_dist(a,b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2 + (a[2] - b[2])**2)


parser = PDBParser(QUIET=True)

if len(sys.argv) < 2:
    raise Exception('No file given as parameter. Please add file path to command line')
file_path = sys.argv[1]

structure = parser.get_structure("s1", file_path)
model = structure[0]

o_coords, p_coords = [], []

for atom in model.get_atoms():
    if atom.id == 'P':
        if len(o_coords) == 0:
            continue
        p_coords.append(atom.get_coord())
    elif atom.id == "O3'":
        o_coords.append(atom.get_coord())


print(f"Found {len(p_coords)} atom pairs")

distances = [get_euclid_dist(p,c) for p,c in zip(p_coords, o_coords[:-1])]
distances = [i for i in distances if i >= 1.571 and i <= 1.643]

print(f"{len(p_coords) - len(distances)} atoms were treated as outliers")


#sns.distplot(distances, hist=True, kde=True,  color = 'darkblue', hist_kws={'edgecolor':'black'},kde_kws={'linewidth': 4})
sns.histplot(distances, kde=True, color = 'darkblue')
plt.xlabel('Distance')
plt.title("Distances between O3' and P atoms in RNA")
plt.show()