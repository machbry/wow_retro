launch-db:
	mkdir data/postgres -p
	@docker compose -f docker-compose-db.yaml up -d

upgrade-db:
	alembic upgrade head 

launch-dagster-assets:
	@dagster dev -f assets.py
