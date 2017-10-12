class ParametricCurve(object):
    def __call__(self, u):
        raise NotImplementedError("Subclasses must implement this")

# B-Spline Basis function
def N(i, k, x, knots):
    T = knots
    if k == 0:
        if T[i] <= x < T[i+1]:
            return 1.0
        else:
            return 0.0
    else:
        part1 = 0.0
        if (T[i+k] - T[i] != 0.0):
            part1 = ((x-T[i])/(T[i+k] - T[i])) * N(i, k-1, x, T)
        part2 = 0.0
        if (T[i+k+1] - T[i+1] != 0.0):
            part2 = ((T[i+k+1] - x)/(T[i+k+1] - T[i+1])) * N(i+1, k-1, x, T)
        return part1 + part2

class BSplineCurve(ParametricCurve):
    def __init__(self, order, knots, points):
        self.order = order
        self.p = self.order - 1
        self.knots = knots
        m = len(self.knots) - 1
        self.points = points
        n = len(self.points) - 1
        assert len(self.points) > self.order, "Number of points: {} must be > than order: {}".format(len(self.points), self.order)
        assert self.p == m - n - 1, "p == m - n - 1 ... {} == {} - {} - 1".format(self.p, m, n)
        self.knot_range = (self.knots[-1] - self.knots[0])


    def __call__(self, u):
        assert u >= 0.0 and u <= 1.0
        t = (u * self.knot_range) + self.knots[0]
        final = 0.0
        for i, Pi in enumerate(self.points):
            basis = N(i, self.p, t, self.knots)
            final += basis * Pi
        return final

def uniform_knots(n, order):
    knots = list(range(n-order+2))
    beginning = [0] * (order-1)
    ending = [knots[-1]] * (order-1)
    return beginning + knots + ending
