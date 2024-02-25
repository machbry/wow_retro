launch-db:
	mkdir data/postgres -p
	@docker compose -f docker-compose-db.yaml up -d 

launch-dagster-assets:
	@dagster dev -f assets.py
