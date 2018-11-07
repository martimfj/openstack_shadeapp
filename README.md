# Openstack Shade App
Esse projeto é uma reprodução do tutorial de Getting Started, que pode ser encontrado no site do openstack [site do Openstack.](https://developer.openstack.org/firstapp-shade/getting_started.html) Que tem como objetivo ensinar a programar utilizando componentes do Openstack.

## Choose your OpenStack SDK
Escolhi o Shade, que utiliza Python, uma linguagem que tenho mais familiaridade e noções avançadas. 

* [Shade](https://docs.openstack.org/infra/shade/): A Python-based library developed by OpenStack Infra team. Use it to operate multiple OpenStack clouds.	

## What you need
Para conseguir as credenciais, foi preciso acessar o dashboard Horizon, acessar a aba *API Access* e baixar o RC File.

## How you interact with OpenStack
Para adicionar as credenciais juntamente com as existentes:
* `nano ~cloud/.config/openstack/clouds.yaml`

## Launch an instance


