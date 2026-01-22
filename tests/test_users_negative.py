import pytest
import httpx
import pydantic

def test_get_user_404(api_mock):
    with pytest.raises(httpx.HTTPStatusError):
        api_mock.get_user(999)

def test_get_user_invalid_schema(api_mock):
    with pytest.raises(pydantic.ValidationError):
        api_mock.get_user(3)