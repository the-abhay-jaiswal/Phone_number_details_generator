import phonenumbers
from phonenumbers import timezone,geocoder,carrier
import qrcode
from PIL import Image

number = input("Enter Phone number (including contry code): ")
phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
car = carrier.name_for_number(phone, "en")
reg = geocoder.description_for_number(phone, "en")
details = phone,time,car,reg
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
qr.add_data(details)
qr.make(fit=True)
img = qr.make_image(fill_colour="black",back_color="white")
img.show()
