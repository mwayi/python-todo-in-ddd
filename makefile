run: stop up
up:
	docker-compose -f docker-compose.yml up -d --build
stop:
	docker-compose -f docker-compose.yml stop
down:
	docker-compose -f docker-compose.yml down
test:
	docker-compose -f docker-compose.test.yml up --build --renew-anon-volumes --abort-on-container-exit
	docker-compose -f docker-compose.test.yml down --volumes
mysql:
	docker start todo_database
	docker exec -it todo_database mysql -utodo -proot