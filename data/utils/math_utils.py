# linear interpolation
# - smoothly moves a value (a) towards a target (b)
# - t determines how much of the distance towards the target has been covered.
# source of the formula: https://en.wikipedia.org/wiki/Linear_interpolation
def lerp(a: float, b: float, t: float) -> float:
    return (1 - t) * a + t * b