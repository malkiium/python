import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd

# Sample data
# Each row: [keyboard_mouse_activity, app, context, feeling, energy_level]
data = [
    [120, 'VSCode', 'Python Project', 'Focused', 0.9],
    [30, 'Chrome', 'Research', 'Bored', 0.3],
    [80, 'Photoshop', 'Design', 'Excited', 0.8],
    [50, 'Slack', 'Chat', 'Neutral', 0.5],
    [200, 'Terminal', 'Server Setup', 'Focused', 1.0],
    [10, 'YouTube', 'Break', 'Relaxed', 0.2]
]

# Convert to DataFrame
df = pd.DataFrame(data, columns=['keyboard_mouse', 'app', 'context', 'feeling', 'energy'])

# Map categorical variables to numeric values for plotting
app_mapping = {app: i for i, app in enumerate(df['app'].unique())}
context_mapping = {ctx: i for i, ctx in enumerate(df['context'].unique())}
feeling_mapping = {f: i for i, f in enumerate(df['feeling'].unique())}

df['app_num'] = df['app'].map(app_mapping)
df['context_num'] = df['context'].map(context_mapping)
df['feeling_num'] = df['feeling'].map(feeling_mapping)

# Color map for feelings
colors = plt.cm.viridis(df['feeling_num'] / max(df['feeling_num']))

# 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Scatter plot: x=keyboard/mouse, y=app, z=context
# Color=feeling, Size=energy level * scale
scatter = ax.scatter(
    df['keyboard_mouse'], 
    df['app_num'], 
    df['context_num'], 
    c=colors, 
    s=df['energy']*200,  # scale for visibility
    alpha=0.8
)

# Labels and ticks
ax.set_xlabel('Keyboard/Mouse Activity')
ax.set_ylabel('App')
ax.set_zlabel('Context')

# Set Y and Z ticks to categorical labels
ax.set_yticks(list(app_mapping.values()))
ax.set_yticklabels(list(app_mapping.keys()))
ax.set_zticks(list(context_mapping.values()))
ax.set_zticklabels(list(context_mapping.keys()))

# Optional: add legend for colors (feeling)
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], marker='o', color='w', label=feeling,
           markerfacecolor=plt.cm.viridis(feeling_mapping[feeling]/max(df['feeling_num'])), markersize=10)
    for feeling in feeling_mapping
]
ax.legend(handles=legend_elements, title="Feeling", loc='upper left')

plt.show()
