import uuid
from behave import given, when, then
from utils.api_client import ApiClient
from utils.helpers import validate_status

# -------------------------------
# CRIAR USUÁRIO
# -------------------------------

@given("que eu possuo dados válidos de usuário")
def step_impl(context):
    context.user_payload = {
        "userName": f"usuario_{uuid.uuid4().hex[:6]}",
        "password": "SenhaForte@123"
    }

@when("eu envio a requisição para criar o usuário")
def step_impl(context):
    response = context.client.create_user(
        username=context.user_payload["userName"],
        password=context.user_payload["password"]
    )
    data = validate_status(response, 201)
    context.user_id = data["userID"]
    context.username = data["username"]
    context.password = context.user_payload["password"]

@then("o usuário deve ser criado com sucesso")
def step_impl(context):
    assert context.user_id is not None
    assert context.username == context.user_payload["userName"]

# -------------------------------
# GERAR TOKEN
# -------------------------------

@given("que eu possuo credenciais válidas")
def step_impl(context):
    pass

@when("eu envio a requisição para gerar o token")
def step_impl(context):
    response = context.client.generate_token(
        username=context.username,
        password=context.password
    )
    data = validate_status(response, 200)
    context.token = data.get("token")
    assert context.token is not None

@then("devo receber um token válido")
def step_impl(context):
    assert isinstance(context.token, str)

# -------------------------------
# AUTORIZAR USUÁRIO
# -------------------------------

@given("que eu possuo um token de acesso válido")
def step_impl(context):
    assert hasattr(context, "token")

@when("eu verifico a autorização do usuário")
def step_impl(context):
    response = context.client.is_authorized(
        username=context.username,
        password=context.password
    )
    data = validate_status(response, 200)
    context.authorized = data["authorized"]

@then("o usuário deve estar autorizado")
def step_impl(context):
    assert context.authorized is True

# -------------------------------
# LISTAR LIVROS
# -------------------------------

@given("que existem livros cadastrados")
def step_impl(context):
    pass

@when("eu solicito a lista de livros")
def step_impl(context):
    response = context.client.list_books()
    data = validate_status(response, 200)
    context.books = data["books"]

@then("devo receber a lista de livros disponíveis")
def step_impl(context):
    assert len(context.books) > 0

# -------------------------------
# ALUGAR LIVROS
# -------------------------------

@given("que eu possuo dois livros disponíveis")
def step_impl(context):
    assert len(context.books) >= 2

@when("eu envio a requisição para alugar os livros")
def step_impl(context):
    response = context.client.rent_books(
        user_id=context.user_id,
        username=context.username,
        password=context.password
    )
    data = validate_status(response, 201)
    context.rent_response = data

@then("os livros devem ser adicionados ao meu usuário")
def step_impl(context):
    rented_isbns = [book["isbn"] for book in context.rent_response["books"]]
    assert "9781449331818" in rented_isbns
    assert "9781449325862" in rented_isbns
    assert len(rented_isbns) >= 2

# -------------------------------
# DETALHES DO USUÁRIO
# -------------------------------

@given("que eu possuo um usuário com livros alugados")
def step_impl(context):
    assert hasattr(context, "user_id")

@when("eu consulto os detalhes do usuário")
def step_impl(context):
    response = context.client.get_user(context.user_id)
    data = validate_status(response, 200)
    context.user_details = data

@then("devo ver os dados do usuário e os livros alugados")
def step_impl(context):
    rented_isbns = [book["isbn"] for book in context.user_details["books"]]
    assert "9781449331818" in rented_isbns
    assert "9781449325862" in rented_isbns
    assert len(rented_isbns) >= 2
