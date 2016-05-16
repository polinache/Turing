rules = open('4.txt', 'r')
line = input()
oldstate = [0]*24
newstate = [0]*24
oldsymbol = [0]*24
newsymbol = [0]*24
direction = [0]*24
s=rules.readline()
i=0
while len(s)!=0:
    A = s.split(' ')
    oldsymbol[i] = A[0]
    oldstate[i] = A[1]
    newsymbol[i] = A[3]
    newstate[i] = A[4]
    direction[i] = A[5]
    s=rules.readline()
    i+=1
q='q1'
output=[0]*6
for j in range(len(line)):
    if (q=='q1') or (q=='q2') or (q=='q3') or (q=='q4') or (q=='q5'):
        for i in range(len(output)):
            if oldsymbol[i]==line[j] and oldstate[i]==q:
                q = newstate[i]
                output[i] = newsymbol[i]
    elif q =='no':
        print(list(output))
        break
print(output)

    Status API Training Shop Blog About 

