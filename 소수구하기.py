inputcount=0                                            #사용자가 입력한 숫자를 저장할 변수
count=0                                                 #약수의 개수를 카운팅할 변수
primecount=0                                            #inputcount까지의 소수개수를 카운팅할 변수
i=0                                                     #for문과 출력에 쓰일 변수
j=0                                                     #for문에 쓰일 변수    

inputcount = input('몇번째 소수를 출력할까요? : ')        #입력받은값 inputcount에 저장
for i in range(1,9999999999,1) :                        #main for문 시작
    for j in range(1,i,1) :                             #약수개수 counting for문 시작                                    
        if count>2 :                                    #약수개수가 2개를 넘으면 break
            break                                       
        if i%j==0 :                                     #j로 나누어 떨어지는 i값이 있으면 i의 약수개수 1 증가                                                                                       
            count=count+1
    if count==2 :                                       #counting for문에서 count가 2로 나왔을경우 소수로 판단하여   
        primecount=primecount+1                         #primecount를 1증가
if inputcount == primecount :                           #inputcount 값과 primecount값이 같아지면 main for 문 탈출
    break
    count = 0                                           #count 초기화 한후 main for 문 반복                                         
 
print(inputcount,"번째 소수 : ",i)                      #결과값 출력
