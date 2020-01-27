def solution(arr):
    answer = 0
    length = len(arr)
    for i in arr:
        answer = answer + i
    answer = answer / float(length)
    return answer
