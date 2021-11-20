# e6156-blog-service

Get all blogs:
GET http://ec2-54-84-66-191.compute-1.amazonaws.com:8000/blog/ 

Create new blog:
POST http://ec2-54-84-66-191.compute-1.amazonaws.com:8000/ 
+title/body/user_id/tag

Get blog with id:
GET http://ec2-54-84-66-191.compute-1.amazonaws.com:8000/2
(Get blog with id=2)

Put blog with id:
PUT http://ec2-54-84-66-191.compute-1.amazonaws.com:8000/2
+title/body/user_id/tag
(Put blog with id=2)

Delete blog with id:
DELETE http://ec2-54-84-66-191.compute-1.amazonaws.com:8000/2
(Delete blog with id=2)


#Connect with AWS

connect to ec2 instance:
ssh -i "hw3_t1.pem" ec2-user@ec2-54-84-66-191.compute-1.amazonaws.com

connect to rds:
mysql -h database-1.crentgyphipj.us-east-1.rds.amazonaws.com -P 3306 -u admin -p t1

upload file to ec2 instance:
scp -i ~/Desktop/"hw3_t1.pem" -r e6156-blog-service/ ec2-user@ec2-54-84-66-191.compute-1.amazonaws.com:t1/

Allow Host:
/blog/settings.py
ALLOWED_HOSTS = ['ec2-54-84-66-191.compute-1.amazonaws.com']

Add Security rule:
IPv4 Custom TCP TCP 8000 0.0.0.0/0

python3 manage.py runserver 0.0.0.0:8000


Api GateWay:
base: https://uwu5f8dejb.execute-api.us-east-1.amazonaws.com/t2/test
append ids: https://uwu5f8dejb.execute-api.us-east-1.amazonaws.com/t2/test/1

Cloud Front:
base:https://d339yyb5akm0ol.cloudfront.net/test/
append ids:https://d339yyb5akm0ol.cloudfront.net/test/1