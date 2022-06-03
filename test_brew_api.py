import pytest
import requests


class TestBrew:
    url = "https://api.openbrewerydb.org/breweries"

    def test_search_breweries(self):
        search_breweries = "Diving Dog Brewhouse"
        url = f"{self.url}/search?query={search_breweries}"
        r = requests.get(url)
        assert r.status_code == 200
        response = r.json()
        assert search_breweries in response[0]['name']

    @pytest.mark.parametrize('state', ['New York', 'West Virginia', 'California'])
    def test_breweries_state(self, state):
        r = requests.get(self.url, params={'by_state': state})
        assert r.status_code == 200
        response = r.json()
        for i in range(len(response)):
            assert response[i]['state'] == state

    @pytest.mark.parametrize('brew_id', [999, 888, 'test'])
    def test_not_valid_id(self, brew_id):
        url = self.url + f"/{brew_id}"
        r = requests.get(url)
        assert r.status_code == 404
        response = r.json()
        assert response['message'] == "Couldn't find Brewery"

    @pytest.mark.parametrize('type', ['micro'])
    def test_count_brewery_type(self, type):
        r = requests.get(self.url + f"?by_type={type}")
        assert r.status_code == 200
        response = r.json()
        count = 0
        for i in range(len(response)):
            assert response[i]['brewery_type'] == type
            count += 1
        print(count)

    @pytest.mark.parametrize('sort', ['asc'])
    def test_sort_brewery(self, sort):
        r = requests.get(self.url + f"?sort=name:{sort}&per_page=10")
        assert r.status_code == 200
        response = r.json()
        for i in range(len(response)):
            print(response[i]['name'])
