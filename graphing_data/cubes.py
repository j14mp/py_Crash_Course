import matplotlib.pyplot as plt
xvalues = range(1, 5001)
yvalues = [x**3 for x in xvalues]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(xvalues, yvalues, c=yvalues,cmap=plt.cm.hot, s=10)


ax.set_title("Cubed Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Cube of Value", fontsize = 14)

#Set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=14, width=100)
ax.axis([0,5000, 0, 45_000_100_000])


plt.show()
