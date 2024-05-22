import requests

class ApiEmployee:
    url = "https://x-clients-be.onrender.com"

    def __init__(self, url):
        self.url = url

    def get_token(self, user="raphael", password="cool-but-crude"):
        creds = {
            "username": user,
            "password": password
        }
        resp = requests.post(self.url + '/auth/login', json=creds)
        self.user_token = resp.json()["userToken"]
        return self.user_token

    def create_company(self, name, description):
        company = {
            "name": name,
            "description": description
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url + '/company', json=company, headers=my_headers)
        return resp.json().get("id")

    def get_employees(self, company_id):                     
        params = {'company': company_id}
        resp = requests.get(self.url + '/employee', params=params)   
        return resp.json()

    def add_employee(self, id, company_id, firstName, lastName, middleName, email, url, phone, birthdate, isActive):            
        employee_data = {
            "id": id,
            "companyId": company_id,
            "firstName": firstName,
            "lastName": lastName,
            "middleName": middleName,
            "email": email,
            "url": url,
            "phone": phone,
            "birthdate": birthdate,
            "isActive": isActive
        }
        if company_id is None:
            company_id = self.create_company("Name", "Description")
        if not all([firstName, lastName, company_id, phone, birthdate]):
            raise ValueError("Не запонено обязательное поле")
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url + '/employee', json=employee_data, headers=my_headers)
        return resp.json()

    def get_employee_id(self, id):
        resp = requests.get(self.url + f'/employee/{id}')
        return resp.json()
        
    def changing_data_employee(self, id, new_lastName, new_email,  new_phone, isActive):                          
        employee_new_data = {
            "lastName": new_lastName,
            "email": new_email,
            "phone": new_phone,
            "isActive": isActive
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.patch(self.url + f'/employee/{id}',
                              headers=my_headers, json=employee_new_data)
        return resp.json()