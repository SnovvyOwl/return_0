# # 기능개발
# def solution(progresses, speeds):
#     answer = []
#     cnt=0
#     while progresses:
#         progresses=[ai + bi for ai, bi in zip(progresses, speeds)]
#         while progresses[0]>=100:
#             del progresses[0]
#             del speeds[0]
#             cnt=cnt+1
#             if not progresses :
#                 answer.append(cnt)
#                 break
#             else:
#                 if progresses[0]<100:
#                     answer.append(cnt)
#                     cnt=0

#     return answer

# 디스크 컨트롤러
import heapq
def solution(jobs):
    answer, now, i = 0, 0, 0
    start = -1 
    heap = []
    
    while i < len(jobs):
        # 현재 시점에서 처리할 수 있는 작업을 heap에 저장
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]]) #힙으로 저장 (필요시간, 요청시간 )
        
        if len(heap) > 0: # 처리할 작업이 있는 경우
            work = heapq.heappop(heap) #같은 시간의경우 작업 시간이 적은거 부터 뽑아냄
            start = now # 시간이 변경됨
            now += work[0] # Now에서 작업이 요청된 시간을 더함 -> 더
            answer += now - work[1] # 작업 요청시간부터 종료시간까지의 시간 계산
            i +=1
        else: # 처리할 작업이 없는 경우 다음 시간을 넘어감
            now += 1
                
    return answer // len(jobs)


print(solution([[0, 3], [1, 9], [2, 6]]))