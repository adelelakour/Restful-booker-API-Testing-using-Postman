## BUG-001: POST /booking accepts invalid totalprice

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



## BUG-002: POST /booking returns unexpected Error

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



## BUG-003: POST /booking accepts invalid name value

**Endpoint:** `POST /booking`

**Scenario:**  
A create booking request is sent with the `firstname` value either blank or containing only whitespace.

*Request body:*

```json
{
    "firstname" : " ",
    "lastname" : "Elakour",
    "totalprice" : 100,
    "depositpaid" : true,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}
```
**Expected behavior:**  
The API should return `400 Bad Request` because `firstname` and `lastname` should not be blank.

**Actual behavior:**  
The API returns `200 OK` and creates the booking.

**Impact:**  
The API allows bookings to be created without customer names, which violates basic business data validation and can lead to incomplete or unusable booking records.



## BUG-004: POST /booking accepts check-in date in the past or checkin date after checkout date

**Endpoint:** `POST /booking`

**Scenario:**  
Create booking request is sent with a checkin date in the past.

*Request body:*

```json
{
    "firstname" : "adel",
    "lastname" : "elakour",
    "totalprice" : 100,
    "depositpaid" : true,
    "bookingdates" : {
        "checkin" : "2026-06-01",
        "checkout" : "2026-06-11"
    },
    "additionalneeds" : "Breakfast"
}
```
or

```json
{
    "firstname" : "adel",
    "lastname" : "elakour",
    "totalprice" : 100,
    "depositpaid" : true,
    "bookingdates" : {
        "checkin" : "2026-06-01",
        "checkout" : "2025-04-01"
    },
    "additionalneeds" : "Breakfast"
}
```


**Expected behavior:**  
The API should return `400 Bad Request` because checkin must be either today or a future date.

**Actual behavior:**  
The API returns `200 OK` and creates the booking.

**Impact:**  
The API allows bookings to be created with past check-in dates, which violates basic booking business rules and can lead to invalid booking records, scheduling issues, and unreliable availability or reporting data.



## BUG-005: POST /booking accepts very long name

**Endpoint:** `POST /booking`

**Scenario:**  
Create booking request is sent with a very long `firstname` value (eg: name of 70 letters)

**Expected behavior:**  
The API should return `400 Bad Request` because name length should not exceed a specific range (ex: 30 letters).

**Actual behavior:**  
The API returns `200 OK` and creates the booking.

**Impact:**  
The API allows bookings to be created with unusually long customer names. This can lead to poor data quality, display issues in user interfaces or reports, and unreliable booking records if no reasonable length validation is applied.



## BUG-005: POST /booking accepts very long name

**Endpoint:** `POST /booking`

**Scenario:**  
Create booking request is sent with a very long `firstname` value (eg: name of 70 letters)

**Expected behavior:**  
The API should return `400 Bad Request` because name length should not exceed a specific range (ex: 30 letters).

**Actual behavior:**  
The API returns `200 OK` and creates the booking.

**Impact:**  
The API allows bookings to be created with unusually long customer names. This can lead to poor data quality, display issues in user interfaces or reports, and unreliable booking records if no reasonable length validation is applied.





