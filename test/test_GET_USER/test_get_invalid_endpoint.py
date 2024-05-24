import pytest
import requests
from assertpy import assert_that
from setting.endpoint import api_user_wrong


@pytest.mark.QaseIO(9)
def test():
    head = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer 38cebe5affdc6038017ae850b112f50d15613c3f40d9d2a5d7bfd75f6218fcc2",
    }
    req = requests.get(api_user_wrong, headers=head)

    # VALIDATION
    status_code = req.status_code

    # ASSERT
    assert_that(status_code).is_equal_to(404)
