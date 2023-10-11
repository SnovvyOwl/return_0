import heapq
import math
# 다익스트라

def solution(n,edge):
    dist=[math.inf]*(n+1) # 0번 배열 비워진상태로 배열 초기화
    queue=[] #queue 초기화
    graph=[[] for _ in range(n+1)] # 그래프 초기화


    for n,v in edge: # 인접리스트 표현
        graph[n].append(v)
        graph[v].append(n)
    
    heapq.heappush(queue,[0,1]) # 초기점 도입 초기 점이 1이고 거리는 0임
    q=queue
    dist[1]=0 # 초기 거리 설정 

    while q:
        d,n=heapq.heappop(q) 
        if dist[n]<d: # 만약 거리가 현재 최소거리보다 크면  그대로 진행
            continue
        for adj_vertex in graph[n]: # 현재점에 있는 인접 벌텍스
            if d+1<dist[adj_vertex]: #현재 저장된 vertex 보다  저장된 vertex까지 거리보다 클경우
                dist[adj_vertex]=d+1 #거리 업데이트
                heapq.heappush(q,[d+1,adj_vertex]) # 업데이트된 거리와, vertex를 
    answer = dist[1:].count(max(dist[1:]))

    return answer

if __name__=="__main__":
    n=6
    vertex=[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
    print(solution(n,vertex))
