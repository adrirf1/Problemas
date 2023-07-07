def series_resistance(lst):
    if sum(lst) <= 1:
        return "{} ohm".format(sum(lst))
    else:
        return "{} ohms".format(sum(lst))