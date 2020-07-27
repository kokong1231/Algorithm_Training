import re                               # 정규식을 이용해서 특정 문자열 검색 모듈

point = input()
point_s = re.compile(r'(\d{1,2})(\w?)(.?)(\d{1,2})(\w?)(.?)(\d{1,2})(\w?)(.?)')

match = point_s.search(point)           # match.group(x) <- '()'로 묶은 정규식 값들을 출력 없으면 none

dic = -1
round_value = 1
round_sum = []

def point_mul (a, b):                   # S, D, T 에 대한 제곱 계산
    if a == 'S':
        value = int(match.group(b)) ** 1

    elif a == 'D':
        value = int(match.group(b)) ** 2

    elif a == 'T':
        value = int(match.group(b)) ** 3

    return str(value)

for x in range(3):                      # 인덱스 값을 확인하여 제곱값 round_sum 배열에 삽입
    round_sum.append(point_mul(match.group(x + 1 + round_value), x + round_value))
    round_value += 2

round_value = 3                         # 라운드 값 초기화

def point_dub (a, b, c, dic):           # '*'은 2배 '#'은 -1배
    value_a = b[0]
    value_b = b[1]
    value_c = b[2]

    if a == '*' and c == 0:
        value_a = int(b[0]) * 2

    elif a == '*' and c == 1:
        value_b = int(b[1]) * 2
        value_a = int(b[0]) * 2

    elif a == '*' and c == 2:
        value_c = int(b[2]) * 2
        value_b = int(b[1]) * 2

    if a == '#' and c == 0:
        value_a = int(b[c]) * dic
        dic -= 1

    elif a == '#' and c == 1:
        value_b = int(b[c]) * dic
        dic -= 1

    elif a == '#' and c == 2:
        value_c = int(b[c]) * dic
        dic -= 1
        
    return str(value_a), str(value_b), str(value_c)

for y in range(3):                      # 배열 '#'과 '*' 적용한 값 입력
    if match.group(round_value) != '':
        round_sum[0], round_sum[1], round_sum[2] = point_dub(match.group(round_value), round_sum, y, dic)
    round_value += 3

print(int(round_sum[0]) + int(round_sum[1]) + int(round_sum[2]))    # 최종 값 합산 출력