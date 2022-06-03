import requests


def test_status_code_of_entered_url(url, status_code):
    r = requests.get(url)
    actual_status_code = r.status_code
    assert actual_status_code == status_code
