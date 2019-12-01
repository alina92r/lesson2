import ephem
import datetime

#mars=ephem.Mars('2000/01/01')
#const = ephem.constellation(mars)
#print(const)

a=str(input("rrr     "))


text=a.split(" ")
print(text)
planet=text[1].capitalize()
print(planet)
print(datetime.today())
#planet_text=ephem.planet('datetime.today()')
#print(planet_text)
#const=ephem.constellation(planet_text)
#print(const)
#update.message.reply_text(const)