"""Dictionary Functions"""

__author__ = "730574207"


def invert(d: dict[str, str]) -> dict[str, str]:
    """Dictionary with swapped keys and values"""
    inverted: dict[str, str] = {}
    for key in d:
        value = d[key]
        """ Raise error for duplicate keys"""
        if value in inverted:
            raise KeyError("More than one of same key!")
        inverted[value] = key
    return inverted


def count(items: list[str]) -> dict[str, int]:
    """Dictionary with count of each string in list"""
    counts: dict[str, int] = {}
    for item in items:
        if item in counts:
            counts[item] = counts[item] + 1
        else:
            counts[item] = 1
    return counts


def favorite_color(colors: dict[str, str]) -> str:
    """Dictionary that returns most frequent color"""
    if not colors:
        return ""
    color_list = list(colors.values())
    """Implement count function"""
    counts_colors = count(color_list)
    max_count = 0
    favorite = ""
    for color in color_list:
        if counts_colors[color] >= max_count:
            max_count = counts_colors[color]
            favorite = color
    return favorite


def bin_len(words: list[str]) -> dict[int, set[str]]:
    """Dictionary that associates word lengths with set of words that length"""
    bins: dict[int, set[str]] = {}
    for word in words:
        length = len(word)
        if length in bins:
            bins[length].add(word)
        else:
            bins[length] = {word}
    return bins
