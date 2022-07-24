
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("/home/marco/Documents/code/python/Heatmap_generator/seattle-weather.csv")

result = df.pivot(index="mmdd",columns="year", values="temp_max" )
print(result)

fig, ax = plt.subplots(figsize=(25,15))

# Add title to the Heat map
title = "Seattle Max Temp Heatmap in °C"

# Set the font size and the distance of the title from the plot
plt.title(title,fontsize=18)
ttl = ax.title
ttl.set_position([0.5,1.05])

# Hide ticks for X & Y axis
ax.set_xticks([])
ax.set_yticks([])

# Remove the axes
#ax.axis('off')

# Use the heatmap function from the seaborn package
sns.heatmap(result)

manager = plt.get_current_fig_manager()
#manager.full_screen_toggle()

#save the fig
plt.savefig('foo.pdf')

# Display the Heatmap
plt.show()