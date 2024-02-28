import matplotlib.pyplot as plt
import numpy as np

seq = 'GCGCGGAUAGCUCAGUCGGUAGAGCAGGGGAUUGAAAAUCCCCGUGUCCUUGGUUCGAUUCCGAGUCCGCGCAC'
bracket = '.((((((..((((.....[..)))).(((((.......))))).....(((((..]....)))))))))))...)'


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


def plot_round_plot(seq, pairs):
    fig, ax = plt.subplots(figsize=(10, 10))

    ax.plot(np.cos(2 * np.pi * np.arange(len(seq)) / len(seq)),
            np.sin(2 * np.pi * np.arange(len(seq)) / len(seq)), color='red', lw=0.7)

    # Plot the chords as straight lines
    for start, end in pairs:
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

