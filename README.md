# Random User Info Generator

## Installation
> pip install -r requirements.txt

**Create .env file with next data format:**

>URL = "https://api.api-ninjas.com/v2/randomuser?count=1"

>API_KEY = "YOUR_API_KEY"
#### Get API_KEY from https://api-ninjas.com/
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

**OR if you run cli version: just select option and see the user data!**