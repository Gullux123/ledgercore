# Day 2 – Data Models and First Database Migration

## Objective

Create the initial database models for LedgerCore, generate database tables using Alembic migrations, and verify important database constraints through automated tests.

## 1. SQLAlchemy Database Configuration

Updated `app/core/db.py` to include:

- `DeclarativeBase` for defining SQLAlchemy models.
- `engine` for connecting the Python application to MySQL.
- `SessionLocal` for creating database sessions.
- `get_db()` for providing and closing database sessions.

## 2. Database Models

Created three SQLAlchemy models:

### User
Represents a registered LedgerCore user.

- Unique email address.
- Password hash.
- User role.
- Account creation timestamp.

### Account
Represents a financial account owned by a user.

- Foreign key referencing `users.id`.
- Currency (INR by default).
- Account status.
- Minimum balance.
- Account creation timestamp.

### AccountBalance
Stores the current balance of an account.

- Account ID as both primary key and foreign key.
- Balance stored as an integer in paise.
- Version number for future optimistic concurrency control.
- Last updated timestamp.

## 3. Alembic Migration

Configured Alembic to detect SQLAlchemy models through `Base.metadata`.

Created the initial migration:

`create users accounts balances`

Revision ID: `cfae86acaf56`

Successfully executed:

- `alembic upgrade head`
- `alembic downgrade -1`
- `alembic upgrade head`

Verified that MySQL contained the three application tables and the `alembic_version` tracking table.

During downgrade testing, corrected the migration's downgrade order to remove the foreign key constraint before dropping its required index.

## 4. Database Constraint Testing

Created `tests/test_models.py` with two tests:

1. **Unique email constraint:** Verified that MySQL rejects two users with the same email address.
2. **Foreign key constraint:** Verified that MySQL rejects an account referencing a nonexistent user.

Used SQLAlchemy sessions, `flush()`, `IntegrityError`, and `rollback()` to test database enforcement.

Generated a unique email for each test run to ensure repeatability.

## 5. Final Test Results

| Test | Result |
|---|---|
| Health endpoint | Passed |
| Duplicate email constraint | Passed |
| Invalid account foreign key | Passed |
| **Total** | **3 passed** |

One Starlette deprecation warning remains regarding the use of `httpx` with `starlette.testclient`. It did not affect test execution.

## 6. Key Concepts Learned

- SQLAlchemy ORM models and database metadata.
- Primary keys, foreign keys, unique constraints, and indexes.
- Database sessions and transaction handling.
- Alembic migration generation and execution.
- Schema upgrades and downgrades.
- MySQL InnoDB constraint enforcement.
- Automated database testing with pytest.

## 7. Project Status

Completed the initial database schema and verified its constraints.

The application currently has database models and migration support, but the ledger transfer functionality and API integration are still pending.

**Day 2 Status: Completed**
