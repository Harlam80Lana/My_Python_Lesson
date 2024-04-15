from address import Address
from mailing import Mailing

to_address = Address('164170', 'Мирный', 'Ленина', 29, 4)
from_address = Address("142200", 'Серпухов', 'Весенняя', 160, 36)
my_mailing = Mailing(to_address, from_address, 1200,'881401')

print(f'Отправление № {my_mailing.usertrack}; Из индекс:{my_mailing.from_address.index}, г.{my_mailing.from_address.city}, ул.{my_mailing.from_address.street}, дом {my_mailing.from_address.house}, кв.{my_mailing.from_address.apartment}; В индекс:{my_mailing.to_address.index}, г.{my_mailing.to_address.city}, ул.{my_mailing.to_address.street}, дом {my_mailing.to_address.house}, кв.{my_mailing.to_address.apartment}. Стоимость {my_mailing.cost} рублей')