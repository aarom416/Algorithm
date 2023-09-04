def solution(routes):
    routes.sort(key=lambda x:x[1]) #진출지점을 오름차순 정렬해야 진출 지점에 카메라를 달았을때 다음 차량의 진입 지점과 겹치는지 확인이 가능
    count=0
    out_location=-30001 
    for route in routes:
        if route[0]>out_location:
            count+=1
            out_location=route[1] #진출 지점 업데이트
    return count