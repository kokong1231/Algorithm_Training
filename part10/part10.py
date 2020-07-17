week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
today = []
m_patton = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for today_lop in range(3):
    today.append(input())

year_count = int(today[0]) // 4
year_count -= int(today[0]) // 100
year_count -= int(today[0]) // 400
    
sum_value = int(today[0]) * 365 + year_count + int(today[2])

for m_sum in range(int(today[1])):
    sum_value += int(m_patton[m_sum])

print(week[sum_value % 7 - 1])