# Infraestrutura de Monitoramento e Controle de Acesso Wi-Fi

Este projeto apresenta a implantação de uma infraestrutura de monitoramento e gerenciamento de acesso para rede Wi-Fi em ambiente de produção.

## Arquitetura

A infraestrutura foi implantada em um servidor **HPE ProLiant ML110 Gen9** utilizando **Citrix XenServer** como hypervisor.

Foram criadas duas máquinas virtuais principais:

### Firewall / Gateway
**Tecnologia:** pfSense  
Responsabilidades:
- Firewall da rede
- Roteamento e gateway de internet
- Controle de acesso via Captive Portal
- Gerenciamento de usuários da rede Wi-Fi

### Servidor de Monitoramento
**Tecnologia:** Oracle Linux 9.2 + Zabbix  
Responsabilidades:
- Monitoramento da infraestrutura de rede
- Mapa visual da topologia da rede
- Monitoramento de access points e switches
- Identificação de dispositivos offline
- Configuração de alertas em tempo real (ex: Telegram, e-mail) de forma conceitual

## Funcionalidades
- Virtualização da infraestrutura de rede
- Firewall e gateway centralizado
- Controle de acesso de usuários via Captive Portal
- Monitoramento de dispositivos de rede
- Mapa visual de topologia da rede
- Alertas automáticos em tempo real (conceitual)

## Tecnologias Utilizadas
- Citrix XenServer
- pfSense
- Oracle Linux 9.2
- Zabbix
- Telegram Bot API (integração conceitual para alertas)

## Configurações e Diagramas
- **configs/pfsense_config.xml** → Backup de configuração pfSense
- **configs/zabbix_templates/** → Templates de monitoramento Zabbix
- **diagrams/network_topology.png** → Diagrama visual da topologia da rede

## Como usar
1. Restaurar os templates e configurações no pfSense e Zabbix.
2. Configurar alertas conforme necessidade (Telegram, e-mail).
3. Validar conectividade e monitoramento da rede.
