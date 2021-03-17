
genes = {'USA':29862124,'India':11285561,'Brazil':11205972,'Russia':4360823,'UK':4234924}
L = [29862124,11285561,11205972,4360823,4234924]
total = 0
for i in range(len(L)):
    total += L[i]
print(total)
P = []
for j in range(len(L)):
    a = float(L[j]/total)
    P.append(a)
import matplotlib.pyplot as plt
labels = 'USA','India','Brazil','Russia','UK'
plt.pie(P, labels=labels, autopct = '%1.1f%%')
plt.axis('equal')
plt.show()
