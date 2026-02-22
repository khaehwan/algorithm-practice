def solution(participant, completion):
    answer = ''
    
    runner = dict()
    for name in participant:
        if name in runner:
            runner[name] += 1
        else:
            runner[name] = 1
            
    for name in completion:
        runner[name] -= 1
    
    for key, value in runner.items():
        if value > 0:
            answer = key
            break;
    
    return answer
    