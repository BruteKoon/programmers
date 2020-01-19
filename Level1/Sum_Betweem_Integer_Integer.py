def solution(a, b):
    answer = 0
    for a in range (min(a,b),max(a,b)+1):
        answer = answer + a
    return answer
