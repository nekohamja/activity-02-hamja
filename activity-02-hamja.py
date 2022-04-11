Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#charizard vs feraligatr
charizard = 90
feraligatr = 95
modifier = round((1 * 1 * 1 * 2 * 0.85 * 1.5 * 0.25 ),2)
damage = round(((((((2*90)/5)+2)*110*(205/188))/50)+2),2)
tdamage = round ((damage * modifier),2)
print('Damage Dealt: ', tdamage)
Damage Dealt:  59.62
