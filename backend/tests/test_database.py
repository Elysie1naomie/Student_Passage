import os

import pytest
from sqlalchemy import text

pytestmark = pytest.mark.skipif(
    "DATABASE_URL" not in os.environ,
    reason="DATABASE_URL absent : test de connexion PostgreSQL ignoré",
)


def test_database_is_reachable() -> None:
    from app.db import engine

    with engine.connect() as conn:
        assert conn.execute(text("SELECT 1")).scalar_one() == 1
