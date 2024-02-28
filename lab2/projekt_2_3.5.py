import matplotlib.pyplot as plt
import numpy as np

seq ='GCGCGGAUAGCUCAGUCGGUAGAGCAGGGGAUUGAAAAUCCCCGUGUCCUUGGUUCGAUUCCGAGUCCGCGCAC'
bracket =  '.((((((..((((.....[..)))).(((((.......))))).....(((((..]....)))))))))))...'

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
print(y)
print(len(x))
print(len(y))

figure = plt.figure(figsize=(14,7))
plt.plot(x,y)
plt.title("Mountainplot of a sequence")
plt.xticks(np.arange(len(list(seq))),list(seq), fontsize=8)
plt.savefig('./fig_3.5.svg', format='svg')
plt.show()
