from chessdotcom import *
import pprint
## for better display of json
printer = pprint.PrettyPrinter()

## name to be edited later
##user_name = "momo_gogo"

user_name = input("Enter User Name: ")

## 
response = get_player_stats(user_name)

printer.pprint(response.json)