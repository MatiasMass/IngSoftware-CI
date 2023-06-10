import html
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.text == """<html>
<head>
    <title>Item Details</title>
</head>
<body>
    <h1>FastAPI is working</h1>
</body>
</html>"""


