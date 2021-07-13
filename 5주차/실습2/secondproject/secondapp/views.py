from django.shortcuts import render

# Create your views here.
def wordcount(request):
    return render(request,"wordcount.html")

def result(request):
    sentence=request.GET['sentence'] 
    #wordcount.html에서의 textarea값을 가져옴

    wordList=sentence.split()

    wordDict={}

    for word in wordList:
        if word in wordDict:
            wordDict[word]+=1
        else:
            wordDict[word]=1

    return render(request,'result.html',{'fulltext':sentence,'count':len(wordList),'wordDict':wordDict.items})