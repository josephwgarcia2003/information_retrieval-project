import json
from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

nltk.download("stopwords")
nltk.download('punkt_tab')

with open('ksu1000.json', 'r', errors="ignore") as f:
    data = json.load(f)

words =Counter()

englishStopwords = set(stopwords.words("english"))
 


for page in data:
    pagebody=page['body']
    #remove punctuation
    removedPuncts = pagebody.translate(str.maketrans("","",string.punctuation))
    #tokenized
    wordTokens = word_tokenize(removedPuncts)
    #cleaned word list
    cleanedWordlist = [i for i in wordTokens if not i.lower() in englishStopwords]
    words= words+Counter([word.lower() for word in cleanedWordlist])



#print(words)
total = sum(words.values())

words= words.most_common(30)


#wf= open("WordsbeforeCleanup.txt","x") #Creates txt file


print("Rank      Term                 Freq            Percent")
print("--------------------------------------------------------")

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

