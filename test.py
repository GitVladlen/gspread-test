import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name('key.json', scope)

gc = gspread.authorize(credentials)

ss = gc.open("TextEncountersRegister")

ws = ss.get_worksheet(0)

for value in ws.get_all_values():
	print(value)