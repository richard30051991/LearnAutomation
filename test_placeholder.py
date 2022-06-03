import pytest
import requests


class TestPlaceholder:
    url = "https://jsonplaceholder.typicode.com/"

    def test_check_users(self):
        response = requests.get(self.url + "users")
        assert response.status_code == 200
        users = response.json()
        assert len(users) == 10

    def test_posts_id(self):
        url = self.url + 'posts'
        r = requests.get(url)
        assert r.status_code == 200
        response = r.json()
        for i in range(len(response)):
            assert response[i]['id'] == i + 1

    def test_post_comments(self):
        url = self.url + "posts/1/comments"
        headers = {'Content-type': 'application/json; charset=UTF-8'}
        name = 'test'
        email = 'testov123@maila.net'
        body = {'name': name, 'email': email}
        r = requests.post(url, headers=headers, json=body, verify=False)
        assert r.status_code == 201
        response = r.json()
        assert response['name'] == name
        assert response['email'] == email

    @pytest.mark.parametrize('number, post_id', [(1, 1), (2, 2)])
    def test_posts_post_id(self, number, post_id):
        url = self.url + f'posts/{number}/comments'
        r = requests.get(url)
        assert r.status_code == 200
        response = r.json()
        for i in range(len(response)):
            assert response[i]['postId'] == post_id

    @pytest.mark.parametrize('number, email', [(1, 'Eliseo@gardner.biz'), (2, 'Presley.Mueller@myrl.com')])
    def test_posts_email(self, number, email):
        url = f'https://jsonplaceholder.typicode.com/posts/{number}/comments'
        r = requests.get(url)
        assert r.status_code == 200
        response = r.json()
        count = 0
        for i in range(len(response)):
            if response[i]['email'] == email:
                count += 1
            assert count == 1