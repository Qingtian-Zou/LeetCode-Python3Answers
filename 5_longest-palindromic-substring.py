s='cbbd'

result=[]
for i in reversed(range(1,len(s)+1)):
    for ii in range(len(s)-i+1):
        sub=s[ii:ii+i]
        if sub==sub[::-1]:
            print(sub)
