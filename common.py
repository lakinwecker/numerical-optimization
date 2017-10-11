from collections import OrderedDict
import itertools

# From https://stackoverflow.com/questions/214359/converting-hex-color-to-rgb-and-vice-versa
def hex_to_rgb(value):
    """Return (red, green, blue) for the color given as #rrggbb."""
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def rgb_to_hex(red, green, blue):
    """Return color as #rrggbb for the given color values."""
    return '#%02x%02x%02x' % (red, green, blue)


class emptyobj(object):
    pass

colors = emptyobj()
colors.bar = OrderedDict()
colors.line = OrderedDict()
colors.points = colors.line

colors.bar['blue'] = rgb_to_hex(114, 147, 203)
colors.bar['orange'] = rgb_to_hex(225, 151, 76)
colors.bar['green'] = rgb_to_hex(132, 186, 91)
colors.bar['red'] = rgb_to_hex(211, 94, 96)
colors.bar['grey'] = rgb_to_hex(128, 133, 133)
colors.bar['purple'] = rgb_to_hex(144, 103, 167)
colors.bar['maroon'] = rgb_to_hex(171, 104, 87)
colors.bar['beige'] = rgb_to_hex(204, 194, 16)

colors.line['blue'] = rgb_to_hex(57, 106, 177)
colors.line['orange'] = rgb_to_hex(218, 124, 48)
colors.line['green'] = rgb_to_hex(62, 150, 81)
colors.line['red'] = rgb_to_hex(204, 37, 41)
colors.line['grey'] = rgb_to_hex(83, 81, 84)
colors.line['purple'] = rgb_to_hex(107, 76, 154)
colors.line['maroon'] = rgb_to_hex(146, 36, 40)
colors.line['beige'] = rgb_to_hex(148, 139, 61)

colors.bar_indexed = list(colors.bar.values())
colors.line_indexed = list(colors.line.values())
colors.points_indexed = list(colors.points.values())
