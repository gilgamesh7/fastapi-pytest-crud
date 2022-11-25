import pytest

import json

from app.api import crud

def test_create_note(test_app, monkeypatch):
    test_request_payload = {
        "title" : "test note title",
        "description" : "test note decsription"
    }

    test_response_payload = {
        "id" : 1,
        "title" : "test note title",
        "description" : "test note decsription"
    }

    async def mock_post(payload):
        return True

    monkeypatch.setattr(crud, "post", mock_post)

    response = test_app.post("/notes/", data=json.dumps(test_request_payload),)

    assert response.status_code == 201

    assert response.json() == test_response_payload