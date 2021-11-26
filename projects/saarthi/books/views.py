from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
import sys
import json
import re
from django.http import HttpResponse, JsonResponse,HttpResponseRedirect

from collections import OrderedDict
from django.shortcuts import render
from .models import table
import socket

def hostname():
    try:
        HOSTNAME = socket.gethostname()
    except:
        HOSTNAME = 'localhost'
    return HOSTNAME


def allData(soup1):
    data={
        'name':soup1['name'],
        'isbn':soup1['isbn'],
        'authors':soup1['authors'],
        'numberOfPages':int(soup1['numberOfPages']),
        'publisher':soup1['publisher'],
        'country' : soup1['country'],
        'date':soup1['released']
        }
    return data


def represtingInJson():
    alldata= table.objects.all()

    json_data={"status_code":200,
            "status":"success",
            "data":[]
    }

    for data in alldata:
        dit={'id':int(data.id),
            "name": data.name,
    "isbn" : data.isbn,
    "authors" : data.authors,
    "numberOfPages":int(data.numberOfPages),
    "publisher":data.publisher,
    "country" : data.country,
    "release_date":data.release_date
        }
        json_data["data"].append(dit)
    return json_data

def represtingInJson3(record,dit=OrderedDict()):
    json_data=dit
    json_data["status_code"]=200
    json_data["status"]="success"
    json_data["data"]=[]

    alldata=record
    try:
        for data in alldata:
            dit={'id':int(data.id),
            "name": data.name,
    "isbn" : data.isbn,
    "authors" : data.authors,
    "numberOfPages":int(data.numberOfPages),
    "publisher":data.publisher,
    "country" : data.country,
    "release_date":data.release_date
            }
            json_data["data"].append(dit)
    except:
        pass
    return json_data

def represtingInJson1(record,dit=OrderedDict()):

    json_data=dit
    json_data["status_code"]=200
    json_data["status"]="success"
    json_data["data"]=[]

    data=record
    try:
        dit={'id':int(data.id),
            "name": data.name,
    "isbn" : data.isbn,
    "authors" : data.authors,
    "numberOfPages":int(data.numberOfPages),
    "publisher":data.publisher,
    "country" : data.country,
    "release_date":data.release_date
            }
        json_data["data"].append(dit)
    except:
        pass
    return json_data


def updateTable(soup1):
    post=table()
    post.name= soup1['name']
    post.isbn = soup1['isbn']
    post.authors = soup1['authors']
    post.country = soup1['country']
    post.numberOfPages=int(soup1['numberOfPages'])
    post.publisher=soup1['publisher']
    post.release_date=soup1['released']
    post.save()
    return
def updateTablesecond(request):
    
    id=request.POST['id']

    print("heha")
    post=table(id=id)
    post.name =request.POST['name']
    post.isbn =request.POST['isbn']
    post.authors = request.POST['authors']
    post.country= request.POST['country']
    post.numberOfPages=int(request.POST['numberOfPages'])
    post.publisher=request.POST['publisher']
    post.release_date=request.POST['release_date']
    
    post.save()


    allvideos= table(id=int(id))
    json_data=represtingInJson1(allvideos,dit=OrderedDict({"message":f"The book {post.name} was updated successfully"}))
    json_pretty = json.dumps(json_data,default=lambda o: o.__dict__,sort_keys=False,  indent=9)
    host = request.build_absolute_uri('/')
    url=f'{host}api/v1/books/:{id}'
    return HttpResponseRedirect(url)


def apiData(id):    
    headers = {'User-Agent': 'Mozilla/5.0'}
    urls=f"https://anapioficeandfire.com/api/books/{id}"

    r = requests.get(urls, headers=headers)
    soup1 = json.loads(r.content)
    #del soup1['characters']
    return soup1

def home(request):
    return render(request,'help.html')

def api(request):

    if request.method == 'POST':
        num1=request.POST['num1']
        try:
            soup1=apiData(num1)
            updateTable(soup1)
            allvideos= table.objects.all()
            json_data=represtingInJson()

            json_pretty = json.dumps(json_data,default=lambda o: o.__dict__,sort_keys=False,  indent=9)
            return HttpResponse(json_pretty,content_type="application/json")

        except:
            return HttpResponse(f"API call fail due to no book at given id: {num1} or \
            <a href ='https://anapioficeandfire.com/api/books/{num1}'>https://anapioficeandfire.com/api/books/{num1}</a> <br> \
                Post the data at id: {num1} at \
                   <a href ='https://anapioficeandfire.com/api/books/{num1}'>https://anapioficeandfire.com/api/books/{num1}</a> ")

        

def books(request):

    if request.method == 'GET':
        #print(soup)
        json_data=represtingInJson()
        context= {'soup': allData}
        
        json_pretty = json.dumps(json_data,default=lambda o: o.__dict__,sort_keys=False,  indent=9)
        return HttpResponse(json_pretty,content_type="application/json")


    elif request.method == 'POST':
        return render(request,'form.html')


    elif request.method == 'DELETE':
        url=request.get_full_path()
        try:
            id=int(url.split('/')[-2][1:])
        except:
            id=int(url.split('/')[-1][1:])
        try:
            record = table.objects.get(id=int(id))
            book_message = f"The book {table.name} was deleted successfully"
            record.delete()
        except:
            record=[]
            book_message = "No book with given id: {id}"
        record=[]
        json_data=represtingInJson1(record,dit=OrderedDict({"message":book_message}))
        json_pretty = json.dumps(json_data,default=lambda o: o.__dict__,sort_keys=False,  indent=9)
        return HttpResponse(json_pretty,content_type="application/json")

    elif request.method == 'SHOW':
        pass
    else:
        pass
    
def update(request):
    #print("heha")
    url=request.get_full_path()
    try:
        id=int(url.split('/')[-2][1:])
    except:
        id=int(url.split('/')[-1][1:])
    try:
        record = table.objects.get(id=id)
        return render(request,'form.html',{"heha_id":id})
    except:
        allData= table(id=id)
    json_data=represtingInJson3(allData,dit=OrderedDict({"Id not found":f'{id}'}))
    json_pretty = json.dumps(json_data,default=lambda o: o.__dict__,sort_keys=False,  indent=9)
    return HttpResponse(json_pretty,content_type="application/json")

def deleteding(request):
    url=request.get_full_path()
    try:
        id=int(url.split('/')[-2][1:])
    except:
        id=int(url.split('/')[-1][1:])
    try:
            record = table.objects.get(id=int(id))
            book_message = f"The book {record.name} was deleted successfully"
            record.delete()
    except:
            record=[]
            book_message = f"No book with given id: {id}"
    record=[]
    json_data=represtingInJson1(record,dit=OrderedDict({"message":book_message}))
    json_pretty = json.dumps(json_data,default=lambda o: o.__dict__,sort_keys=False,  indent=9)
    return HttpResponse(json_pretty,content_type="application/json")

def getdata(request):
    url=request.get_full_path()
    id=int(url.split('/')[-1][1:])
    print(id)
    try:
        record = table.objects.get(id=id)
    except:
        record=[]

    json_data=represtingInJson1(record)
    json_pretty = json.dumps(json_data,default=lambda o: o.__dict__,sort_keys=False,  indent=9)
    return HttpResponse(json_pretty,content_type="application/json")

def process(request):

    if request.method=="GET":
        return getdata(request)
    elif request.method=="PATCH":
        return update(request)
    elif request.method=="DELETE":
        return deleteding(request)

    else:
        return HttpResponse("Heeee")

def finding(request):
    try:
        name=request.GET['name'][1:]
        posts=table.objects.filter(name__icontains=name)
    except:
        try:
            name=request.GET['country'][1:]
            posts=table.objects.filter(country__icontains=name)
        except:
            try:
                name=request.GET['publisher'][1:]
                posts=table.objects.filter(publisher__icontains=name)
            except:
                name=[]
                posts=['heha']
    print(name)
    json_data=represtingInJson3(posts)
    json_pretty = json.dumps(json_data,default=lambda o: o.__dict__,sort_keys=False,  indent=9)
    return HttpResponse(json_pretty,content_type="application/json")

def external_books(request):

    return render(request,'external-books.html')

def api_options(request):

    return render(request,'api_options.html')

def search_options(request):
    return render(request,'books.html')

def namefinding(request):
    return render(request,'name.html')

def findbyName(request):
    name=request.POST['num1']
    host = request.build_absolute_uri('/')
    url=f'{host}api/v1/books?name:={name}'
    return HttpResponseRedirect(url)

def countryfinding(request):
    return render(request,'country.html')

def findbyCountry(request):
    country=request.POST['num1']
    host = request.build_absolute_uri('/')
    url=f'{host}api/v1/books?country:={country}'
    return HttpResponseRedirect(url)

def publisherfinding(request):
    return render(request,'publisher.html')

def findbyPublisher(request):
    publisher=request.POST['num1']
    host = request.build_absolute_uri('/')
    url=f'{host}api/v1/books?publisher:={publisher}'
    return HttpResponseRedirect(url)


