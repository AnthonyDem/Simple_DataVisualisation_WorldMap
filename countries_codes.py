from pygal_maps_world.maps import COUNTRIES
def get_country_code(country_name):
    #retutned for set country her pygal code
    for code,name in COUNTRIES.items():
        if name==country_name:
            return code
        #if country not found return none
        return  None
