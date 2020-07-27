n, arr1, arr2 = input(), input(), input()       # 값 입력

arr1 = arr1.split(',')                          # ',' 기준으로 배열 생성
arr2 = arr2.split(',')

def bit_sum(a,b):                               # arr1, arr2를 인자로 받아 or 연산 수행
    save = []

    for x in range(int(n)):
        save.append(int(a[x]) | int(b[x]))      # input 값은 String으로 받기 때문에 정수형(int)로 바꿔준 후 연산

    return save

arr_sum = bit_sum(arr1, arr2)                   # 함수 호출 후 반환값 arr_sum으로 반환

for x in range(int(n)):                         # 비트연산 수행 후 10진수로 되어있는 값을 2진수로 변경
    arr_sum[x] = format(arr_sum[x], 'b')        # format(변수, 'o,b,h') 사용 시 문자열로 변환되어도 0x, 0o, 0b 가 출력되지 않는다.
                                                # format(변수, '#0,#b,#h') 사용 시 문자열로 변환되면서 0x, 0o, 0b가 출력된다.
    while len(arr_sum[x]) < int(n):             # 입력받은 n만큼의 자리수로 맞춰주기 위해 부족한 부분은 0으로 채운다.
        arr_sum[x] = '0' + arr_sum[x]
    
    while len(arr_sum[x]) > int(n):
        arr_sum[x] = arr_sum[x][:-1]

for x in range(int(n)):                         # 변환된 2진수를 ' '(공백) 과 '#'로 변환
    arr_sum[x] = arr_sum[x].replace('0', ' ')
    arr_sum[x] = arr_sum[x].replace('1', '#')

print(arr_sum)
