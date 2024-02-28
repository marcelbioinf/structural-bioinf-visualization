import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import numpy as np

seq ='GCGCGGAUAGCUCAGUCGGUAGAGCAGGGGAUUGAAAAUCCCCGUGUCCUUGGUUCGAUUCCGAGUCCGCGCAC'
bracket =  '.((((((..((((.....[..)))).(((((.......))))).....(((((..]....)))))))))))...'



def get_pairs(bracket):

    l = len(bracket)
    pairs = []

    symbols = {'(': ')', '{': '}', '[': ']', '<': '>'}
    stack_dict = {')': [], '}': [], ']': [], '>': []}

    for i, char in enumerate(bracket):
        if char in symbols.keys():
            stack_dict[symbols[char]].append(i) 
        elif char in symbols.values():
            if stack_dict[char]:
                j = stack_dict[char].pop()
                pairs.append((j,i))
                #pairs.append((j,i))

    pairs.sort(key=lambda x: x[0])
    return pairs


pairs = get_pairs(bracket)
#print(pairs)



fig, ax = plt.subplots(figsize=(len(seq),5))

for i,j in pairs:
    start_index = i
    end_index = j

    # Calculate the mid-point between two indices
    mid_point = (start_index + end_index) / 2

    # Create an arc patch
    arc_patch = Arc((mid_point, 0),  # Center of the arc
                    width=end_index - start_index,  # Width of the arc
                    height=(end_index - start_index)/50,  # Height of the arc
                    theta1=0,  # Starting angle of the arc
                    theta2=180, # Ending angle of the arc
                    color='red')  

    # Add the patch to the plot
    ax.add_patch(arc_patch)


ax.set_xticks(range(len(seq)))
ax.set_xticklabels(list(seq))
ax.set_yticks([])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

plt.title('RNA pairs plot')
plt.savefig('./fig_4.0.svg', format='svg')
plt.show()
