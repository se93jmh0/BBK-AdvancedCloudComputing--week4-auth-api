import security
from security import create_access_token
from security import get_current_user

import jwt
import os
import pytest

from database import get_db
from datetime import datetime, timedelta, timezone
from fastapi import HTTPException
from fastapi.security import HTTPAuthorizationCredentials
from importlib import reload
from sqlalchemy.orm import Session
from unittest.mock import create_autospec


def test_small_secret_key(monkeypatch):
    orig_jwt_secret = os.environ["JWT_SECRET"]
    os.environ["JWT_SECRET"] = "4"
    try:
        with pytest.raises(RuntimeError):
            reload(security)
    finally:
        os.environ["JWT_SECRET"] = orig_jwt_secret
        reload(security)


def test_get_current_user_empty_sub():
    credentials = create_autospec(HTTPAuthorizationCredentials,
        spec_set=False, instance=True)
    session = create_autospec(Session, spec_set=True, instance=True)
    credentials.credentials = create_access_token({"sub": ""})

    with pytest.raises(HTTPException) as exc_info:
        get_current_user(credentials, session)

    assert exc_info.value.status_code == 401


def test_get_current_user_expired_jwt():
    credentials = create_autospec(HTTPAuthorizationCredentials,
        spec_set=False, instance=True)
    session = create_autospec(Session, spec_set=True, instance=True)
    yesterday = datetime.now(timezone.utc)
    yesterday -= timedelta(days=1)
    payload = {"exp": yesterday}
    credentials.credentials = jwt.encode(
        payload, security.SECRET_KEY, algorithm=security.ALGORITHM)

    with pytest.raises(HTTPException) as exc_info:
        get_current_user(credentials, session)

    assert exc_info.value.status_code == 401


def test_get_current_user_unknown_user(client):
    credentials = create_autospec(HTTPAuthorizationCredentials,
        spec_set=False, instance=True)
    credentials.credentials = create_access_token(
        {"sub": "donotreply@example.com"})
    overridden_get_db = client.app.dependency_overrides[get_db]
    
    with pytest.raises(HTTPException) as exc_info:
        user = get_current_user(credentials, next(overridden_get_db()))

    assert exc_info.value.status_code == 401
