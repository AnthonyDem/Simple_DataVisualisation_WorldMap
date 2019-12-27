import json
from countries_codes import get_country_code
from pygal_maps_world.maps import World
from pygal.style import RotateStyle

filename='population_data.json'
with open(filename) as f:
    pop_data=json.load(f)

#output population from 2010
cc_populations={}
for pop_dict in pop_data:
    if pop_dict['Year']=='2010':
        country_name=pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code=get_country_code(country_name)
        if code:
            cc_populations[code]=population

#group by 3 population level
cc_pops_1, cc_pops_2, cc_pops_3= {} , {} , {}
for cc,pop in cc_populations.items():
    if pop< 10000000:
        cc_pops_1[cc]=pop
    elif pop < 1000000000:
        cc_pops_2[cc]=pop
    else:
        cc_pops_3[cc]=pop

#cheking countries count on each level
print(len(cc_pops_1),len(cc_pops_2),len(cc_pops_3))

wm_style=RotateStyle('#336699')
wm=World(style=wm_style)
wm.title='World Population in 2010, by Country'
wm.add('0-10m',cc_pops_1)
wm.add('10m-10b',cc_pops_2)
wm.add('>1bn',cc_pops_3)
wm.render_to_file('world_populations.svg')