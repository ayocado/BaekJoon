import sys, heapq

N = int(sys.stdin.readline())
classes = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
classes.sort()

rooms = []
heapq.heappush(rooms, classes[0][1])

for i in range(1, N):
    if classes[i][0] < rooms[0]: # 현재 회의실 끝나는 시간보다 다음 회의 시작시간이 빠르면
        heapq.heappush(rooms, classes[i][1]) # 새로운 회의실 개설
    else: # 현재 회의실에 이어서 회의 개최 가능
        heapq.heappop(rooms) # 새로운 회의로 시간 변경을 위해 pop후 새 시간 push
        heapq.heappush(rooms, classes[i][1])

print(len(rooms))