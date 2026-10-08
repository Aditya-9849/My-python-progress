# we will create a phone number  [freakin useless project]

def phoneno(country_code, area, first, last):
    return f"{country_code}-{area}-{first}-{last}"

phone_num = phoneno(area="23",first="455",last="444",country_code="+91")
print(phone_num)