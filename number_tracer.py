# I have made this phone_number tracker which reflects location , time zone and compamy name #
import phonenumbers
from phonenumbers import timezone , geocoder , carrier 

number = input("Enter  Number With Country Code Here: ")

phone = phonenumbers.parse(number)

time = timezone.time_zones_for_number(phone)


car = carrier.name_for_number(phone ,"en")

reg = geocoder.description_for_number(phone , "en")

print(phone)
print(time)
print(car)