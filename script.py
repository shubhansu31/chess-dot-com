from chessdotcom import *
import json
import pprint
printer = pprint.PrettyPrinter()

user_name = "momo_gogo"
user_details = get_player_profile(user_name).json['player']
user_country = user_details['country']
user_country = user_country[len(user_country) - 2 : len(user_country)]
user_followers = user_details['followers']

print(user_country)
print(user_followers)
printer.pprint(user_details)