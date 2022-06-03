import pytest
import requests


class TestDogs:
    url = "https://dog.ceo/"

    def test_all_breads(self):
        r = requests.get(self.url + "api/breeds/list/all")
        assert r.status_code == 200
        response = r.json()["message"]
        for response in response:
            print(f"{response}")

    def test_all_hound_breads(self):
        response = requests.get(self.url + "api/breed/hound/list")
        assert response.status_code == 200
        assert response.json()["message"] == ['afghan', 'basset', 'blood', 'english', 'ibizan', 'plott', 'walker']

    def test_random_image(self):
        response = requests.get(self.url + "api/breeds/image/random/3")
        assert response.status_code == 200
        first = response.json()["message"]
        response = requests.get(self.url + "api/breeds/image/random/3")
        second = response.json()["message"]
        assert first != second

    @pytest.mark.parametrize('breed, sub_breed', [
        ('airedale', []),
        ('buhund', ['norwegian']),
        ('mastiff', ['bull', 'english', 'tibetan'])])
    def test_breeds_and_sub_breads(self, breed, sub_breed):
        response = requests.get(self.url + "api/breeds/list/all")
        assert response.status_code == 200
        response = response.json()
        assert response['message'][breed] == sub_breed

    @pytest.mark.parametrize('breed, count', [
        ('australian', 1),
        ('bulldog', 3),
        ('hound', 7)])
    def test_count_of_sub_breeds(self, breed, count):
        r = requests.get(self.url + "api/breeds/list/all")
        response = r.json()
        assert len(response['message'][breed]) == count