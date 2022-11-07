class Lagrange:

    @staticmethod
    def formula():
        return "/Lagrange.png"

    @staticmethod
    def methodName():
        return "Lagrange.png"

    def solve():
        roundValue = 9
        x = np.array([0, 1, 4, 6])
        y = np.array([2, 3, 18, 38])

        n = 4
        xp = 2
        yp = 0
        for i in range(n):

            p = 1

            for j in range(n):
                if i != j:
                    p = p * (xp - x[j])/(x[i] - x[j])

            yp = yp + p * y[i]

        return yp
