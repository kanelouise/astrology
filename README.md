# astrology
using Python to dive into our charts

`astrology_houses.py` asks users for their sun, moon, and rising signs (only accepts answers with these exact capitalization and spellings: ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']). Then there are two functions: `find_houses` and `moon_phase` which reveal their house placements as well as whether there was a full moon when the person was born. The moon phase calculation is a bit of a crude calculation. Without using a planetary or astrological API, this code makes mathematical assumptions about the moon phase given a user's sun and moon sign. 

At present, this code does not help a user calculate their chart, but rather tell them information about their birth chart.

To run this code, open terminal, navigate to the folder the file is saved, and run `python3 astrology_houses.py`. From there enter your sun, moon, and rising sign.

### Requirements
This script was built using Python 3x and is not compatible with Python 2.

### Maintenance and future projects
1. In order to have a more accurate moon phase calculator, it would be great to do some research about a possible API to reference.
2. Extend the number of placements calculated.
3. Calculate (crudely) a person's  midheaven and descendant.
4. Use Django to create a simple front-end to make the program more pleasant than running it from the terminal.
5. In creating a frontend, it would be great for user input to have a dropdown menu, that way there are fewer ways that user input could result in an error.
6. Add error messages and hints to common misspellings. Also, prompt users to use correct spellings.
