## BUG-001: CreateBooking accepts negative totalprice

**Endpoint:** `POST /booking`

**Scenario:**  
Create booking request is sent with `totalprice: -111`.

**Expected behavior:**  
The API should reject the request with `400 Bad Request` because booking price should not be negative.

**Actual behavior:**  
The API returns `200 OK` and creates the booking.

**Impact:**  
The API allows invalid business data to be created.

**Status:**  
Known API behavior observed during testing.


## BUG-002: CreateBooking returns unexpected Error

**Endpoint:** `POST /CreateBooking`

**Scenario:**  
Create booking request is sent with invalid body (ex: remove lastname field).

*Request body:*

```json
{
  "firstname": "Jim",
  "totalprice": 111,
  "depositpaid": true,
  "bookingdates": {
    "checkin": "2018-01-01",
    "checkout": "2019-01-01"
  },
  "additionalneeds": "Breakfast"
}

**Expected behavior:**  
The API should return 400 Bad Request because the client sent an invalid request body.

**Actual behavior:**  
The API returns 500 Internal Server Error.

**Impact:**  
Invalid client input is handled as a server failure. This can mislead API consumers, make debugging harder, and cause monitoring systems to report false backend errors. It also suggests that request body validation is weak or missing. The API should validate the request body and return a clear 400 Bad Request response explaining which field is missing or invalid.

**Status:**  
Known API behavior observed during testing.