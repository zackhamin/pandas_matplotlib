# First commit
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# plt.show() has to go at the end of plots
#%%
x = np.linspace(0,5,11)
y = x ** 2

# Functional method to create
plt.plot(x,y,"r")
plt.xlabel("X Label")
plt.ylabel("Y Label")
plt.title("Title")
# plt.show()

plt.subplot(1,2,1)
plt.plot(x,y,"g")

plt.subplot(1,2,2)
plt.plot(y,x,"b")
plt.show()