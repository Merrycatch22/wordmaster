import time
start_time = time.time()

wlist = open("words5").read().splitlines()
hintlines=open("hints").read().splitlines()
hintlist=[]
for line in hintlines:
    hintlist.append(line.split(','))
#wlist=["twelve"]
#hintlist=[["golden",0,2]]
listok=[]
for word in wlist:
    flag=True
    for hint in hintlist:
        plus1=0
        plus2=0
        unusedindexes=range(0,len(hint[0]))
        doublelooper=range(0,len(hint[0]))
        for i in range(0,len(hint[0])):
            if word[i]==hint[0][i]:
                plus2+=1
                try:
                    unusedindexes.remove(i)
                    doublelooper.remove(i)
                except ValueError:
                    pass
        for i in doublelooper:
            #else:
                for j in range(0,len(hint[0])):
                    if word[i]==hint[0][j] and j in unusedindexes:
                        plus1+=1
                        unusedindexes.remove(j)
                        break
        #print(plus1,plus2)                
        if plus1!=int(hint[1]) or plus2!=int(hint[2]):
            flag=False
            break
    if flag:
        listok.append(word)

print (len(listok))        
print (listok)


output=open('output','w')
for word in listok:
    output.write(word+"\n")
output.close()

print("--- %s seconds ---" % (time.time() - start_time))