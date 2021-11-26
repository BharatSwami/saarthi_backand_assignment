# saarthi_backand_assignment



## Saarthi.ai backand project IIT KANPUR

start the virtual environment and use

$ pip install -r requirment.txt

to install the required modules

To start the server use

../saarthi_backand_project/project/saarthi $ python manage.py runserver 8080

this command start the django server in localhost at port 8080
if port 8080 not availble start at 8000 (default)

On going web page  http://127.0.0.1:8000/
it will show as-

![image](https://user-images.githubusercontent.com/69075767/143603449-8798be39-0dc6-4149-be6c-ac6348de824f.png)

here id represtents the id used in url request to Ice anf Fire Api as-
urls=f"https://anapioficeandfire.com/api/books/{id}"

and after submitting the form it makes a GET request to API anf get the data and store in database.
![image](https://user-images.githubusercontent.com/69075767/143486195-5f496846-7ec6-47da-a852-419d74a64d88.png)


GET: http://127.0.0.1:8000/api/v1/books
will show all the books in database

![image](https://user-images.githubusercontent.com/69075767/143604043-76ea119c-1a8d-4d90-995e-4bea38b2dac4.png)


then to GET, POST, DELETE, the data use following urls:
GET: http://127.0.0.1:8000/api/v1/books/:4 
![image](https://user-images.githubusercontent.com/69075767/143603659-a4e68f3b-8acd-4674-b5cb-85428e5acfe6.png)

POST: http://127.0.0.1:8000/api/v1/books/:5 or GET http://127.0.0.1:8000/api/v1/books/:5/update
if id exists in database
![image](https://user-images.githubusercontent.com/69075767/143604121-7c2c0c69-7d04-4f58-bb0f-b19cd9fc8210.png)

if id doesn't exist
![image](https://user-images.githubusercontent.com/69075767/143604270-ad4346bd-0a2b-4eae-a794-9083f229d914.png)



DELETE: http://127.0.0.1:8000/api/v1/books/:4 or GET http://127.0.0.1:8000/api/v1/books/:5/delete
![image](https://user-images.githubusercontent.com/69075767/143603855-dd99526e-32c9-4641-9c79-7c4a9105e1e1.png)

id book doesn't exist with given id
![image](https://user-images.githubusercontent.com/69075767/143604455-607c9a5f-067f-4151-a7a0-ce7df530cb69.png)


requesting data with name of book ,publisher of book or country 

http://127.0.0.1:8000/api/
![image](https://user-images.githubusercontent.com/69075767/143605100-66faff22-79a9-450e-b3bc-136a8cda7a61.png)

http://127.0.0.1:8000/api/external-books/
![image](https://user-images.githubusercontent.com/69075767/143605155-754582af-a2ce-4d5d-bcb5-90d3c8fcf354.png)

by name:
http://127.0.0.1:8000/api/external-books/name  or http://127.0.0.1:8000/api/v1/books?name:=A%20Game%20of%20Thrones
![image](https://user-images.githubusercontent.com/69075767/143605233-dfe9889d-dc96-44a4-86dd-68cd2eb9f68f.png)
![image](https://user-images.githubusercontent.com/69075767/143605279-f5cb485f-86de-45ce-97b2-ff47d63f4178.png)

by country:
http://127.0.0.1:8000/api/external-books/country or http://127.0.0.1:8000/api/v1/books?country:=United%20States
![image](https://user-images.githubusercontent.com/69075767/143605387-28c0d4d1-b3bb-45c1-99d5-5752360d8775.png)
![image](https://user-images.githubusercontent.com/69075767/143605427-53559f35-8496-44a9-98c6-0809b1cce8e4.png)

by publisher:
http://127.0.0.1:8000/api/external-books/publisher or http://127.0.0.1:8000/api/v1/books?publisher:=Bantam%20Books
![image](https://user-images.githubusercontent.com/69075767/143605490-9576f654-dfc1-41f4-877b-26f0f42d8ba6.png)
![image](https://user-images.githubusercontent.com/69075767/143605553-b0e65afc-8ce8-46ce-ac15-64c87e85d0c9.png)






