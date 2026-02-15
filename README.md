# Random User Info Generator

## Installation
> pip install -r requirements.txt

## Starting
### Server:
``` Bash
uvicorn backend.main:app --reload
```
### Cli:
``` Bash
python -m cli.main
```

## User Guide
**When you start a uvicorn server you can visit this endpoint: *localhost:8000/api/get/info* and see the user data!**