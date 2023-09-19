def solution(n, times):
    min_time,max_time=0, max(times)*n
    while min_time<=max_time:
        mid=(min_time+max_time)//2 # 중간 시간 찾기
        people=0
        for time in times:
            people+=mid//time # 중간시간에 찾은 사람명수 구하기
            if people>=n:
                break
        if people>=n: #다함 
            answer=mid
            max_time=mid-1
        elif people<n: #아직 다못함
            min_time=mid+1
    
    return answer



#ERROR
def solution(people, limit):
    people.sort()
    answer=0
    shiped=0
    for p in people:
        shiped+=p
        if shiped>limit:
            answer+=1
            shiped=p
        elif shiped==limit:
            answer+=1
            shiped=0
        elif p==people[-1] and shiped:
            answer+=1
    return answer


if __name__=="__main__":
    print(solution([50,70,80,50],100))