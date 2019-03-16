inputcount=0
count=0
primecount=0
i=0
j=0

inputcount = input('몇번째 소수를 출력할까요? : ')

for i in range(1,999999999999) :
    for j in range(1,i) :
        if count>2 :
            break
        if i%j==0 :
            count+=1
    if count==2 : 
        primecount+=1
    if inputcount == primecount :
        break
    count = 0

print(inputcount + "번째 소수 : " + i)
