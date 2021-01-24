import json

from lib.api.api_test_case import APITestCase
class TestClass(APITestCase):
    def test_verify_api_start_with_empty_store(self):
        book_list=json.loads(self.get_books().content)
        assert len(book_list) == 0
    def test_verify_title_is_required(self):
        params={"author":"Test Author"}
        response = self.put_a_book(params)
        assert response.status_code == 400
        assert json.loads(response.content)["error"] == "Field 'title' is required."
    def test_verify_author_is_required(self):
        params={"title":"Test Title"}
        response = self.put_a_book(params)
        assert response.status_code == 400
        assert json.loads(response.content)["error"] == "Field 'author' is required."
    def test_verify_title_cannot_be_empty(self):
        params={"author":"Test Author","title":""}
        response = self.put_a_book(params)
        assert response.status_code == 400
        assert json.loads(response.content)["error"] == "Field 'title' cannot be empty."
    def test_verify_author_cannot_be_empty(self):
        params={"author":"","title":"Test Title"}
        response = self.put_a_book(params)
        assert response.status_code == 400
        assert json.loads(response.content)["error"] == "Field 'author' cannot be empty."
    def test_verify_id_field_is_read_only(self):
        params = {"id":1234,"author": "", "title": "Test Title"}
        response = self.put_a_book(params)
        assert response.status_code == 400
    def test_verify_book_can_be_created(self):
        params = {"author": "Test Author", "title": "Test Title"}
        response = self.put_a_book(params)
        book=json.loads(response.content)
        assert book["author"] == params ["author"]
        assert book["title"] == params ["title"]
        response=self.get_a_book(book["id"])
        assert json.loads(response.content) == book
    def test_verify_duplicate_book_cannot_be_created(self):
        existing_book=json.loads(self.get_books().content)[0]
        params = {"author": existing_book["author"], "title": existing_book["title"]}
        response = self.put_a_book(params)
        assert response.status_code == 400
        assert json.loads(response.content)["error"] == "Another book with similar title and author already exists."
