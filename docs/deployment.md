# Deployment

## Local Development

```bash
python -m pip install -e .[dev]
python -m uvicorn main:app --reload
```

## Docker

```bash
docker compose -f docker-compose.example.yml up --build
```

The container expects your real config files to be mounted into `./config`.

## Health Check

```bash
curl http://127.0.0.1:8000/healthz
```

Expected response:

```json
{"status":"ok"}
```

## Production Notes

- replace example keys in `config/accounts.example.yaml`
- move example config into environment-specific files
- use a process manager such as systemd, Docker, or a platform runtime
- place the service behind HTTPS if exposed publicly
- do not describe upstream quotas as unlimited; use failover language instead
