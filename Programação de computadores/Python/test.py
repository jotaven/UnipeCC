import matplotlib.pyplot as plt
import numpy as np

pop = []
np_pop = np.array(pop)


values = [0,0.6,1.4,1.6,2.2,2.5,2.6,3.2,3.5,3.9,4.2,6]
plt.hist(values)
plt.show()
test = np.random.normal(100, 10, 10)
test2 = []
for c in range(0,10):
    test2.append(c+1)
print(test2)
plt.plot(test2, test)
plt.xlabel("distancia")
plt.ylabel("quantidade")
plt.show()
year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]
plt.plot(year, pop)
plt.scatter(year, pop)
plt.show()
