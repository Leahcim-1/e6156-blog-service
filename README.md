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