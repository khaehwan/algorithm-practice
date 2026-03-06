def solution(nums):
    answer = 0
    max = len(nums)//2
    
    pokemon = dict()
    
    for num in nums:
        if num in pokemon:
            pokemon[num] += 1
        else:
            pokemon[num] = 1
    
    if len(pokemon) > max:
        answer = max
    else:
        answer = len(pokemon)
    
    return answer