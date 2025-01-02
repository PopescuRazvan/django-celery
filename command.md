pip freeze > requirements.txt
chmod +x ./entrypoint.sh
docker-compose up -d --build
./manage.py startapp taskapp
docker exec -it django /bin/sh

#on server
/usr/local/bin/python3 manage.py startapp cworker
/usr/local/bin/python3 manage.py shell

#remove all docker
docker ps -aq | ForEach-Object { docker stop $_; docker rm $_ }
docker images -aq | ForEach-Object { docker rmi $_ }


