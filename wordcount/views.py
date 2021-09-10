from django.http import HttpResponse
from django.shortcuts import render, resolve_url
import operator

def home(request):
    # return HttpResponse('Hello')
    # return render(request,'home.html',{'hithere':'This is me'})
    return render(request,'home.html')

def eggs(request):
    # return HttpResponse('eggs are great')
    return HttpResponse('<h1>Eggs</h1>')

def count(request):
    fulltext=request.GET['fulltext']
    # print(fulltext)
    wordlist=fulltext.split()
    worddictionary={}

    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1
    
    sorteddict=sorted(worddictionary.items(),key=operator.itemgetter(1),reverse=True)

    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'sorteddict':sorteddict})

def about(request):
    return HttpResponse('This is the website for counting the words')