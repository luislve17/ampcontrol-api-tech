docker-up-dev:
	docker-compose -f docker-compose.yml up

docker-up-rebuild-dev:
	docker-compose -f docker-compose.yml up --force-recreate --build

docker-rebuild-dev:
	docker-compose -f docker-compose.yml build --no-cache $(resource)

docker-restart-component:
	docker restart $(resource)