# LedgerCore

A concurrent-safe double-entry payment ledger built using FastAPI, MySQL and React.

## Project Overview

LedgerCore is a simulated payment ledger system designed to demonstrate reliable financial transaction processing. It focuses on maintaining accurate account balances when multiple transactions occur simultaneously.

This project does not process real money.

## Technology Stack

- **Backend:** Python, FastAPI
- **Database:** MySQL 8.0
- **ORM:** SQLAlchemy
- **Database Driver:** PyMySQL
- **Containerization:** Docker and Docker Compose
- **Testing:** Pytest and HTTPX
- **Frontend:** React (planned)


## Current Development Status

- [x] Development environment setup
- [x] GitHub repository created
- [x] Project structure created
- [x] Docker Compose configuration added
- [x] MySQL 8.0 container running
- [x] Python-to-MySQL connection verified
- [x] FastAPI health endpoint implemented
- [x] Automated health endpoint test passed
- [ ] Database models and schema
- [ ] Double-entry ledger implementation
- [ ] Transfer API and transaction management
- [ ] Concurrency-control strategies
- [ ] Performance benchmarking
- [ ] React frontend


## Project Structure

```text
ledgercore/
├── app/
│   ├── core/
│   │   ├── __init__.py
│   │   └── db.py
│   ├── __init__.py
│   └── main.py
├── notes/
│   └── day1.md
├── tests/
│   └── test_health.py
├── docker-compose.yml
├── requirements.txt
├── .env.example
└── README.md
```

## Prerequisites

- Python 3.11+
- Git
- Docker Desktop with WSL 2
- VS Code

## How to Run

Instructions will be updated as the project implementation progresses.

## Research Focus

The project will compare database concurrency-control strategies for double-entry ledger transfers using MySQL InnoDB.

Evaluation will focus on transaction correctness, throughput, latency, deadlocks, retries and idempotency.

## Disclaimer

LedgerCore is an educational software development and research project. It does not handle real financial transactions.
