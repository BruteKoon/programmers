def solution(n):
    N = str(n)
    M = list(N[::-1])
    for i in range(len(M)):
        M[i] = int(M[i])
    return M
