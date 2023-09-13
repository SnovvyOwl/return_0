# 기능개발
def solution(progresses, speeds):
    answer = []
    cnt=0
    while progresses:
        progresses=[ai + bi for ai, bi in zip(progresses, speeds)]
        while progresses[0]>=100:
            del progresses[0]
            del speeds[0]
            cnt=cnt+1
            if not progresses :
                answer.append(cnt)
                break
            else:
                if progresses[0]<100:
                    answer.append(cnt)
                    cnt=0

    return answer

#디스크 컨트롤러
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
            now += work[0] # 현재 부터 작업종료 시점 계산
            answer += now - work[1] # 현재 시점의 종료시간에서 요청시간 빼서 요청부터 종료시간을 계산
            i +=1
        else: # 처리할 작업이 없는 경우 다음 시간을 넘어감
            now += 1
                
    return answer // len(jobs)

# 맵최단거리 runtime err..
import queue
def solution(maps):
    row=len(maps)
    col=len(maps[0])

    def bfs(maps):
        cnt=1
        que=queue.Queue()
        que.put([row-1,col-1,cnt])
        maps[row-1][col-1]=0
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]

        while queue:
            x, y, cnt = que.get()
        
            for i in range(4):
                nx = x + dx[i] 
                ny = y + dy[i]
                # 4가지 이동방향
                if nx == 0 and ny == 0:
                    return cnt + 1
                if 0 <= nx < row and 0 <= ny < col:
                    if maps[nx][ny] != 0:
                        maps[nx][ny] = 0
                        que.put([nx, ny, cnt+1])

        return -1
    
    if len(maps)==1 and len(maps[0]) == 1:
        return 1
    return bfs(maps)
    