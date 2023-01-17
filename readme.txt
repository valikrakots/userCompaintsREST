This is a project written during my internship. Project is a fully REST service to process users' complaints. 


To see info about project structure go to(get method):
http://127.0.0.1:8000/api - for simple user
http://127.0.0.1:8000/api/admin - for superuser(you should create superuser
and provide access token in header {Authentication : JWT (your token)})


To run locally:
    1) go to two/setting.py and set USE-DOCKER to False
    2) provide your database credentials
    3) run redis-server
    4) run database server (postgresql prefered)
    5) migrate
    6) runserver


To run in docker:
    1) stop you local redis and postgresql servers
    2) go to two/setting.py and set USE-DOCKER to True
    3) open folder in terminal and write following commands:
        - docker-compose up -d --build
        - docker-compose exec web python manage.py migrate
    NOTE: if you want to access your database type in terminal:
        - docker exec -it {your db container's name} bash
        - psql -U postgres

