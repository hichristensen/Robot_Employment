# Import pands

import pandas as pd
import matplotlib.pyplot as plt 

data_frame = pd.read_csv("/users/hic/src/Robot_Employment/robot-employment-data.csv")

year = data_frame["Year"];
robots = data_frame["Robots"]
employment = data_frame["Employment"]

# create figure and axis objects with subplots()
fig,ax = plt.subplots()
# make a plot
ax.plot(year, robots, color="red", marker="o")
ax.grid()
# set x-axis label
ax.set_xlabel("year",fontsize=14)
# set y-axis label
ax.set_ylabel("US Robot sales",color="red",fontsize=14)
# twin object for two different y-axis on the sample plot
ax2=ax.twinx()
# make a plot with different y-axis using second axis object
ax2.plot(year, employment,color="blue",marker="o")
ax2.set_ylabel("Manufacturing Employment (x 1000)",color="blue",fontsize=14)
plt.title("Employment in manufacturing and sale of robots in the US (2010-2022)")
plt.show()
# Save to file as PDF
fig.savefig('robot-employment22.pdf', format='pdf', dpi=220, bbox_inches='tight')
