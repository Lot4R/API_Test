import requests

BASE_URL = "https://postman-echo.com"

# Возвращение сервером отправленных query-параметров
def test_echo_get_params():
    response = requests.get(f"{BASE_URL}/get", params={"id": "123", "key1": "value1", "key2": "value2"})
    assert response.status_code == 200
    data = response.json()
    assert data["args"]["id"] == "123"
    assert data["args"]["key1"] == "value1"
    assert data["args"]["key2"] == "value2"

# GET-запрос без параметров
def test_get_no_params():
    res = requests.get(f"{BASE_URL}/get")
    assert res.status_code == 200
    body = res.json()
    assert body["args"] == {}

# Передача JSON POST запросом
def test_post_json_data():
    payload = {"username": "test_user", "active": True}
    r = requests.post(f"{BASE_URL}/post", json=payload)
    assert r.ok
    result = r.json()
    assert result["data"] == payload

# Отправка обычного текста в теле POST-запроса
def test_post_plain_text():
    text_payload = "какой-нибудь текст"
    headers = {"Content-Type": "text/plain"}
    response = requests.post(f"{BASE_URL}/post", data=text_payload, headers=headers)
    assert response.status_code == 200
    result = response.json()
    assert result["data"] == text_payload

# Передача и возврат кастомных заголовков
def test_custom_headers_echo():
    custom_headers = {
        "X-Custom-Header": "Value1",
        "User-Agent": "TestAgent/1.0"
    }
    res = requests.get(f"{BASE_URL}/get", headers=custom_headers)
    assert res.status_code == 200
    echoed = res.json()["headers"]
    # Возврат заголовка
    assert "x-custom-header" in {k.lower() for k in echoed.keys()}
    assert echoed.get("x-custom-header") == "Value1"