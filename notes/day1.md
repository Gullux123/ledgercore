# LedgerCore — Day 1 Learning Notes

## 1. What is an HTTP request?

An HTTP request is a message sent by a client (such as a browser or frontend application) to a server to request information or perform an operation.

Common HTTP methods:

- **GET:** Retrieves information from the server.
- **POST:** Sends information to the server to create something or perform an operation.

Example:

When a user opens the LedgerCore health endpoint, the browser sends a GET request to `/health`. FastAPI processes the request and returns a response.

## 2. What does SQLAlchemy Engine do?

The SQLAlchemy Engine is the main interface between a Python application and a database.

It manages database connectivity and provides connections whenever the application needs to execute SQL queries.

### What is a connection pool?

A connection pool is a collection of reusable database connections.
Instead of opening a completely new connection for every request, the application can reuse existing connections.

Benefits:

- Reduces connection overhead.
- Improves application performance.
- Manages database connections efficiently.

## 3. Why is .env excluded from Git?

The `.env` file stores sensitive configuration values, such as database usernames, passwords and connection strings.

Uploading it to a public GitHub repository could expose credentials.

Therefore:

- `.env` is excluded through `.gitignore`.
- `.env.example` is committed with placeholder values.
- Each developer maintains their own local `.env` file.

## 4. What does docker compose up do?

The `docker compose up` command reads the `docker-compose.yml` configuration and creates or starts the required Docker resources.

For LedgerCore, it will:

- Download the MySQL 8.0 image if it is not already available.
- Create a MySQL container named `ledgercore-mysql`.
- Create the `ledgercore` database.
- Configure the database user and password.
- Create a persistent Docker volume named `mysql_data`.
- Expose MySQL through port 3306.

The persistent volume ensures that database data can survive container recreation.

## 5. What is LedgerCore?

LedgerCore is a simulated payment ledger system designed to demonstrate reliable financial transaction processing.

It will use FastAPI as the backend, MySQL as the database and React as the frontend.

Its research focus is comparing concurrency-control strategies to prevent incorrect balances when multiple transfers happen simultaneously.

**Note:** No real money is involved.