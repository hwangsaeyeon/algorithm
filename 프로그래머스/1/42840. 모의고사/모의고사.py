def solution(answers):
    answer = []
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    
    scores = [0,0,0]
    score_one, score_two, score_three = 0, 0, 0 
    
    for i in range(len(answers)) : 
        if answers[i] == one[i%len(one)] : 
            scores[0] += 1 
        
        if answers[i] == two[i%len(two)] : 
            scores[1] += 1
        
        if answers[i] == three[i%len(three)] : 
            scores[2] += 1 
    
    for i in range(len(scores)) : 
        if max(scores) == scores[i] :
            answer.append(i+1)
            
    return answer