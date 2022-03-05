# Test your FastAPI endpoints
# TODO: Add more unit tests

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_fcfs_home():
    response = client.get("/fcfs/")
    assert response.status_code == 200
    assert response.json() == {"name": "First Come First Serve"}


def test_fcfs_schedule():
    response = client.get("/fcfs/schedule", data="[{\"executionTime\": 1,\"period\": 8,\"arrivalTime\": 8,"
                                                 "\"deadline\": 0}]")
    assert response.status_code == 200
    assert response.json() == {"schedule": [0, 0, 0, 0, 0, 0, 0, 0], "lcm": 8}