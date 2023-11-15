1. 
# Phone Addresses API

```commandline
git clone https://github.com/Unuseptiy/phone-address.git

cd phone-address
touch app/.env
```

Fill the app/.env file with vars like:
```commandline
# app settings
project_name="Phone Address API"
api_prefix="/api/v1"
version="1.0.0"
openapi_url="/docs/v1/openapi.json"
docs_url="/docs/v1"
host="localhost"
port="8000"
debug="True"

REDIS_URL="redis://redis"
```

```commandline
docker-compose up --build
```

Run tests:

```commandline
poetry install
docker run -p 6379:6379 -d redis
poetry run pytest
```

2. 
# SQL

```commandline
CREATE INDEX ON short_names(name);
CREATE INDEX ON full_names(split_part(name, '.', 1))
```

```commandline
UPDATE full_names
SET status = short_names.status
FROM short_names
WHERE split_part(full_names.name, '.', 1) = short_names.name;
```

```commandline
UPDATE full_names
SET status = act_status
FROM (SELECT name, status as act_status FROM short_names) as foo
WHERE split_part(full_names.name, '.', 1) = foo.name;
```
