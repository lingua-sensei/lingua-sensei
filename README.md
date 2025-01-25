# Lingua Sensei

Lingua Sensei is a platform where you can practice vocabulary in its context. It contains hundreds of recorded audio and text samples to boost your learning. 

## Running locally

### API

Running backend (Django 5), it will use localhost:8000

```shell
cd ./api
uv run python manage.py runserver
```

Running tests

```
uv run pytest --cov=linguist --cov-report=html --cov-report=term-missing 
```

### WEB

Running frontend (Svelte 5), it will use localhost:5173

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

