# Cost Manager RESTful Web Services

Final Project – Asynchronous Server-Side Development Course 

---

## Project Description

This project implements a **Cost Manager RESTful Web Services system** that enables managing users, costs, monthly reports, logs, and administrative information.

The system was developed according to the course requirements and follows a **four-process architecture**, allowing future separation into independent services or servers.

The project uses **Node.js, Express.js, MongoDB Atlas, Mongoose, and Pino**, and is fully deployed to the cloud.

---

## Technologies Used

- Node.js
- Express.js
- MongoDB Atlas
- Mongoose
- Render
- GitHub
- Pino Logger
- Jest

## System Architecture

The project is divided into **four independent processes**, each responsible for a specific domain:

### 1. Users Process
- Add new users  
- Get details of a specific user  
- List all users  

### 2. Costs Process
- Add cost items  
- Generate monthly reports  
- Implements the *Computed Design Pattern*  

### 3. Logs Process
- Logs every HTTP request  
- Stores logs in MongoDB  

### 4. Admin Process
- Returns development team details  
- Data is not stored in the database  

Each process runs separately and can be deployed independently.

---

## Deployed Services (Render)

- **Users Service**  
  https://cost-manager-users-sgdp.onrender.com  

- **Costs Service**  
  https://cost-manager-costs-ptc6.onrender.com  

- **Logs Service**  
  https://cost-manager-logs-7cgb.onrender.com  

- **Admin Service**  
  https://cost-manager-admin-otvg.onrender.com  

---

## Database

- MongoDB Atlas (cloud-hosted)
- Collections:
  - users
  - costs
  - logs
  - report_cache
- `_id` is stored in MongoDB but never returned in API responses
- Supported categories:
  - food
  - health
  - housing
  - sports
  - education

---

## Computed Design Pattern

Monthly reports are cached **only for past months**.  
Since the system does not allow adding cost items with past dates, cached reports are immutable and safe to reuse.

Reports for the current or future months are always generated dynamically.

---

## API Endpoints

### Users Service

- **GET /api/users**  
  Returns all users

- **GET /api/users/:id**  
  Returns user details and total costs

- **POST /api/add**  
  Adds a new user

---

### Costs Service

- **POST /api/add**  
  Adds a new cost item  
  - Future dates are allowed  
  - Past dates are rejected  

- **GET /api/report?id=USER_ID&year=YYYY&month=MM**  
  Returns a monthly cost report grouped by categories

---

### Logs Service

- **GET /api/logs**  
  Returns all logged HTTP requests

---

### Admin Service

- **GET /api/about**  
  Returns development team details

---

## How to Run

There are two ways to use the project: run the four services yourself, or call the services that are already deployed on Render.

### Option A — Run Locally

1. Install dependencies: `npm install`
2. Create a `.env` file (use `.env.example` as a template). For a fully local run, set `USERS_SERVICE_URL=http://localhost:2001` so the Costs service verifies users against your local Users service (not the deployed one).
3. Start each process in its own terminal:

```bash
npm run start:users   # http://localhost:2001
npm run start:costs   # http://localhost:2002
npm run start:logs    # http://localhost:2003
npm run start:admin   # http://localhost:2004
```

The services are now reachable at `http://localhost:PORT`.

### Option B — Use the Deployed Backend (Render)

The four services are already deployed (see [Deployed Services](#deployed-services-render) above), so no local setup is needed — just send HTTP requests to the Render URLs.

> Note: free Render instances sleep after ~15 minutes of inactivity. The first request after a sleep can take 30–50 seconds while the service wakes up. Hit each `/health` endpoint first to wake all four before testing.

---

## Testing

Unit tests were written for all endpoints using **Jest** (with `supertest`). They verify:
- Endpoint accessibility (`/health`)
- Basic request/response structure
- Validation handling (error responses)

Run the Jest suite:

```bash
npm test
```

A Python end-to-end tester is also included at `tests/test.py`. It walks the full flow (about → report → add cost → report → user → logs):

```bash
python3 tests/test.py
```

Both test sets target the **deployed Render services** by default. To point them at a local run instead, switch the base URLs to `http://localhost:PORT` (the local URLs are present as a commented-out block in `tests/test.py`).

