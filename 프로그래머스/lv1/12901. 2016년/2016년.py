def solution(a, b):
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    calendar = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    day_cnt = 0
    for month in range(1, a):
        day_cnt += calendar[month]
    day_cnt += b - 1
    return day[day_cnt % 7]