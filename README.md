# Support service application


## Adjust the application


### Create `.env` file based on `.env.default`
```bash
# Unix
cp .env.default .env

# Windows
copy .env.default .env
```
### Install deps
```bash
pipenv sync --dev

# Activate the environment
pipenv shell
```

## Code quality tools
- flake8 6.0.0
- black 22.12.0
- isort 5.11.2

## Run using Docker Compose
```bash
docker-compose up -d
```

### Useful commands
```bash
# Build images
docker-compose build

# Stop containers
docker-compose down

# Check containers status
docker-compose ps

## Logs

# Get all logs
docker-compose logs

# Get specific logs
docker-compose logs app

# Get limited logs
docker-compose logs --tail 10 app

# Get flowed logs
docker-compose logs -f app
```

## Application description
```bash
▾ users
    ├─ apps.py # Django apps configuration
    ├─ urls.py # pre-controller
    ├─ api.py # Endpoints / post-controller
    ├─ models.py # Database tables mapper
    ├─ admin.py
```

# Database
```mermaid
erDiagram
    Users {
        int id
        string first_name
        string last_name
        string email
        string password
        bool is_stuff
        bool is_active
        string role
        datetime created_at
        datetime updated_at
    }
    
    Tickets {
        int id
        int customer_id
        int manager_id
        string header
        string body
        datetime created_at
        datetime updated_at
    }
    
    Comments {
        int id
        int prev_comment_id
        int user_id
        int ticket_id
        string body
        datetime created_at
        datetime updated_at
    }
    
    Users ||--o{ Tickets : ""
    Tickets ||--o{ Comments : ""
    Comments ||--o{ Comments : ""
```