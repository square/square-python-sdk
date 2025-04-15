from square.core.api_error import ApiError
from square.types.error import Error


class TestResponse:
    def __init__(self, data):
        for key, value in data.items():
            if isinstance(value, list):
                setattr(
                    self,
                    key,
                    [
                        TestResponse(item) if isinstance(item, dict) else item
                        for item in value
                    ],
                )
            else:
                setattr(self, key, value)


def test_exception_without_body():
    exception = ApiError(status_code=400, body=None)

    assert "status_code: 400" in str(exception)
    assert exception.status_code == 400
    assert len(exception.errors) == 1
    assert isinstance(exception.errors[0], Error)
    assert exception.errors[0].code == "Unknown"
    assert exception.errors[0].category == "API_ERROR"
    assert exception.errors[0].field is None
    assert exception.errors[0].detail is None


def test_exception_with_v1_error():
    error_string = """{
        "type": "INVALID_REQUEST",
        "message": "Invalid field value",
        "field": "customer_id"
    }"""
    exception = ApiError(status_code=400, body=error_string)

    assert "status_code: 400" in str(exception)
    assert "body:" in str(exception)
    assert exception.status_code == 400
    assert len(exception.errors) == 1
    assert isinstance(exception.errors[0], Error)
    assert exception.errors[0].code == "INVALID_REQUEST"
    assert exception.errors[0].category == "API_ERROR"
    assert exception.errors[0].field == "customer_id"
    assert exception.errors[0].detail == "Invalid field value"


def test_exception_with_v1_error_without_type():
    error_string = """{
        "message": "Invalid field value",
        "field": "customer_id"
    }"""
    exception = ApiError(status_code=400, body=error_string)

    assert "status_code: 400" in str(exception)
    assert exception.status_code == 400
    assert len(exception.errors) == 1
    assert isinstance(exception.errors[0], Error)
    assert exception.errors[0].code == "Unknown"
    assert exception.errors[0].category == "API_ERROR"
    assert exception.errors[0].field == "customer_id"
    assert exception.errors[0].detail == "Invalid field value"


def test_exception_with_v2_error():
    error_string = """{
        "errors": [{
            "category": "API_ERROR",
            "code": "BAD_REQUEST",
            "detail": "Invalid input",
            "field": "email"
        }]
    }"""
    exception = ApiError(status_code=400, body=error_string)

    assert "status_code: 400" in str(exception)
    assert exception.status_code == 400
    assert len(exception.errors) == 1
    assert isinstance(exception.errors[0], Error)
    assert exception.errors[0].category == "API_ERROR"
    assert exception.errors[0].code == "BAD_REQUEST"
    assert exception.errors[0].detail == "Invalid input"
    assert exception.errors[0].field == "email"


def test_exception_with_v2_error_as_dict():
    errors = {
        "errors": [
            {
                "category": "API_ERROR",
                "code": "BAD_REQUEST",
                "detail": "Invalid input",
                "field": "email",
            }
        ]
    }
    exception = ApiError(status_code=400, body=errors)

    assert "status_code: 400" in str(exception)
    assert exception.status_code == 400
    assert len(exception.errors) == 1
    assert isinstance(exception.errors[0], Error)
    assert exception.errors[0].category == "API_ERROR"
    assert exception.errors[0].code == "BAD_REQUEST"
    assert exception.errors[0].detail == "Invalid input"
    assert exception.errors[0].field == "email"


def test_exception_with_v2_error_as_object():
    errors = TestResponse(
        {
            "errors": [
                {
                    "category": "API_ERROR",
                    "code": "BAD_REQUEST",
                    "detail": "Invalid input",
                    "field": "email",
                }
            ]
        }
    )

    exception = ApiError(status_code=400, body=errors)

    assert "status_code: 400" in str(exception)
    assert exception.status_code == 400
    assert len(exception.errors) == 1
    assert isinstance(exception.errors[0], Error)
    assert exception.errors[0].category == "API_ERROR"
    assert exception.errors[0].code == "BAD_REQUEST"
    assert exception.errors[0].detail == "Invalid input"
    assert exception.errors[0].field == "email"


def test_exception_with_multiple_errors():
    errors = {
        "errors": [
            {
                "category": "API_ERROR",
                "code": "BAD_REQUEST",
                "detail": "Invalid input",
                "field": "email",
            },
            {
                "category": "AUTHENTICATION_ERROR",
                "code": "UNAUTHORIZED",
                "detail": "Not authorized",
                "field": None,
            },
        ]
    }
    exception = ApiError(status_code=400, body=errors)

    assert exception.status_code == 400
    assert len(exception.errors) == 2

    # First error
    assert exception.errors[0].category == "API_ERROR"
    assert exception.errors[0].code == "BAD_REQUEST"
    assert exception.errors[0].detail == "Invalid input"
    assert exception.errors[0].field == "email"

    # Second error
    assert exception.errors[1].category == "AUTHENTICATION_ERROR"
    assert exception.errors[1].code == "UNAUTHORIZED"
    assert exception.errors[1].detail == "Not authorized"
    assert exception.errors[1].field is None
