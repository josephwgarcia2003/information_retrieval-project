import json
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

with open('ksu1000.json', 'r', errors="ignore") as f:
    data = json.load(f)

words =Counter()
for page in data:
    pagebody=page['body']
    words= words+Counter(pagebody.split())

#print(words)
total = sum(words.values())

allwords=words

words= words.most_common(30)


#wf= open("WordsbeforeCleanup.txt","x") #Creates txt file


print("Rank      Term                 Freq            Percent")
print("--------------------------------------------------------")
#wf.write("Rank      Term                 Freq            Percent\n")
#wf.write("--------------------------------------------------------\n")

index=1
top30count=0
percentagesum=0
for element,count in words:
    percentage=(count/total)*100
    row= f"{index}         {element:10s}           {count}             %{round(percentage,2)}"
    print(row)
    #wf.write(row+"\n")
    #top30count+=count #Counts the occurences of each word 
    #percentagesum+=percentage #Keeps track of percentage of the top 30 
    index+=1

differentwords=len(allwords)

freq= sorted(allwords.values(), reverse=True)
ranks = np.arange(1, differentwords + 1)


plt.plot(ranks, freq)   #'ro'

plt.xlabel("Rank")
plt.ylabel("Frequency")
plt.title("Word Distribution")

plt.show()


##Loglog Plot
plt.loglog(ranks, freq)   

plt.xlabel("Rank")
plt.ylabel("Log Occurences")
plt.title("Word Frequency before Cleanup")

plt.show()


