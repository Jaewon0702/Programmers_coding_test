def solution(numbers) :
    biggest=''
    sorted_v=[]
    sorted_v = sorted([ str(v) * 3 for v in numbers ], reverse=True)
    for v in sorted_v :
        biggest+=v[:int(len(v)/3)]
    if biggest[0]=='0' :
        return '0'

    return biggest
#kdlelk99님의 코드를 참고하였다. 6줄을 좀 더 간단한 코드로 줄였다.
#100점

            
        
        


    
            

    
            
        
