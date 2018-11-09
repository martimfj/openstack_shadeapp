from shade import *

simple_logging(debug=True)
conn = openstack_cloud(cloud='martim_openstack')

def get_image(image_name):
    image_list = []
    for image in conn.list_images():
        image_list.append((image['name'], image['id']))
    return [image[1] for image in image_list if image[0] == image_name]

def get_flavor(flavor_name):
    flavor_list = []
    for flavor in conn.list_flavors():
        flavor_list.append((flavor['name'], flavor['id']))
    return [flavor[1] for flavor in flavor_list if flavor[0] == flavor_name]

def get_instances():
    instance_list = []
    for instance in conn.list_servers():
        instance_list.append((instance['name'], instance['id']))
    return instance_list

def define_keypair(keypair_name):
    pub_key_file = '/home/cloud/.ssh/id_rsa.pub'
    if conn.search_keypairs(keypair_name):
        print('Keypair já existe. Pulando import.')
    else:
        print('Criando keypair...')
        conn.create_keypair(keypair_name, open(pub_key_file, 'r').read().strip())
    return keypair_name

def delete_instance(instance_id):
    conn.delete_server(name_or_id=instance_id)

def define_security_group(sec_group_name):
    if conn.search_security_groups(sec_group_name):
        print('Security group already exists. Skipping creation.')
    else:
        print('Creating security group.')
        conn.create_security_group(sec_group_name, 'network access for all-in-one application.')
        conn.create_security_group_rule(sec_group_name, 80, 80, 'TCP')
        conn.create_security_group_rule(sec_group_name, 22, 22, 'TCP')
    return sec_group_name

image_id = get_image("bionic")
flavor_id = get_flavor("m1.small")
instance_name = "all-in-one-final"
key_name = define_keypair('demokey')
sec_group_name = define_security_group('all-in-one')
network_id ='b5326950-875d-450b-bbe9-eac01428eff7'
ex_userdata = '''#!/usr/bin/env bash

curl -L -s https://git.openstack.org/cgit/openstack/faafo/plain/contrib/install.sh | bash -s -- \
-i faafo -i messaging -r api -r worker -r demo
'''

def create_instance(image_id, flavor_id, instance_name, key_name, sec_group_name, network_id, ex_userdata):
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
