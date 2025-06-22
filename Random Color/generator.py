import random
import matplotlib.pyplot as plt

def random_hex_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

# Generate 4 random colors
colors = [random_hex_color() for _ in range(4)]

# Create a 2x2 plot
fig, axs = plt.subplots(2, 2, figsize=(4, 4))

for i, ax in enumerate(axs.flat):
    color = colors[i]
    ax.set_facecolor(color)
    ax.text(0.5, 0.5, f'{i+1}', color='white' if i != 2 else 'black',
            ha='center', va='center', fontsize=20, weight='bold')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

plt.tight_layout()
plt.show()
