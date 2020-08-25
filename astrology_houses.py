signs = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']


def find_houses():
  global rising_sign
  rising_sign = input("What is your rising sign? ")
  global rising_sign_index
  rising_sign_index = signs.index(rising_sign)
  global houses_list
  houses_list = signs[rising_sign_index:] + signs[:rising_sign_index]
  match_house = ["1st house" , '2nd house', '3rd house', '4th house', '5th house', '6th house', '7th house', '8th house', '9th house', '10th house', '11th house', '12th house']
  match =  [str(house_num) + ": " + str(house_name) for (house_num,house_name) in zip(match_house, houses_list)]
  return(match)

  
def moon_phase():
  global sun_sign
  sun_sign = input("What is your sun sign? ")
  global moon_sign
  moon_sign = input ("What is your moon sign? ")
  sun_sign_index = signs.index(sun_sign)
  sun_list = signs[sun_sign_index:] + signs[:sun_sign_index]
  print(sun_sign_index)
  print(sun_list)
  sun_sign_index = sun_list.index(sun_sign)
  print(sun_sign_index)
  moon_sign_index = sun_list.index(moon_sign)
  print(moon_sign_index)
  global calc
  calc = 0 - moon_sign_index
  print(calc)
  if calc == 6:
    return("You were born during a full moon.")
  elif calc == -6:
    return("You were born during a full moon.") 
  else:
    return("You were not born during a full moon.")
  return(sign_calc)


#want to create a list that holds the values of 
def sign_calc(calc):
  global sign_calc
  sign_calc = []
  sign_calc.append(calc)

