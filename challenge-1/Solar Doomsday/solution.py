def solution(area):
    squares =[]
    while area > 0:
        square = int(area**0.5)**2
        squares.append(square)
        area -= square
    return squares
