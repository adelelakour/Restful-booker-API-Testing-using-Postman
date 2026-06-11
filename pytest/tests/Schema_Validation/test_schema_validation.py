import requests
from jsonschema import validate

def test_get_token_schema(base_url):
    schema = {
        "type": "object",
        "required": ["token"],
        "properties": {
            "token": {
                "type": "string"
            }
        }
    }

    payload = {
        "username": "admin",
        "password": "password123"
    }

    response = requests.post(f"{base_url}/auth", json=payload)

    assert response.status_code == 200

    json_data = response.json()

    validate(instance=json_data, schema=schema)


def test_create_booking_schema(base_url, auth_token, test_create_booking):
    schema = create_booking_schema = {
        "type": "object",
        "required": ["bookingid", "booking"],
        "properties": {
            "bookingid": {
                "type": "number"
            },
            "booking": {
                "type": "object",
                "required": [
                    "firstname",
                    "lastname",
                    "totalprice",
                    "depositpaid",
                    "bookingdates",
                    "additionalneeds"
                ],
                "properties": {
                    "firstname": {
                        "type": "string"
                    },
                    "lastname": {
                        "type": "string"
                    },
                    "totalprice": {
                        "type": "number"
                    },
                    "depositpaid": {
                        "type": "boolean"
                    },
                    "bookingdates": {
                        "type": "object",
                        "required": ["checkin", "checkout"],
                        "properties": {
                            "checkin": {
                                "type": "string"
                            },
                            "checkout": {
                                "type": "string"
                            }
                        }
                    },
                    "additionalneeds": {
                        "type": "string"
                    }
                }
            }
        }
    }

    validate(instance=test_create_booking, schema=schema)

def test_get_a_booking_schema(base_url, auth_token, test_create_booking):
    schema = {
        "type": "object",
        "properties": {
            "firstname": {
                "type": "string"
            },
            "lastname": {
                "type": "string"
            },
            "totalprice": {
                "type": "integer"
            },
            "depositpaid": {
                "type": "boolean"
            },
            "bookingdates": {
                "type": "object",
                "properties": {
                    "checkin": {
                        "type": "string"
                    },
                    "checkout": {
                        "type": "string"
                    }
                },
                "required": [
                    "checkin",
                    "checkout"
                ]
            }
        },
        "required": [
            "firstname",
            "lastname",
            "totalprice",
            "depositpaid",
            "bookingdates"
        ]
    }

    bookingID = test_create_booking["bookingid"]
    response = requests.get(f"{base_url}/booking/{bookingID}")
    assert response.status_code == 200
    validate(instance=response.json(), schema=schema)

