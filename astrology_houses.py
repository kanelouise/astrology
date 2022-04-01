signs = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']
ind = {}
planets = ("sun", "moon", "rising")
for planet in planets:
	place = input(f"What is your {planet} sign? ")
	sign_count = signs.index(place)
	ind[f"{planet}"] = (place,sign_count)

def find_houses(sign = ind['rising'][0], rising_ind = ind['rising'][1], signs = signs):
  houses_list = signs[rising_ind:] + signs[:rising_ind]
  match_house = ["1st house" , '2nd house', '3rd house', '4th house', '5th house', '6th house', '7th house', '8th house', '9th house', '10th house', '11th house', '12th house']
  match = [f"{house_num}: {house_name}" for (house_num,house_name) in zip(match_house, houses_list)]
  return(match)

def moon_phase(sun = ind['sun'], sun_ind = ind['sun'][1], moon = ind['moon'], moon_ind = ind['moon'][1]):
  calc = moon_ind - sun_ind
  if calc == 6 or calc == -6:
    return("You were born during a full moon.")
  else:
    return("You were not born during a full moon.")


