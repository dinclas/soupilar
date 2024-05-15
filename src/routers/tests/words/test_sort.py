from src.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_invalid_content_type():
    response = client.post(
        "/vowel_count",
        headers={"Content-Type": "x-www-form-urlencoded"},
    )

    assert response.status_code == 415


def test_valid_payload_asc():
    response = client.post(
        "/sort", json={"words": ["batman", "robin", "coringa"], "order": "asc"}
    )

    assert response.status_code == 200
    assert response.json() == ["batman", "coringa", "robin"]


def test_valid_payload_desc():
    response = client.post(
        "/sort", json={"words": ["batman", "robin", "coringa"], "order": "desc"}
    )

    assert response.status_code == 200
    assert response.json() == ["robin", "coringa", "batman"]


def test_invalid_words_null_string():
    response = client.post("/sort", json={"words": ["batman", None], "order": "desc"})

    assert response.status_code == 422


def test_invalid_empty_words():
    response = client.post("/sort", json={"words": [], "order": "desc"})

    assert response.status_code == 422


def test_invalid_order_value():
    response = client.post("/sort", json={"words": ["batman"], "order": "foo"})

    assert response.status_code == 422


def test_invalid_missing_order():
    response = client.post("/sort", json={"words": ["batman"]})

    assert response.status_code == 422


def test_invalid_missing_words():
    response = client.post("/sort", json={"order": "asc"})

    assert response.status_code == 422
