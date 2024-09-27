
import colorgram

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    # print(color)
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    newColor = (r,g,b)
    rgb_colors.append(newColor)
    



