from pygal_maps_world.maps import World
wm=World()

wm.title='North,Cnetral, and South America'

wm.add('North Amreica',['ca','mx','us'])
wm.add('Centeral America',['bz','cr','gt','hn','ni','pa','sv'])
wm.add('South Amrica',['ar','bo','br','cl','co','ec','gf',
                       'gy','pe','py','sr','uy','ve'])

wm.render_to_file('americas.svg')