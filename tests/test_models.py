import pytest
from sqlalchemy.exc import IntegrityError
import uuid
from app.core.db import SessionLocal
from app.models import User, Account


def test_user_email_must_be_unique():
    db = SessionLocal()

    try:
        email = f"duplicate-{uuid.uuid4().hex}@example.com"

        user1 = User(
            email=email,
            password_hash="hash1"
        )

        user2 = User(
            email=email,
            password_hash="hash2"
        )

        db.add(user1)
        db.flush()

        db.add(user2)

        with pytest.raises(IntegrityError):
            db.flush()

        db.rollback()

    finally:
        db.close()


def test_account_must_reference_existing_user():
    db = SessionLocal()

    try:
        account = Account(owner_id=999999)

        db.add(account)

        with pytest.raises(IntegrityError):
            db.flush()

        db.rollback()

    finally:
        db.close()