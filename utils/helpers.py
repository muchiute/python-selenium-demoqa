def validate_status(response, expected_status):
    actual_status = response.get("status_code")
    assert actual_status == expected_status, f"Esperado {expected_status}, obtido {actual_status}"
    data = response.copy()
    data.pop("status_code", None)
    return data