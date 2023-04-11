mysql: ## start mysql
	docker compose up -d mysql

stop-mysql: ## stop mysql
	docker compose stop mysql

quit-docker: ## quit docker
	docker compose down