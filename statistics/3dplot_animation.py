import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go


# read the CSV file into pandas DataFrame
df = pd.read_csv('/mnt/d/CodingPractice/statistics/data.csv')

# # Print the data frame
# # print(df)
# # df

# # Using plotly express
# # create a 3D scatter plot 

# fig = px.scatter_3d(df, x='Pull Strength y', y = 'Wire length x1', z='Die height x2')
# # fig = go.Figure(data=[go.Surface(x=df['Pull Strength y'], y=df['Wire length x1'], z=df['Die height x2'])])

# # Add animation 
# fig.update_layout(scene=dict(camera=dict(up=dict(x=0, y=0, z=1), center=dict(x=0, y=0, z=0), eye=dict(x=1.25, y=1.25, z=1.25))))
# # fig.update_layout(scene=dict(xaxis_title='Pull Strength y', yaxis_title='Wire length x1', zaxis_title='Die height x2'))
# # fig.update_traces(marker=dict(size=5, line=dict(width=1, color='DarkSlateGrey')), selector=dict(mode='markers'))


# fig.show()


# Using matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# read the CSV file into pandas DataFrame
df = pd.read_csv('/mnt/d/CodingPractice/statistics/data.csv')

# create a 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(df['Pull Strength y'], df['Wire length x1'], df['Die height x2'])

# create a 3D surface plot
surf = ax.plot_trisurf(df['Pull Strength y'], df['Wire length x1'], df['Die height x2'], cmap='viridis', edgecolor='none')

# add labels
ax.set_xlabel('Pull Strength y')
ax.set_ylabel('Wire length x1')
ax.set_zlabel('Die height x2')

# add colorbar
fig.colorbar(scatter)

# add animation
def update(num):
    ax.view_init(elev=10., azim=num)

ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 360, 2), interval=50)

# show the plot
plt.show()