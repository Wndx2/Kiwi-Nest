'''Random Color Generator for Kiwi Nest.'''

# Importing modules.
import random
import matplotlib.pyplot as plt

# Removes Matplot's toolbar.
plt.rcParams['toolbar'] = 'none'

# Generates colors that pass the minimum brightness.
def get_random_color(min_brightness=155):
    while True:
        hex_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        # Setting colors in hex format.
        r = int(hex_color[1:3], 16)
        g = int(hex_color[3:5], 16)
        b = int(hex_color[5:7], 16)
        # Calculates brightness using relative luminance.
        brightness = 0.2126*r + 0.7152*g + 0.0722*b
        if brightness >= min_brightness:
            # Returns hex colors that pass the minimum brightness.
            return hex_color

# Determines text color based on background brightness.
def pick_text_color(bg_color):
    r = int(bg_color[1:3], 16)
    g = int(bg_color[3:5], 16)
    b = int(bg_color[5:7], 16)
    # Calculates brightness using relative luminance.
    brightness = 0.2126*r + 0.7152*g + 0.0722*b
    # Returns black text on light backgrounds, white on dark.
    return 'black' if brightness > 128 else 'white'

# Picks 9 light hex colors for the grid.
color_list = [get_random_color() for _ in range(9)]

# Generates 3x3 grid with DPI of 225 (2025x2025 pixels).
fig, axs = plt.subplots(3, 3, figsize=(9, 9), dpi=225)

# Populates each square in the grid.
for idx, ax in enumerate(axs.flat):
    hex_color = color_list[idx]
    ax.set_facecolor(hex_color)  # Set square background color.
    text_color = pick_text_color(hex_color)  # Pick contrast text color.
    # Displays index number and HEX color code.
    ax.text(0.5, 0.5, f'{idx + 1}\n{hex_color.upper()}',
            color=text_color, ha='center', va='center',
            fontsize=18, fontfamily='SN Pro')
    # Removes ticks and axis lines for a clean look.
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.spines[:].set_visible(False)  # Hide border lines.

# Removes spacing and margins between subplots.
plt.subplots_adjust(wspace=0, hspace=0, left=0, right=1, top=1, bottom=0)

randomnumber = random.randint()

# Saves final image as 2025x2025 PNG in the "colors" folder.
plt.savefig("colors/rcotw{}.png", bbox_inches='tight', pad_inches=0)

# Uncomment to preview the image interactively.
# plt.show()