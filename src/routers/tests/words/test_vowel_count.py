from src.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_invalid_content_type():
    response = client.post(
        "/vowel_count",
        headers={"Content-Type": "x-www-form-urlencoded"},
    )

    assert response.status_code == 415


def test_valid_payload():
    response = client.post(
        "/vowel_count", json={"words": ["batman", "robin", "coringa"]}
    )

    assert response.status_code == 200
    assert response.json() == {"batman": 2, "robin": 2, "coringa": 3}


def test_empty_word_list():
    response = client.post("/vowel_count", json={"words": []})

    assert response.status_code == 422


def test_null_string():
    response = client.post("/vowel_count", json={"words": ["batman", None]})

    assert response.status_code == 422
