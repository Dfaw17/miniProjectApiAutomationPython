import pytest
import requests
from assertpy import assert_that
from setting.endpoint import api_user
from faker import Faker

fake = Faker()


@pytest.mark.QaseIO(3)
def test():
    random_email = fake.email()
    head = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer 38cebe5affdc6038017ae850b112f50d15613c3f40d9d2a5d7bfd75f6218fcc2",
    }
    payload = {
        "name": "",
        "gender": "male",
        "email": random_email,
        "status": "active"
    }
    req = requests.post(api_user, headers=head, json=payload)

    # VALIDATION
    status_code = req.status_code
    res_field = req.json()[0]["field"]
    res_msg = req.json()[0]["message"]

    # ASSERT
    assert_that(status_code).is_equal_to(422)
    assert_that(res_field).is_equal_to("name")
    assert_that(res_msg).is_equal_to("can't be blank")
