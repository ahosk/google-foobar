def solution(pegs):
    n = len(pegs)
    dist = [pegs[i+1] - pegs[i] for i in range(n-1)]

    A = [[0] * (n-2) for _ in range(n-2)]
    for i in range(n-2):
        A[i][i] = 1
        A[i][i+1] = 1
    for i in range(n-3):
        A[i][n-3] = 2 * (-1)**i
    b = [2 * dist[i] * (-1)**i for i in range(n-1)]

    try:
        x = gauss(A, b)
    except ValueError:
        return [-1, -1]

    r0 = x[0]
    if r0 < 1:
        return [-1, -1]
      
    if n % 2 == 0:
        rb = x[-1]
        ra = 2 * r0
    else:
        rb = 1
        ra = r0
    gcd = math.gcd(ra, rb)
    return [ra // gcd, rb // gcd]

def gauss(A, b):
    n = len(A)
    for i in range(n):
        maxrow = max(range(i, n), key=lambda r: abs(A[r][i]))
        if i != maxrow:
            A[i], A[maxrow] = A[maxrow], A[i]
            b[i], b[maxrow] = b[maxrow], b[i]
        for r in range(i+1, n):
            factor = A[r][i] / A[i][i]
            for j in range(i, n):
                A[r][j] -= factor * A[i][j]
            b[r] -= factor * b[i]
    x = [0] * n
    for i in range(n-1, -1, -1):
        x[i] = b[i] / A[i][i]
        for j in range(i):
            b[j] -= A[j][i] * x[i]
    return x
