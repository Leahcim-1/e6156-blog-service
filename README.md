# e6156-blog-service

Get all blogs:
GET http://127.0.0.1:8000/blog/ 

Create new blog:
POST http://127.0.0.1:8000/blog/ 
+title/body/user_id/tag

Get blog with id:
GET http://127.0.0.1:8000/blog/2
(Get blog with id=2)

Put blog with id:
PUT http://127.0.0.1:8000/blog/2
+title/body/user_id/tag
(Put blog with id=2)

Delete blog with id:
DELETE http://127.0.0.1:8000/blog/2
(Delete blog with id=2)


#Connect with AWS

connect to ec2 instance:
ssh -i "hw3_t1.pem" ec2-user@ec2-54-84-66-191.compute-1.amazonaws.com

connect to rds:
yuanboli$ mysql -h database-1.crentgyphipj.us-east-1.rds.amazonaws.com -P 3306 -u admin -p t1

upload file to ec2 instance:
scp -i ~/Desktop/"hw3_t1.pem" -r e6156-blog-service/ ec2-user@ec2-54-84-66-191.compute-1.amazonaws.com:t1/
