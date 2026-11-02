# Authentication API

A simple Authentication API that builds on the the technologies we've already
learned about and introduces JWT-based bearer authorization to FastAPI.

# Test Results

    $ python -m pytest -v | cat
    ============================= test session starts ==============================
    platform linux -- Python 3.14.4, pytest-9.1.1, pluggy-1.7.0 -- /home/jhorns01/Uni/BBK/DataAnalyticsAndAI/AdvancedCloudComputing/week4-auth-api/.venv/bin/python
    cachedir: .pytest_cache
    rootdir: /home/jhorns01/Uni/BBK/DataAnalyticsAndAI/AdvancedCloudComputing/week4-auth-api
    plugins: anyio-4.16.0
    collecting ... collected 6 items

    tests/test_auth.py::test_password_hash PASSED                            [ 16%]
    tests/test_auth.py::test_login_and_profile PASSED                        [ 33%]
    tests/test_auth.py::test_profile_requires_token PASSED                   [ 50%]
    tests/test_auth.py::test_duplicate_registration PASSED                   [ 66%]
    tests/test_auth.py::test_wrong_password_login PASSED                     [ 83%]
    tests/test_auth.py::test_invalid_registration_data PASSED                [100%]

    =============================== warnings summary ===============================
    .venv/lib/python3.14/site-packages/fastapi/testclient.py:1
    /home/jhorns01/Uni/BBK/DataAnalyticsAndAI/AdvancedCloudComputing/week4-auth-api/.venv/lib/python3.14/site-packages/fastapi/testclient.py:1: StarletteDeprecationWarning: Using `httpx` with `starlette.testclient` is deprecated; install `httpx2` instead.
        from starlette.testclient import TestClient as TestClient  # noqa

    -- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
    ========================= 6 passed, 1 warning in 0.39s =========================
    (.venv)
