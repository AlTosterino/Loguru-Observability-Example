run:
	docker-compose up -d

run-logs:
	docker-compose up log_generator

# OPENTELEMETRY, LOKI, GRAFANA
run-otel:
	docker-compose up otel_collector

run-loki:
	docker-compose up loki

run-grafana:
	docker-compose up grafana