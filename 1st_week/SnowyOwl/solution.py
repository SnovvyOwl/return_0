# 완주하지 못한사람 HASH
def solution(participant, completion):
    hashed=dict()
    hash_sum=0
    for people in participant:       
        hashed[hash(people)]=people  #hash 함수는 같은 스트링일경우 같은 값을 가짐 
        hash_sum+=hash(people)  

    for  people in completion:
        hash_sum-=hash(people) # 같은값일경우 같은 해시를 가지므로 빼고나서 나믄것이 실제 남는 선수가 됨 
    return hashed[hash_sum]



#피로도
from itertools import permutations
def solution(k, dungeons):
    answer = 0
    count=0
    hp=k
    kind_of_dungeons=len(dungeons)
    for permutation in permutations(dungeons,kind_of_dungeons):
        k=hp
        count=0
        for permute in permutation:
            if k>=permute[0]:

                k=k-permute[1]
                count+=1
        if count>answer:
            answer=count    
    return answer

# 가장 큰수 (RUN TIME ERRor)
from itertools import permutations
def solution(numbers):
    answer="0"
    for per in permutations(numbers):
        result = ''.join(str(s) for s in list(per))
        if answer<result:
            answer=result
    return answer


#H IDX
def solution(citations):
    citations.sort()
    for i,h in enumerate(citations):
        if h>=len(citations)-i:
            return len(citations)-i
    return 0

