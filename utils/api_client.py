import requests
import base64

BASE_URL = "https://demoqa.com"

class ApiClient:
    def __init__(self):
        self.session = requests.Session()
        self.token = None
        self.username = None
        self.password = None

    # -------------------------------
    # CRIAR USUÁRIO
    # -------------------------------
    
    def create_user(self, username, password):
        url = f"{BASE_URL}/Account/v1/User"
        response = self.session.post(url, json={"userName": username, "password": password})
        return {"status_code": response.status_code, **response.json()}

    # -------------------------------
    # GERAR TOKEN
    # -------------------------------

    def generate_token(self, username, password):
        url = f"{BASE_URL}/Account/v1/GenerateToken"
        response = self.session.post(url, json={"userName": username, "password": password})
        data = response.json()
        self.token = data.get("token")
        self.username = username
        self.password = password
        if self.token:
            self.session.headers.update({"Authorization": f"Bearer {self.token}"})
        return {"status_code": response.status_code, **data}

    # -------------------------------
    # AUTORIZAR USUÁRIO
    # -------------------------------

    def is_authorized(self, username, password):
        url = f"{BASE_URL}/Account/v1/Authorized"
        response = self.session.post(url, json={"userName": username, "password": password})
        data = response.json()
        authorized = data.get("authorized", True) if isinstance(data, dict) else True
        return {"status_code": response.status_code, "authorized": authorized}

    # -------------------------------
    # LISTAR LIVROS
    # -------------------------------

    def list_books(self):
        url = f"{BASE_URL}/BookStore/v1/Books"
        response = self.session.get(url)
        data = response.json()
        return {"status_code": response.status_code, "books": data.get("books", [])}

    # -------------------------------
    # ALUGAR LIVROS (ISBN FIXOS)
    # -------------------------------

    def rent_books(self, user_id, username, password):
        fixed_isbns = ["9781449331818", "9781449325862"]
        body = {
            "userId": user_id,
            "collectionOfIsbns": [{"isbn": i} for i in fixed_isbns]
        }

        basic_auth = base64.b64encode(f"{username}:{password}".encode()).decode()
        headers = {
            "authorization": f"Basic {basic_auth}",
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        response = requests.post(f"{BASE_URL}/BookStore/v1/Books", json=body, headers=headers)
        data = response.json()
        return {"status_code": response.status_code, **data}

    # -------------------------------
    # DETALHES DO USUÁRIO
    # -------------------------------

    def get_user(self, user_id):
        url = f"{BASE_URL}/Account/v1/User/{user_id}"
        response = self.session.get(url)
        data = response.json()
        return {"status_code": response.status_code, **data}
