from http import HTTPStatus

from fastapi.testclient import TestClient

def test_healthz(client: TestClient) -> None:
    r = client.get("/healthz")
    assert r.status_code == HTTPStatus.OK
