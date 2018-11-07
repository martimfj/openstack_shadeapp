from shade import *

simple_logging(debug=True)
conn = openstack_cloud(cloud='martim_openstack')

images = conn.list_images()
flavors =  conn.list_flavors()

image_id = '5d215499-f728-4cfa-b21c-ebdb34a9f4fe'
image = conn.get_image(image_id)

flavor_id = '9dd13582-b003-4c4a-813f-92c71890f4fe'
flavor = conn.get_flavor(flavor_id)
'''
print(image, flavor)

instance_name = 'testing'
testing_instance = conn.create_server(wait=True, auto_ip=True,
    name=instance_name,
    image=image_id,
    flavor=flavor_id,
	network='b5326950-875d-450b-bbe9-eac01428eff7')
print(testing_instance)

instances = conn.list_servers()
for instance in instances:
    print(instance)

conn.delete_server(name_or_id='215b225f-7ed9-46eb-9d83-d76434a575bd')
conn.delete_server(name_or_id='60afee71-186f-43c2-ac20-fce0fb5728fd')
conn.delete_server(name_or_id='f28309fd-a1ec-4284-810f-1ed29433e3ed')

print('Checking for existing SSH keypair...')
keypair_name = 'demokey'
pub_key_file = '/home/cloud/.ssh/id_rsa.pub'

if conn.search_keypairs(keypair_name):
    print('Keypair already exists. Skipping import.')
else:
    print('Adding keypair...')
    conn.create_keypair(keypair_name, open(pub_key_file, 'r').read().strip())

for keypair in conn.list_keypairs():
    print(keypair)
'''

sec_group_name = 'all-in-one'
conn.search_security_groups(sec_group_name)

ex_userdata = '''#!/usr/bin/env bash

curl -L -s https://git.openstack.org/cgit/openstack/faafo/plain/contrib/install.sh | bash -s -- \
-i faafo -i messaging -r api -r worker -r demo
'''
network_id ='b5326950-875d-450b-bbe9-eac01428eff7'
keypair_name = 'demokey'
instance_name = 'all-in-one-final'

testing_instance = conn.create_server(wait=True, auto_ip=False,
    name=instance_name,
    image=image_id,
    flavor=flavor_id,
    key_name=keypair_name,
    security_groups=[sec_group_name],
    userdata=ex_userdata,
	network=network_id)

f_ip = conn.available_floating_ip()
conn.add_ip_list(testing_instance, [f_ip['floating_ip_address']])
print('The Fractals app will be deployed to http://%s' % f_ip['floating_ip_address'] )
