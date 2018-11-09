# Openstack Shade App
Esse projeto é uma reprodução do tutorial de Getting Started, que pode ser encontrado no site do openstack [site do Openstack.](https://developer.openstack.org/firstapp-shade/getting_started.html) Que tem como objetivo ensinar a programar utilizando componentes do Openstack.

## Escolha de um OpenStack SDK
Escolhi o Shade, que utiliza Python, uma linguagem que tenho mais familiaridade e noções avançadas. 

* [Shade](https://docs.openstack.org/infra/shade/): A Python-based library developed by OpenStack Infra team. Use it to operate multiple OpenStack clouds.	

## Requerimentos
Para conseguir as credenciais, foi preciso acessar o dashboard Horizon, acessar a aba *API Access* e baixar o RC File.

## Credenciais OpenStack
Para adicionar as credenciais juntamente com as existentes:
* `nano ~cloud/.config/openstack/clouds.yaml`
```
clouds:
  openstack:
    auth:
      auth_url: http://192.168.1.33:5000/v3
      username: "Hugo"
      project_id: e6b2220a057049c4b6fd78444dbd7d71
      project_name: "HugoSuperProj"
      user_domain_name: "admin_domain"
      password: "123456"
    region_name: "RegionOne"
    interface: "public"
    identity_api_version: 3
  martim_openstack:
    auth:
      auth_url: http://192.168.1.33:5000/v3
      username: "martim"
      project_id: f0263df0ae984f50b74204a1f920fc0f
      project_name: "MartimProj"
      user_domain_name: "admin_domain"
      password: "123456"
    region_name: "RegionOne"
    interface: "public"
    identity_api_version: 3
```

## Launch de uma instância



