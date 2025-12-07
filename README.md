# analytics-API

# an analytics API using FastAPI and time-series postgres

Own your data pipeline!

## Docker
- 'docker build -t analyticsapi -f Dockerfile .'
- 'docker run analyticsapi'

becomes

- 'docker compose up --watch'
- 'socker compose down' or 'docker compose down -v' (to remove volumes)
- 'docker compose run app /bin/bash' or 'docker compose run app python'