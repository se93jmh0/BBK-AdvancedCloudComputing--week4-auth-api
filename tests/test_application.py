
def test_home(client):
    home_result = client.get("/")

    assert home_result.status_code == 200
    assert home_result.json()["message"] == "Week 4 auth API is running"
