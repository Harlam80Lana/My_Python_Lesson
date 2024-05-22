from class_api_employee_ import ApiEmployee

api = ApiEmployee("https://x-clients-be.onrender.com")

def test_get_list():
    user = "stella"
    password = "sun-fairy"
    api.get_token(user, password)
    name = "Svetlana"
    description = "HW 8"
    result = api.create_company(name, description)
    new_id = result
    body = api.get_employees(f'?company={new_id}')
    assert len(body) > 0


def test_create_new_employee():
    name = "Engineering"
    description = "Conveyers"
    company_id = api.create_company(name, description)
    employees_before = api.get_employees(company_id)
    len_before = len(employees_before)
    new_employee = api.add_employee(
        id = 0,
        firstName = "Vasiliy",
        lastName = "Simakin",
        middleName = "Ivanovich",
        company_id = company_id,  
        email = "ivan@test.com",
        phone = "988-523-36-29",
        url = "http://test.com",
        birthdate = "2004-05-14",
        isActive = True
    )
    employees_after = api.get_employees(company_id)
    len_after = len(employees_after)

    assert len_after - len_before == 1
    assert employees_after[-1].get("companyId") == company_id
    assert employees_after[-1].get("firstName") == "Vasiliy"
    assert employees_after[-1].get("lastName") == "Simakin"
    assert employees_after[-1].get("middleName") == "Ivanovich"
    assert employees_after[-1].get("phone") == "988-523-36-29"
    assert employees_after[-1].get("birthdate") == "2004-05-14"
    assert employees_after[-1].get("isActive") == True


def test_changing_data_employee():
    user = "stella"
    password = "sun-fairy"
    api.get_token(user, password)
    name = "ООО Деловой Союз"
    description = "АЗС"
    company_id = api.create_company(name, description)
    employee = api.add_employee(
        id = 0,
        firstName = "Vasilisa",
        lastName = "Simakina",
        middleName = "Ivanovna",
        company_id = company_id,
        email = "vasilisa@test.com",
        phone = "907-363-38-99",
        url = "http://test.com",
        birthdate = "1999-05-18",
        isActive = True
    )
    new_employee_id = api.changing_data_employee(
        id=employee["id"],
        new_lastName = "Petrova",
        new_email = "petrova@test.com",
        new_phone = "988-523-36-29",
        isActive = False
    )

    assert new_employee_id.get("id") == employee["id"]
    assert new_employee_id.get("email") == "petrova@test.com"
    assert new_employee_id.get("isActive") == False