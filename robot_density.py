## This is a Python script that creates a bar chart of the number of robots per 10,000 workers in various countries.
## Source World Robotics 2024

import matplotlib.pyplot as plt

data = [1012, 770, 470, 429, 419, 347, 306, 306, 302, 295, 294, 264]
x_axis = ['R. Korea', 'Singapore', 'China', 'Germany', 'Japan', 'Sweden', 'Denmark', 'Slovenia', 'Switzerland', 'USA', 'Taiwan', 'Netherlands']

fig = plt.figure()
plt.bar(x_axis, data, color='red')
fig.autofmt_xdate()
plt.xlabel('Country')
plt.ylabel('Robots/10,000 workers')
plt.title('Robots per 10,000 workers in various countries (WR-2024)')
plt.show()
