from shade import *

simple_logging(debug=True)
conn = openstack_cloud(cloud='martim_openstack')

images = conn.list_images()
flavors =  conn.list_flavors()

image_id = '5d215499-f728-4cfa-b21c-ebdb34a9f4fe'
image = conn.get_image(image_id)

flavor_id = '9dd13582-b003-4c4a-813f-92c71890f4fe'
flavor = conn.get_flavor(flavor_id)
print(flavor)
