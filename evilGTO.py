
# coding: utf-8

# In[2]:

import time
start_time = time.time()
file=open("output")
wlist = file.read().splitlines()
file.close()

#listok=[]

scoreposs=[]
amtletters=5
'''for i in range(0,amtletters+1):
    for j in range(0,amtletters+1-i):
        if i!=1 or j!=amtletters-1:
            scoreposs.append([i,j])'''

for i in range(0,2*amtletters-1):
    scoreposs.append([i])

#print (scoreposs)
'''
scoreposs=[
    [0,0],[1,0],[2,0],[3,0],[4,0],[0,1],[0,2],[0,3],
    [1,1],[1,2],[2,1]
]'''
minscore=len(wlist)
minword=""
for trial in wlist:
    maxscore=0
    for poss in scoreposs:
        hint=[]
        hint.append(trial)
        hint.extend(poss)
        
        #print(hint) #uncomment for debuggin!
        
        count=0
        
        for word in wlist:
            plus1=0
            plus2=0
            unusedindexes=range(0,len(hint[0]))
            '''for i in range(0,len(hint[0])):

                if word[i]==hint[0][i]:
                    plus2+=1
                    try:
                        unusedindexes.remove(i)
                    except ValueError:
                        pass
                else:
                    for j in range(0,len(hint[0])):
                        if word[i]==hint[0][j] and j in unusedindexes:
                            plus1+=1
                            unusedindexes.remove(j)
                            break'''
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
                            
            
            #if plus1!=int(hint[1]) or plus2!=int(hint[2]):
            if plus1+2*plus2!=int(hint[1]):
                pass        
            else:
                count+=1
        
        
        #print(count)
        if count>maxscore:
            maxscore=count
        
        if count>=minscore:
            #print(minscore)
            break
            
    #print(maxscore) #uncomment for debuggin
    if maxscore<minscore:
        minscore=maxscore
        minword=trial
        #print(minscore)
        #listok.append(word)
            
#print (listok)
#print (len(listok))
print(minscore)
print(minword)
print("--- %s seconds ---" % (time.time() - start_time))


# In[ ]:




# In[ ]:



