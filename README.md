# 📊 Infraestrutura de Monitoramento e Controle de Acesso Wi-Fi com Zabbix + ChatOps

## 📌 Descrição

Este projeto apresenta a implantação de uma infraestrutura completa de **monitoramento e controle de acesso para rede Wi-Fi em ambiente de produção**, evoluindo para um modelo de **observabilidade com integração via Telegram (ChatOps)**.

A solução permite:

- Monitoramento contínuo da rede
- Controle de acesso de usuários
- Visualização da topologia
- Alertas automáticos em tempo real
- Consulta interativa da infraestrutura via Telegram

---

## 🏗️ Arquitetura

A infraestrutura foi implantada em um servidor:

- **HPE ProLiant ML110 Gen9**
- **Hypervisor:** Citrix XenServer

Foram provisionadas duas máquinas virtuais principais:

---

### 🔐 Firewall / Gateway
**Tecnologia:** pfSense  

Responsável por:
- Firewall da rede  
- Roteamento e gateway de internet  
- Controle de acesso via Captive Portal  
- Gerenciamento de usuários da rede Wi-Fi  

---

### 📊 Servidor de Monitoramento
**Tecnologia:** Oracle Linux 9.2 + Zabbix  

Responsável por:
- Monitoramento da infraestrutura de rede  
- Mapa visual da topologia (Network Map)  
- Monitoramento de access points e switches (SNMP)  
- Identificação de dispositivos offline  
- Geração de alertas em tempo real  

---

## 🤖 Integração ChatOps (Telegram)

Como evolução do projeto, foi implementada uma camada de **interação via Telegram**, permitindo operação e consulta da rede em tempo real.

Fluxo:

Dispositivos de Rede ] ↓ Zabbix ↓ API / Script Python ↓ Telegram Bot (ChatOps) ↓ Usuário

---

## 🚀 Funcionalidades

### Monitoramento e Infraestrutura
- Virtualização da infraestrutura de rede  
- Firewall e gateway centralizado  
- Controle de acesso via Captive Portal  
- Monitoramento de dispositivos de rede  
- Mapa visual de topologia  
- Identificação de falhas em tempo real  

### Automação e ChatOps
- 🔔 Envio automático de alertas via Telegram  
- 💬 Interação com o ambiente via comandos  
- 📡 Consulta de status da rede em tempo real  
- ⚠️ Listagem de alertas ativos  
- 🌐 Identificação de dispositivos offline  
- 📈 Exibição de métricas (download/upload)  

---

## 🤖 Comandos disponíveis

| Comando     | Descrição |
|------------|----------|
| `/alertas` | Lista alertas ativos |
| `/status`  | Status geral da rede |
| `/rede`    | Resumo da infraestrutura |
| `/host`    | Consulta detalhada de um host |

---

## 🔧 Tecnologias utilizadas

- **Citrix XenServer** → Virtualização  
- **pfSense** → Firewall / Gateway / Captive Portal  
- **Oracle Linux 9.2** → Sistema operacional servidor  
- **Zabbix** → Monitoramento e observabilidade  
- **Python** → Integração e automação  
- **Telegram Bot API** → Interface ChatOps  

---

## 📡 Objetivos da Solução

- Aumentar a visibilidade da rede  
- Reduzir o tempo de detecção de falhas (MTTD)  
- Melhorar o tempo de resposta a incidentes (MTTR)  
- Centralizar controle e monitoramento  
- Permitir operação remota via chat  

---

## 📈 Resultados

- Monitoramento acessível via celular  
- Resposta mais rápida a incidentes  
- Redução de dependência de acesso direto ao servidor  
- Melhor gestão de usuários da rede Wi-Fi  
- Maior controle operacional da infraestrutura  

---

## 📂 Estrutura do Repositório (Em breve será disponibilizado)

configs/ pfsense_config.xml /zabbix_templates/
diagrams/ network_topology.png
scripts/ bot_telegram.py

---

## ⚙️ Como utilizar

1. Restaurar configurações do pfSense (`pfsense_config.xml`)  
2. Importar templates no Zabbix  
3. Configurar SNMP nos dispositivos de rede  
4. Ajustar scripts Python com credenciais e API do Zabbix  
5. Configurar bot do Telegram  
6. Validar comunicação e alertas  

---

## 🧠 Conceitos aplicados

- Virtualização de infraestrutura  
- Observabilidade  
- ChatOps  
- Automação de monitoramento  
- Gerenciamento de acesso à rede  
- Monitoramento proativo  

---

## 🏷️ Tags

`zabbix` `pfsense` `chatops` `networking` `python` `automation` `infraestrutura` `monitoramento` `virtualization`

---

## 👨‍💻 Autor

Projeto desenvolvido como implementação prática de monitoramento, controle de acesso e automação em ambiente de rede real em produção atualmente.