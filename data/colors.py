from math import floor


def hex2rgb(hex):
    return tuple(int(hex[i : i + 2], 16) for i in (1, 3, 5))


def rgb2hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(*rgb)


def color_is_bright(hex):
    r, g, b = hex2rgb(hex)
    luminance = (0.299 * r + 0.587 * g + 0.114 * b) / 255
    return luminance > 0.5


def blend_channel(v1, v2, alpha):
    blend = alpha * v2 + ((1 - alpha) * v1)
    return floor(min(max(0, blend), 255) + 0.5)


def blend_colors(c1, c2, alpha):
    c1, c2 = hex2rgb(c1), hex2rgb(c2)
    return rgb2hex(tuple(blend_channel(v1, v2, alpha) for (v1, v2) in zip(c1, c2)))
