def solution(x):
    x_str = str(x)
    num_t = 0
    x_int = map(int, x_str)
    for i in x_int:
        num_t = num_t + i
    if x % num_t == 0:    
        answer = True
    else:
        answer = False
    return answer
