from smartphone import Smartphone

catalog = [
    Smartphone('Apple', 'iPhone_15', '+79267081923'),
    Smartphone("Xiaomi", "Mi_12", "+79779876543"),
    Smartphone("Samsung", "Galaxy_S23", "+79158912336"),
    Smartphone("Huawei", "Nova_12_SE", "+79161234567"),
    Smartphone("Nokia", "XR_21", "+79105577889")
]

for phone in catalog:
    print(phone.brand_phone, "-", phone.model_phone, "." , phone.number_phone) 
