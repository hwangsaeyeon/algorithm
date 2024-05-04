def solution(genres, plays):
    answer = []
    
    hashmap = {}
    for i in range(len(genres)) : 
        hashmap[genres[i]] = hashmap.get(genres[i], 0) + plays[i]

    genres_cnt = []
    for type in hashmap : 
        genres_cnt.append([hashmap[type], type])
    
    genres_cnt.sort(reverse=True)

    
    for _ , gen in genres_cnt : 
        count = []
        for i in range(len(genres)) : 
            if genres[i] == gen :         
                
                count.append([plays[i], -i])
        
        count.sort(reverse=True)
        
        if len(count) >= 2 : 
            answer.append(-count[0][1])
            answer.append(-count[1][1])
        else : 
            answer.append(-count[0][1])

        
    return answer