def solution(num):
    answer = 0
    while(num != 1 or answer == 0):
        if num % 2 == 0:
            num = num / 2
        else:
            num = num * 3 + 1
        answer = answer + 1
        
        if answer >= 500 :
            return -1
    return answer
