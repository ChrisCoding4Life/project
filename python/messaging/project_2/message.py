import requests

print("phone area codes: \n 804 \n     Chesterfield \n     Henrico\n     Hopewell\n      Mechanicsville\n       Powhatan\n      Midlothian\n        Petersburg\n and Colonial Heights")
area_code = input("area code?: ")
phone = input("last 7 digits of the number you want to text?: ")

message = input("message?: ")
resp = requests.post('https://textbelt.com/text', {
  'phone': f'{area_code}{phone}',
  'message': f'{message}',
  'key': 'textbelt',
})
print(resp.json())