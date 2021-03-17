gene_lengths=[9410,394141,4442,105338,19149,76779,126550,36296,842,15981]
exon_counts=[51,1142,42,216,25,650,32533,57,1,523]
P = []
for i in range(len(gene_lengths)):
    a = int(gene_lengths[i]/exon_counts[i])
    P.append(a)
sorted(P)
P = sorted(P)
print(P)
import numpy as np
import matplotlib.pyplot as plt
plt.boxplot(P,
            vert = True,
            whis = 1.5,
            patch_artist = True,
            meanline = False,
            showbox = True,
            showcaps = True,
            showfliers = True,
            notch = False
                )
plt.show()
