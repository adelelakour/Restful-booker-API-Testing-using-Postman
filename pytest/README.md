# Restful Booker API Testing with Pytest

This project contains automated API tests for the public Restful Booker service using `pytest`. The suite validates basic service availability, booking CRUD behavior, and response schema correctness against the live API.

## Project Overview

The tests target `https://restful-booker.herokuapp.com` and cover three main areas:

- Smoke checks to confirm the service is reachable and core endpoints respond as expected
- End-to-end booking operations including create, read, update, partial update, and delete
- JSON schema validation for authentication and booking responses

The project uses shared `pytest` fixtures in `conftest.py` to provide the base URL, create an authentication token, and generate a booking record for tests that require existing data.

## Tech Stack

- Python 3
- `pytest` for test execution and assertions
- `requests` for HTTP client calls
- `jsonschema` for response schema validation

## Project Structure

```text
pytest/
├── conftest.py
├── pytest.ini
├── requirements.txt
└── tests/
    ├── Booking_CRUD_Flow/
    │   └── test_CRUD.py
    ├── Schema_Validation/
    │   └── test_schema_validation.py
    └── Smoke_Tests/
        └── test_if_system_alive.py
```

## Installation

1. Create and activate a virtual environment.
2. Install the project dependencies.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

If you are using Windows PowerShell, activate the environment with:

```powershell
.venv\Scripts\Activate.ps1
```

## How to Run Tests

Run the full test suite from the project root:

```bash
pytest
```

Because `pytest.ini` already includes `addopts = -v`, tests run in verbose mode by default.

You can also run specific test groups:

```bash
pytest tests/Smoke_Tests/
pytest tests/Booking_CRUD_Flow/
pytest tests/Schema_Validation/
```

## API Endpoints Covered

The current suite exercises the following endpoints:

- `POST /auth`
  - Generates an authentication token
  - Validates the token response schema

- `GET /ping`
  - Verifies the API is alive

- `GET /booking`
  - Confirms the booking collection endpoint is reachable

- `POST /booking`
  - Creates a new booking
  - Validates the create-booking response schema

- `GET /booking/{id}`
  - Retrieves a specific booking
  - Validates the returned booking schema

- `PUT /booking/{id}`
  - Replaces an existing booking using an authenticated request

- `PATCH /booking/{id}`
  - Partially updates an existing booking using an authenticated request

- `DELETE /booking/{id}`
  - Deletes a booking using an authenticated request

## Test Organization

- `tests/Smoke_Tests/test_if_system_alive.py`
  - Basic health and availability checks

- `tests/Booking_CRUD_Flow/test_CRUD.py`
  - Functional booking lifecycle tests

- `tests/Schema_Validation/test_schema_validation.py`
  - Response contract validation using JSON schemas

## Notes

- The suite depends on the availability of the live Restful Booker environment.
- Authentication uses the sample admin credentials defined in `conftest.py`.
- Some tests create and modify real booking data in the target environment.
