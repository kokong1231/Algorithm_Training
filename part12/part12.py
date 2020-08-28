def solution(participant, completion):
    a = ''
    answer = ''

    try:
        for x in participant:
            a = x
            completion.index(x)
        
    except:
        answer += a
    
    return answer