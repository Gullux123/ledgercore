
from datetime import datetime

from sqlalchemy import BigInteger, Integer, String, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base


class Account(Base):
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        autoincrement=True
    )

    owner_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
        index=True
    )

    currency: Mapped[str] = mapped_column(
        String(3),
        nullable=False,
        default="INR"
    )

    status: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        default="ACTIVE"
    )

    min_balance: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
        default=0
    )

    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now()
    )


class AccountBalance(Base):
    __tablename__ = "account_balances"

    account_id: Mapped[int] = mapped_column(
        ForeignKey("accounts.id"),
        primary_key=True
    )

    balance: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
        default=0
    )

    version: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0
    )

    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        onupdate=func.now()
    )
