# Authentication API

A simple Authentication API that builds on the the technologies we've already
learned about and introduces JWT-based bearer authentication to FastAPI.

# Usage

This application requires Python 3 and has been tested on Python 3.14.4.

## Steps to Run

First initialize a Python virtual environment; e.g.:

    python3 -m venv .venv
    source .venv/bin/activate

Next install Authentication API's dependencies; for example:

    python3 -m pip install -r requirements.txt

Now we need a JWT secret in the environment; in Bash you can do that like so:

    export JWT_SECRET=foobar

One way to generate a secret is to run the following:

    python3 -c "import secrets; print(secrets.token_hex(32))"

Simply replace `foobar` with the string printed by the above Python snippet.

You can now launch the web server:

    uvicorn main:app

At this point the Authentication API is up and running!

To actually try it out, one of the easiest ways is using the Swagger interface
built into FastAPI.  Visit http://127.0.0.1:8000/docs.  You may then:
* Create a user by issuing a `POST` to the `/auth/register` endpoint
* Log the user in by issuing a `POST` to the `/auth/login` endpoint
* Store your logged-in user's credentials using the _Authorize_ button (make
  sure to only copy the access_token without the "s)
* Get your user's profile by issuing a `GET` to the `/profile/me` endpoint

At this point, congratulations—you're an Authentication API pro!  Note that
registered users are stored in the `auth.db` SQLite database file.

# Testing

To run the Authentication API automated tests, one must employ Pytest; e.g.:

    python3 -m pytest -v

Here's what the output should look like roughly:

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

And don't worry—running the tests doesn't affect the local `auth.db`.

Happy Authenticating!  &:D
