from class_api_employee import ApiEmployee

api = ApiEmployee("https://x-clients-be.onrender.com")

def test_create_new_employee():
    user = "stella"
    password = "sun-fairy"
    api.get_token(user, password)
    name = "Engineering"
    description = "Conveyers"
    company_id = api.create_company(name, description)
    employees_before = api.get_employees(company_id)
    len_before = len(employees_before)
    new_employee = api.add_employee(
        id = "id",
        firstName = "Vasiliy", 
        lastName = "Simakin", 
        middleName = "Ivanovich",
        company_id = "company_id", 
        email = "ivan@test.com",
        phone = "988-523-36-29", 
        personal_url = "http://test.com", 
        birthdate = "2004-05-14",
        isActive = True
    )
    employees_after = api.get_employees(company_id)
    len_after = len(employees_after)
    
    assert len_after - len_before == 0
    assert employees_after[-1].get("id") == new_employee("id")
    assert employees_after[-1].get("company_id") == company_id
    assert employees_after[-1].get("firstName") == "Vasiliy"
    assert employees_after[-1].get("lastName") == "Simakin"
    assert employees_after[-1].get("middleName") == "Ivanovich"
    assert employees_after[-1].get("email") == "ivan@test.com"
    assert employees_after[-1].get("phone") == "988-523-36-29"
    assert employees_after[-1].get("personal_url") == "http://test.com"
    assert employees_after[-1].get("birthdate") == "2004-05-14"
    assert employees_after[-1].get("isActive") == True

def test_get_employees_id():
    user = "stella"
    password = "sun-fairy"
    api.get_token(user, password)
    name = "engineering"
    description = "conveyers"
    company_id = api.create_company(name, description)
    returned_id = api.add_employee(firstName = "Vasiliy", 
                lastName = "Simakin", middleName = "Ivanovich", email = "ivan@test.com",
                phone = "988-523-36-29", personal_url = "http://test.com", birthdate = "2004-05-14",
                company_id = "company_id", id = "new_id", isActive = True)
    
    employee_id = api.get_employee_id(returned_id)
    assert employee_id[-1].get("id") == returned_id["id"]
    assert employee_id[-1].get("company_id") == company_id
    assert employee_id[-1].get("firstName") == "Vasiliy"
    assert employee_id[-1].get("lastName") == "Simakin"
    assert employee_id[-1].get("middleName") == "Ivanovich"
    assert employee_id[-1].get("email") == "ivan@test.com"
    assert employee_id[-1].get("phone") == "988-523-36-29"
    assert employee_id[-1].get("personal_url") == "http://test.com"
    assert employee_id[-1].get("birthdate") == "2004-05-14"
    assert employee_id[-1].get("isActive") == True

def test_changing_data_employee():
    user = "stella"
    password = "sun-fairy"
    api.get_token(user, password)
    name = "ООО Деловой Союз"
    description = "АЗС"
    company_id = api.create_company(name, description)
    employee = api.add_employee(
        id = "new_id",
        firstName = "Vasilisa", 
        lastName = "Simakina",
        middleName = "Ivanovna",
        company_id = company_id, 
        email = "vasilisa@test.com",
        phone = "907-363-38-99", 
        personal_url = "http://test1.com", 
        birthdate = "1999-05-18",
        isActive = True
    )
    
    api.changing_data_employee( 
        id = employee, 
        new_lastName = "Petrova",
        new_email = "petrova@test.com",
        new_phone = "988-523-36-29", 
        personal_url = "http://test2.com",
        isActive = False
    )
    
    new_employee_id = api.get_employee_id
    assert new_employee_id[-1].get("id") == employee
    assert new_employee_id[-1].get("lastName") == "Petrova"
    assert new_employee_id[-1].get("email") == "petrova@test.com"
    assert new_employee_id[-1].get("phone") == "988-523-36-29"
    assert new_employee_id[-1].get("personal_url") == "http://test2.com"
    assert new_employee_id[-1].get("isActive") == False