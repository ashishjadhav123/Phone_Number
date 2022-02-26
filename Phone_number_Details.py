import phonenumbers
from phonenumbers import carrier, geocoder, timezone

mobile_no = input("Enter mobile number with Country code: ")
mobile_no = phonenumbers.parse(mobile_no)

print(timezone.time_zones_for_number(mobile_no))    # Timezone

print(carrier.name_for_number(mobile_no, 'en'))     # Carrier

print(geocoder.description_for_number(mobile_no, 'en'))     # Region

print("Valid mobile number : ",phonenumbers.is_valid_number(mobile_no))     # Validating

print("Checking possibility of number : ",phonenumbers.is_possible_number(mobile_no))       # Possibility