from random import randint

def generate_numbers(n):
    drawed_list = []
    count = 0
    
    while count < n:
        draw = randint(1,45)
        
        if draw not in drawed_list:
            drawed_list.append(draw)
            count += 1
        
    return drawed_list


def draw_winning_numbers():
    win_num = sorted(generate_numbers(6))
    
    while True:
        bonus = randint(1,45)
        if bonus not in win_num:
            win_num.append(bonus)
            break
    
    return win_num

def count_matching_numbers(numbers, winning_numbers):
    count = 0
    for num in numbers:
        if num in winning_numbers:
            count += 1
    
    return count

def check(numbers, winning_numbers):
    cash = {0:0, 1:0, 2:0, 3:5000, 4:50000, 5:1000000, 6:1000000000}
    
    count = count_matching_numbers(numbers, winning_numbers)
    
    if count == 6:
        if winning_numbers[-1] in numbers:
            return 50000000
    return cash[count]

# 테스트 코드
# print(check([2, 7, 11, 14, 25, 40], [2, 11, 13, 14, 30, 35]))
# print(check([2, 7, 11, 14, 25, 40], [14]))
# print(check([2, 7, 11, 14, 25, 40], [2, 7, 11, 14, 25, 40,42]))