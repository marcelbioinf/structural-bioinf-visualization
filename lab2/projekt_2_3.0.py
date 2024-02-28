import matplotlib.pyplot as plt
import numpy as np


seq = 'GCGCGGAUAGCUCAGUCGGUAGAGCAGGGGAUUGAAAAUCCCCGUGUCCUUGGUUCGAUUCCGAGUCCGCGCAC'
bracket = '.((((((..((((.....[..)))).(((((.......))))).....(((((..]....)))))))))))...'


def get_matrix(bracket):

    l = len(bracket)
    pairs = np.zeros((l, l))

    symbols = {'(': ')', '{': '}', '[': ']', '<': '>'}
    stack_dict = {')': [], '}': [], ']': [], '>': []}

    for i, char in enumerate(bracket):
        if char in symbols.keys():
            stack_dict[symbols[char]].append(i) 
        elif char in symbols.values():
            if stack_dict[char]:
                j = stack_dict[char].pop()
                pairs[i,j] = 1
                pairs[j,i] = 1

    np.fill_diagonal(pairs,1)

    return pairs

dotplot = get_matrix(bracket)

print(dotplot)

plt.figure(figsize=(11,10))
plt.imshow(dotplot, cmap='viridis', interpolation='nearest')
plt.title("Dotplot of a sequence")
plt.xticks(np.arange(len(list(seq))),list(seq), fontsize=8)
plt.yticks(np.arange(len(list(seq))),list(seq), fontsize=8)
plt.savefig('./fig_3.0.svg', format='svg')
plt.show()
