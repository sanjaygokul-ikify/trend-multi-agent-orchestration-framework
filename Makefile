build:	docker-compose build

test:	poetry run pytest

lint:	black --check .
	flake8 .

clean:	rm -rf __pycache__ .pytest_cache

deploy:	docker-compose up -d