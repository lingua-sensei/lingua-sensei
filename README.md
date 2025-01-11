# Lingua Sensei

## Running locally

### API

Running backend (Django 5)

```shell
cd ./api
uv run python manage.py runserver
```

Running tests

```
uv run pytest --cov=linguist --cov-report=html --cov-report=term-missing 
```

### WEB

Running frontend (Svelte 5)

```shell
cd ./web
pnpm install && pnpm dev
```

Running tests

```
pnpm test -- --run

pnpm exec playwright install # required one time for installing headless browser
pnpm test:browser # runs headless browser tests
```

