mysql: ## start mysql
	docker compose up -d mysql

stop-mysql: ## stop mysql
	docker compose stop mysql

quit-docker: ## quit docker
	docker compose down

copy-env: ## copy .env.example to .env
	cp .env.example .env
	rm .env.example
	
reverse-copy-env: ## copy .env to .env.example
	cp .env .env.example
	rm .env