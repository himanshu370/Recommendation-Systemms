To Get Embedding database:-

<br/> steps:-
<br/>1.) Install docker on your system from docker official if not present:-
<br/>2.) Git Clone this repo
<br/>3.) Put your images in the image folder for which you want to add embeddings in your database.
<br/>4.) run this -> "sudo docker build -f Dockerfile --no-cache -t test ."
<br/>5.) run this -> " sudo docker run -ti test /bin/bash " and then exit.
<br/>6.) Check the current latest container ID with "sudo docker ps -a" and copy the topmost id 
<br/>7.) run this -> "sudo docker cp {container ID}:/main_database main_database " and then "sudo docker cp {container ID}:/topwear_database topwear_database" and 
"sudo docker cp {container ID}:/bottomwear_database bottomwear_database " 


<br/> The new databases for embeddings of the image into are saved into:- 
<br/> Topwear_database(topwear object detection and it's embedding) 
<br/> Bottomwear_database (Bottomwear object detection and it's embedding) 
<br/> main_database(embedding of whole look)
 
 
To get Required similar clothing details:-
<br/>steps:-
<br/>1.) git clone the repo ans and move to image_similarity directory
<br/>2.) run uvicorn app:app --reload for api
<br/>3.) use localhost/image_id/k for getting k recommended fashion clothes for cloth_id/image_id



To get top k recommended topwears and  Bottomwears:-
<br/> run uvicorn app1:app --reload 


<br/>
For using API for embedding generation of image in Database:-
<br/> 1.) git clone and move into Embedding folder
<br/> 2.) Edit database.py with the image url yu have and id you want to give
<br.> 2.) RUN "uvicorn database_app:app --reload" and the embedding will be saved into database
