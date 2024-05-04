def solution(clothes):
    # 각 종류별 가진 의상을 저장 (종류:[이름, 이름, ...])
    hashmap = {}
    for name, type in clothes : 
        hashmap[type] = hashmap.get(type,0) + 1 
    ans = 1 
    for type in hashmap:
        ans *= ( hashmap[type] + 1 ) 
    
    return ans -1 
        