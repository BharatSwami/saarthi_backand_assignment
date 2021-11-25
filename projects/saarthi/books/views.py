from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
import sys
import json
import re
from django.http import HttpResponse, JsonResponse
# Create your vi
# ews here.
from django.shortcuts import render
from .models import table

def allData(soup1):
    data={
        'name':soup1['name'],
        'isbn':soup1['isbn'],
        'authors':soup1['authors'],
        'numberOfPages':soup1['numberOfPages'],
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
        dit={'id':data.id,
            "name": data.name,
    "isbn" : data.isbn,
    "authors" : data.authors,
    "country" : data.country,
    "numberOfPages":data.numberOfPages,
    "publisher":data.publisher,
    "release_date":data.release_date
        }
        json_data["data"].append(dit)
    return json_data

def represtingInJson3(record):
    #alldata= table.objects.all()

    json_data={"status_code":200,
            "status":"success",
            "data":[]
    }

    alldata=record
    #print(allData.id)
    try:
        for data in alldata:
            dit={'id':data.id,
                "name": data.name,
        "isbn" : data.isbn,
        "authors" : data.authors,
        "country" : data.country,
        "numberOfPages":data.numberOfPages,
        "publisher":data.publisher,
        "release_date":data.release_date
            }
            json_data["data"].append(dit)
    except:
        pass
    return json_data

def represtingInJson1(record):
    #alldata= table.objects.all()

    json_data={"status_code":200,
            "status":"success",
            "data":[]
    }

    data=record
    try:
        dit={'id':data.id,
                "name": data.name,
        "isbn" : data.isbn,
        "authors" : data.authors,
        "country" : data.country,
        "numberOfPages":data.numberOfPages,
        "publisher":data.publisher,
        "release_date":data.release_date
            }
        json_data["data"].append(dit)
    except:
        pass
    return json_data


def updateTable(soup1):
    post=table()
    #post.id=soup1['id']
    post.name= soup1['name']
    post.isbn = soup1['isbn']
    post.authors = soup1['authors']
    post.country = soup1['country']
    post.numberOfPages=soup1['numberOfPages']
    post.publisher=soup1['publisher']
    post.release_date=soup1['released']
    post.save()
    return
    #allvideos= table.objects.all()
    #return render(request,'result.html',{'soup':allvideos})
def updateTablesecond(request):
    try:
        id=request.POST['id']
        #post=table(id=id)
        print("heha")
        post=table(id=id)
        post.name =request.POST['name']
        post.isbn =request.POST['isbn']
        post.authors = request.POST['authors']
        post.country= request.POST['country']
        post.numberOfPages=request.POST['numberOfPages']
        post.publisher=request.POST['publisher']
        post.release_date=request.POST['release_date']
        
        post.save()
    except:
        id=request.GET['id']
        #post=table(id=id)
        print("heha")
        post=table(id=id)
        post.name =request.GET['name']
        post.isbn =request.GET['isbn']
        post.authors = request.GET['authors']
        post.country= request.GET['country']
        post.numberOfPages=request.GET['numberOfPages']
        post.publisher=request.GET['publisher']
        post.release_date=request.GET['release_date']
        
        post.save()


    allvideos= table.objects.all()
    return render(request,'result.html',{'soup':allvideos})


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
        soup1=apiData(num1)
        #del soup1['characters']
        #print(soup)
        updateTable(soup1)
        allvideos= table.objects.all()
        json_data=represtingInJson()
        #return render(request,'result.html',{'soup':json_data})
        #return render(request,'result.html',{'soup':soup1})
        json_pretty = json.dumps(json_data,default=lambda o: o.__dict__,sort_keys=False,  indent=9)
        return HttpResponse(json_pretty,content_type="application/json")

def books(request):

    if request.method == 'GET':
        #print(soup)
        json_data=represtingInJson()
        context= {'soup': allData}
        
        json_pretty = json.dumps(json_data,default=lambda o: o.__dict__,sort_keys=False,  indent=9)
        return HttpResponse(json_pretty,content_type="application/json")

    #return HttpResponse("heh")

    elif request.method == 'POST':
        return render(request,'form.html')
        """num1=request.POST['num1']    
        soup1=apiData(num1)
        updateTable(soup1)
        #del soup1['characters']
        
        allvideos= table.objects.all()

        return render(request,'result.html',{'soup':allvideos})"""

    elif request.method == 'DELETE':
        url=request.get_full_path()
        try:
            id=int(url.split('/')[-2][1:])
        except:
            id=url.split('/')[-1][1:]
        try:
            record = table.objects.get(id=int(id))
            record.delete()
        except:
            record=[]
        json_data=represtingInJson1(record)
        #return render(request,'json.html',{'soup':json_data})
        json_pretty = json.dumps(json_data,default=lambda o: o.__dict__,sort_keys=False,  indent=9)
        return HttpResponse(json_pretty,content_type="application/json")

    elif request.method == 'SHOW':
        pass
    else:
        pass
    
def update(request):
    url=request.get_full_path()
    try:
        id=int(url.split('/')[-2][1:])
    except:
        id=url.split('/')[-1][1:]
    #record = table.objects.get(id=int(id))
    try:
        record = table.objects.get(id=int(id))
        #updateTable(record)
        return render(request,'form.html')
        #allvideos= table.objects.all()
    except:
        allData= table.objects.all()
    json_data=represtingInJson3(allData)
    #return render(request,'result.html',{'soup':allvideos})
    json_pretty = json.dumps(json_data,default=lambda o: o.__dict__,sort_keys=False,  indent=9)
    return HttpResponse(json_pretty,content_type="application/json")

def deleteding(request):
    url=request.get_full_path()
    try:
        id=int(url.split('/')[-2][1:])
    except:
        id=url.split('/')[-1][1:]
    try:
        record = table.objects.get(id=int(id))
        record.delete()
    except:
        record=[]
    json_data=represtingInJson1(record)
    #return render(request,'json.html',{'soup':json_data})
    json_pretty = json.dumps(json_data,default=lambda o: o.__dict__,sort_keys=False,  indent=9)
    return HttpResponse(json_pretty,content_type="application/json")

def getdata(request):
    url=request.get_full_path()
    id=url.split('/')[-1][1:]
    print(id)
    try:
        record = table.objects.get(id=id)
    except:
        record=[]
    #record.delete()
    #print(record.id)

    json_data=represtingInJson1(record)
    #return render(request,'json.html',{'soup':json_data})
    #json_data = json_data.json()
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

    #name=request.GET['name'][1:]
    #print(name)
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
                posts=['heha']
    print(posts)
    json_data=represtingInJson3(posts)
    json_pretty = json.dumps(json_data,default=lambda o: o.__dict__,sort_keys=False,  indent=9)
    return HttpResponse(json_pretty,content_type="application/json")

def external_books(request):

    return render(request,'external-books.html')

def api_options(request):

    return render(request,'api_options.html')

def search_options(request):
    return HttpResponse("hehah")