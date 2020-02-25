def solution(phone_number):
    number = len(phone_number) - 4
    star_number = ''
    for i in range(number):
        star_number = star_number + '*'
    star_number = star_number + phone_number[-4:]
    return star_number
