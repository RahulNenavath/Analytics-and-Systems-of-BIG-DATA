# 2nd Question:

import matplotlib.pyplot as plt

# pip install stemgraphic

import stemgraphic 

points = [22, 21, 24, 19, 27, 28, 24, 25, 29, 28, 26, 31, 28, 27, 22, 39, 20, 10, 26, 24, 27, 28, 26, 28, 18, 32, 29,
25, 31, 27]

stemgraphic.stem_graphic(points, scale = 10) 

plt.show()

# outliers are 39 and 10.