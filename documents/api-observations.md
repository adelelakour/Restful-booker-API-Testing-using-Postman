## BUG-001: CreateBooking accepts invalid totalprice

**Endpoint:** `POST /booking`

**Scenario:**  
Create booking request is sent with `totalprice: -111` or `totalprice: 0`

**Steps to Reproduce:**
1. Send a `POST` request to `/booking`
2. set totalprice attribute in request body to -111 or 0
3. Send the request
4. Check the response status code

*request body*
```json
{
    "firstname" : "Jim-carry",
    "lastname" : "Brown",
    "totalprice" : 0,
    "depositpaid" : true,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}

```
**Expected behavior:**  
The API should reject the request with `400 Bad Request` because booking price should not be negative or zero.

**Actual behavior:**  
The API returns `200 OK` and creates the booking.

**Impact:**  
The API allows invalid business data to be created.

**Status:**  
Known API behavior observed during testing.




## BUG-002: CreateBooking returns unexpected Error

**Endpoint:** `POST /booking`

**Scenario:**  
Create booking request is sent with a missing field

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

```
**Expected behavior:**  
The API should return `400 Bad Request` because the client sent an invalid request body.

**Actual behavior:**  
The API returns `500 Internal Server Error`.

**Impact:**  
Invalid client input is handled as a server failure. This can mislead API consumers, make debugging harder, and cause monitoring systems to report false backend errors. It also suggests that request body validation is weak or missing. The API should validate the request body and return a clear 400 Bad Request response explaining which field is missing or invalid.

**Status:**  
Known API behavior observed during testing.