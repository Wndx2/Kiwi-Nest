import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.dates as mdates

plt.rcParams['toolbar'] = 'none'

file = pd.read_csv('membercount.csv')
dates = pd.to_datetime(file['DATE'], dayfirst=True)
member_counts = file['MEMBERCOUNT']
days = file['DAY']
first_col = file.iloc[:, 0].astype(str) 

fig, ax = plt.subplots(figsize=(10 , 6))
fig.canvas.manager.set_window_title('Kiwi Nest 2025 Member Growth')

fig.patch.set_facecolor('#000000')
ax.set_facecolor('#000000')

for spine in ax.spines.values():
    spine.set_visible(False)

ax.set_xticks([])
ax.set_yticks([])

ax.set_xlim(min(dates), max(dates))
ax.set_ylim(0, max(member_counts) * 1.1)
ax.set_aspect('auto')

ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

line, = ax.plot([], [], color='#524A9B', lw=2)

top_text = ax.text(0.5, 0.995, '', transform=ax.transAxes, ha='center', va='top', fontsize=14, fontweight='bold', color='#524A9B', font='Jenker Font')
day_text = ax.text(0.5, 0.07, '', transform=ax.transAxes, ha='center', va='bottom', fontsize=14, fontweight='bold', color='#524A9B', font='Jenker Font')
member_text = ax.text(0.5, 0.03, '', transform=ax.transAxes, ha='center', va='bottom', fontsize=14, fontweight='bold', color='#524A9B', font='Jenker Font')

def update(frame):
    line.set_data(dates[:frame], member_counts[:frame])
    top_text.set_text(first_col[frame-1])
    day_text.set_text(f'Day: {days[frame-1]}')
    member_text.set_text(f'Member Count: {member_counts[frame-1]:,.0f}')
    return line, top_text, day_text, member_text

ani = FuncAnimation(fig, update, frames=range(1, len(dates)+1), interval=1, blit=False, repeat=False)
# ani.save('server_traffic_growth.mp4', writer='ffmpeg', fps=30)
# Uncomment line above to download it locally.
plt.show()
