import uuid
import time
from utils.api_client import ApiClient
from selenium import webdriver

def before_scenario(context, scenario):
    # ------------------ API ------------------
    context.client = ApiClient()

    # Criar usuário
    if any(tag in scenario.tags for tag in ["criarUsuario", "gerarToken", "autorizarUsuario", "alugarLivros", "detalhesUsuario"]):
        context.user_payload = {
            "userName": f"usuario_{uuid.uuid4().hex[:6]}",
            "password": "SenhaForte@123"
        }
        response = context.client.create_user(
            username=context.user_payload["userName"],
            password=context.user_payload["password"]
        )
        context.user_id = response["userID"]
        context.username = response["username"]
        context.password = context.user_payload["password"]

    # Gerar token
    if any(tag in scenario.tags for tag in ["gerarToken", "autorizarUsuario", "alugarLivros", "detalhesUsuario"]):
        response = context.client.generate_token(
            username=context.username,
            password=context.password
        )
        context.token = response["token"]

    # Carregar lista de livros
    if any(tag in scenario.tags for tag in ["listarLivros", "alugarLivros", "detalhesUsuario"]):
        response = context.client.list_books()
        context.books = response["books"]

    # Alugar livros automaticamente (usando ISBNs fixos)
    if any(tag in scenario.tags for tag in ["alugarLivros", "detalhesUsuario"]):
        context.rent_response = context.client.rent_books(
            user_id=context.user_id,
            username=context.username,
            password=context.password
        )
        time.sleep(1)  # garante que o POST foi processado

    # ------------------ UI ------------------
    # Inicializar driver apenas para cenários com tag 'ui'
    if "ui" in scenario.tags:
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-notifications")
        context.driver = webdriver.Chrome(options=options)

def after_scenario(context, scenario):
    # Fechar navegador se estiver aberto
    if hasattr(context, "driver"):
        try:
            context.driver.quit()
        except Exception:
            pass  # garante que não falhe se o driver já estiver fechado
