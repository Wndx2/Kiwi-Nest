import random
import matplotlib.pyplot as plt

plt.rcParams['toolbar'] = 'none'

def get_random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

def pick_text_color(bg_color):
    r = int(bg_color[1:3], 16)
    g = int(bg_color[3:5], 16)
    b = int(bg_color[5:7], 16)
    brightness = 0.2126*r + 0.7152*g + 0.0722*b
    return 'black' if brightness > 128 else 'white'

color_list = [get_random_color() for _ in range(9)]

fig, axs = plt.subplots(3, 3, figsize=(9, 9), dpi=225)

for idx, ax in enumerate(axs.flat):
    hex_color = color_list[idx]
    ax.set_facecolor(hex_color)
    text_color = pick_text_color(hex_color)
    ax.text(0.5, 0.5, f'{idx + 1}\n{hex_color.upper()}',
            color=text_color, ha='center', va='center',
            fontsize=18, fontfamily='SN Pro')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.spines[:].set_visible(False)

plt.subplots_adjust(wspace=0, hspace=0, left=0, right=1, top=1, bottom=0)

# Save the image (optional)
plt.savefig("colors/rcotw.png", bbox_inches='tight', pad_inches=0)
# plt.show()