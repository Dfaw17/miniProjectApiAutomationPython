import pytest
import requests
from assertpy import assert_that
from setting.endpoint import api_user
from faker import Faker
fake = Faker()


@pytest.mark.QaseIO(7)
def test():
    random_name = fake.name()
    random_email = fake.email()
    head = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer 38cebe5affdc6038017ae850b112f50d15613c3f40d9d2a5d7bfd75f6218fcc2",
    }
    payload = {
        "name": random_name,
        "gender": "male",
        "email": random_email,
        "status": "active"
    }
    req = requests.post(api_user, headers=head, json=payload)

    # VALIDATION
    status_code = req.status_code
    res_name = req.json().get("name")
    res_email = req.json().get("email")

    # ASSERT
    assert_that(status_code).is_equal_to(201)
    assert_that(res_name).is_equal_to(random_name)
    assert_that(res_email).is_equal_to(random_email)
