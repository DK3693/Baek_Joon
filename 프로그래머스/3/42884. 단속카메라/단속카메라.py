def solution(routes):
    cameras=[]
    routes.sort(key=lambda x: x[1])
    cameras.append(routes[0][1])
    for route in routes:
        result = True
        for camera in cameras:
            if route[0] <= camera <= route[1]:
                result = False
                break
        if result:
            cameras.append(route[1])
    answer = len(cameras)
    return answer