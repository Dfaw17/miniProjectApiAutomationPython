import pytest
import requests
from assertpy import assert_that
from setting.endpoint import api_user
from faker import Faker

fake = Faker()


@pytest.mark.QaseIO(11)
def test():
    # ====================== CREATE NEW USER ======================
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
    id_new_user = req.json().get("id")

    # ====================== UPDATE USER ======================
    random_name_update = f"{fake.name()} EDIT"
    random_email_update = fake.email()
    payload = {
        "name": random_name_update,
        "gender": "male",
        "email": random_email_update,
        "status": "active"
    }
    head = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer 38cebe5affdc6038017ae850b112f50d15613c3f40d9d2a5d7bfd75f6218fcc2",
    }
    req = requests.patch(f"{api_user}/{id_new_user}", headers=head, json=payload)

    # VALIDATION
    status_code = req.status_code
    res_name = req.json().get("name")
    res_email = req.json().get("email")

    # ASSERT
    assert_that(status_code).is_equal_to(200)
    assert_that(res_name).is_equal_to(random_name_update)
    assert_that(res_email).is_equal_to(random_email_update)
