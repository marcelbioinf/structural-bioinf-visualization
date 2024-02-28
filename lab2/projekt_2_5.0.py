import matplotlib.pyplot as plt
import numpy as np

seq = 'GCGCGGAUAGCUCAGUCGGUAGAGCAGGGGAUUGAAAAUCCCCGUGUCCUUGGUUCGAUUCCGAGUCCGCGCAC'
bracket = '.((((((..((((.....[..)))).(((((.......))))).....(((((..]....)))))))))))...)'


pseudoknots = []
def get_pairs(bracket):

    l = len(bracket)
    pairs = []

    symbols = {'(': ')', '{': '}', '[': ']', '<': '>'}
    stack_dict = {')': [], '}': [], ']': [], '>': []}

    for i, char in enumerate(bracket):
        if char in symbols.keys():
            if char == '[':
                pseudoknots.append(i)
            stack_dict[symbols[char]].append(i) 
        elif char in symbols.values():
            if stack_dict[char]:
                if char == ']':
                    pseudoknots.append(i)
                j = stack_dict[char].pop()
                pairs.append((j,i))
                #pairs.append((j,i))

    pairs.sort(key=lambda x: x[0])
    return pairs


pairs = get_pairs(bracket)

stems = []
current_subsequence = []

for pair in pairs:
    if not current_subsequence:
        current_subsequence.append(pair)
    else:
        last_pair = current_subsequence[-1]
        if pair[0] == last_pair[0] + 1 and pair[1] == last_pair[1] - 1:
            current_subsequence.append(pair)
        else:
            stems.append(tuple(zip(*current_subsequence)))
            current_subsequence = [pair]

# Append the last subsequence
if current_subsequence:
    stems.append(tuple(zip(*current_subsequence)))

print(stems)
print(pseudoknots)





## wykres 3.5 ###

x = list(range(0, len(seq)))
y = [0]

for i, j in enumerate(bracket):
    if j in ['(', '[']:
        y.append(y[-1]+1)
    elif j in [')', ']']:
        y.append(y[-1]-1)
    else:
        y.append(y[-1])

y.pop(0)
y.pop()

figure = plt.figure(figsize=(14,7))
plt.plot(x,y, color='black')
for stem in stems:
    plt.plot(x[stem[0][0]-1:stem[0][-1]+1], y[stem[0][0]-1:stem[0][-1]+1], color='red')
    plt.plot(x[stem[1][-1]-1:stem[1][0]+1], y[stem[1][-1]-1:stem[1][0]+1], color='red')
plt.title("Mountainplot of a sequence")
plt.xticks(np.arange(len(list(seq))),list(seq), fontsize=8)
# plt.savefig('./fig_3.5.svg', format='svg')
plt.show()


## WYKRES 4 ###
from matplotlib.patches import Arc
fig, ax = plt.subplots(figsize=(len(seq),5))

unpacked_stems = [value for sublist in stems for values in sublist for value in values]
print(unpacked_stems)
for i,j in pairs:
    start_index = i
    end_index = j

    # Calculate the mid-point between two indices
    mid_point = (start_index + end_index) / 2

    # Create an arc patch
    if i in pseudoknots:
        arc_patch = Arc((mid_point, 0),  # Center of the arc
                width=end_index - start_index,  # Width of the arc
                height=(end_index - start_index)/50,  # Height of the arc
                theta1=0,  # Starting angle of the arc
                theta2=180, # Ending angle of the arc
                color='black',
                linestyle = 'dotted')  
        
    elif i in unpacked_stems:
        arc_patch = Arc((mid_point, 0),  # Center of the arc
                        width=end_index - start_index,  # Width of the arc
                        height=(end_index - start_index)/50,  # Height of the arc
                        theta1=0,  # Starting angle of the arc
                        theta2=180, # Ending angle of the arc
                        color='red')  
    else:
        arc_patch = Arc((mid_point, 0),  # Center of the arc
                width=end_index - start_index,  # Width of the arc
                height=(end_index - start_index)/50,  # Height of the arc
                theta1=0,  # Starting angle of the arc
                theta2=180, # Ending angle of the arc
                color='black')  

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
#plt.savefig('./fig_4.0.svg', format='svg')
plt.show()


### WYKRES 4.5 ###
def plot_round_plot(seq, pairs):
    fig, ax = plt.subplots(figsize=(10, 10))

    ax.plot(np.cos(2 * np.pi * np.arange(len(seq)) / len(seq)),
            np.sin(2 * np.pi * np.arange(len(seq)) / len(seq)), color='red', lw=0.7)

    # Plot the chords as straight lines
    for start, end in pairs:
        if start in pseudoknots:
            start_angle = 2 * np.pi * start / len(seq)
            end_angle = 2 * np.pi * end / len(seq)
            ax.plot([np.cos(start_angle), np.cos(end_angle)],
                    [np.sin(start_angle), np.sin(end_angle)], color='black', linestyle='dotted')
        else:
            start_angle = 2 * np.pi * start / len(seq)
            end_angle = 2 * np.pi * end / len(seq)
            ax.plot([np.cos(start_angle), np.cos(end_angle)],
                    [np.sin(start_angle), np.sin(end_angle)], color='blue', lw=1)

    # Add labels to each base in the sequence
    for i, (x, y) in enumerate(zip(np.cos(2 * np.pi * np.arange(len(seq)) / len(seq)),
                                   np.sin(2 * np.pi * np.arange(len(seq)) / len(seq)))):
        ax.text(x, y, seq[i], ha='center', va='center', fontsize=9)

    # Set aspect ratio to be equal
    ax.set_aspect('equal', adjustable='box')

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_xticks([])
    ax.set_yticks([])
    plt.title("Circular visualization of bracket RNA sequence")
    plt.savefig('./fig_4.5.svg', format='svg')
    plt.show()

pairs = get_pairs(bracket)
plot_round_plot(seq, pairs)