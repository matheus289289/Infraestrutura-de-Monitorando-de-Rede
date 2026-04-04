# -*- coding: utf-8 -*-
import requests
import time

# ===== CONFIG =====
TELEGRAM_TOKEN = "SEU_TOKEN"
CHAT_ID = "SEU_ID"

ZABBIX_URL = "http://IP_ZABBIX/zabbix/api_jsonrpc.php"
ZABBIX_TOKEN = "SEU_TOKEN_ZABBIX"            

HOST_NAME = "HOSTNAME_DO_MONITORAMENTO"

# Interfaces
ITEM_DOWNLOAD = "net.if.in[ifInOctets.X]"
ITEM_UPLOAD = "net.if.out[ifOutOctets.X]"
ITEM_PING = "icmpping"
# ==================

# ===== Funcoes Zabbix =====
def zabbix_api(method, params):
    url = ZABBIX_URL
    headers = {
        "Content-Type": "application/json-rpc",
        "Authorization": f"Bearer {ZABBIX_TOKEN}" # Novo padrão Zabbix 7
    }
    payload = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "id": 1
    }
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        return response.json()
    except Exception as e:
        print(f"Erro na conexao: {e}")
        return {"result": []}

def get_host_id(hostname):
    # Tenta listar TODOS os hosts que este Token tem acesso
    result = zabbix_api("host.get", {"output": ["hostid", "host", "name"]})
    
    hosts = result.get("result", [])
    
    if not hosts:
        print("DEBUG: O Token nao tem acesso a NENHUM host ou a lista esta vazia!")
        return None

    print("--- HOSTS DISPONIVEIS PARA ESTE TOKEN ---")
    for h in hosts:
        print(f"ID: {h['hostid']} | Nome Interno: {h['host']} | Nome Visivel: {h['name']}")
        # Busca parcial (ignora maiusculas/minusculas)
        if hostname.lower() in h['host'].lower() or hostname.lower() in h['name'].lower():
            print(f"-> SUCESSO: Usando ID {h['hostid']}")
            return h['hostid']
    
    print("-----------------------------------------")
    return None

def get_item_value(key):
    host_id = get_host_id(HOST_NAME)
    if not host_id:
        print("DEBUG: host_id não encontrado!")
        return 0

    result = zabbix_api("item.get", {
        "filter": {"key_": key},
        "output": ["lastvalue", "name", "key_"],
        "hostids": [host_id],
        "limit": 1
    })

    if result.get("result"):
        try:
            return float(result["result"][0]["lastvalue"])
        except:
            return 0
    return 0

def get_triggers():
    result = zabbix_api("trigger.get", {
        "filter": {"value": 1},
        "output": ["description", "priority"]
    })
    return result.get("result", [])

# ===== Funcoes Bot =====
def get_status():
    try:
        download = float(get_item_value(ITEM_DOWNLOAD) or 0)
        upload = float(get_item_value(ITEM_UPLOAD) or 0)
        ping = float(get_item_value(ITEM_PING) or 0)

        download_mbps = download / 1_000_000
        upload_mbps = upload / 1_000_000

        return (
            "📡 STATUS DA REDE\n\n"
            f"🖥️  Host: {HOST_NAME}\n\n"
            f"⬇️  Download: {download_mbps:.2f} Mbps\n"
            f"⬆️  Upload: {upload_mbps:.2f} Mbps\n"
            f"📶 Ping: {ping*1000:.0f} ms\n"  #Falta corrigir 
        )
    except Exception as e:
        return f"❌ Erro ao calcular status: {e}"

def get_help():
    return (
        "📋  COMANDOS DISPONÃVEIS\n\n"
        "📊  /status - Uso de banda + ping\n"
        "🚨 /alertas - Problemas ativos\n"
        "❓ /help - Ajuda\n"
    )

def send_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    r = requests.post(url, data={"chat_id": CHAT_ID, "text": text})
    print("DEBUG: send_message", r.status_code)

def get_updates(offset):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/getUpdates?timeout=10&offset={offset}"
        response = requests.get(url, timeout=15)
        if response.status_code == 200:
            return response.json()
        return {}
    except Exception as e:
        print(f"Erro de rede Telegram: {e}")
        return {}

def get_last_update_id():
    updates = get_updates(0)
    if updates.get("result"):
        return updates["result"][-1]["update_id"] + 1
    return 0

def get_alerts():
    triggers = get_triggers()
    if not triggers:
        return "âœ… Nenhum alerta ativo"

    msg = "ðŸš¨ ALERTAS ATIVOS\n\n"
    for t in triggers:
        msg += f"âš ï¸ {t['description']}\n"
    return msg

# ===== Loop principal =====
def main():
    offset = get_last_update_id()
    print("Bot rodando...")

    while True:
        updates = get_updates(offset)

        for update in updates.get("result", []):
            offset = update["update_id"] + 1

            if "message" in update:
                text = update["message"].get("text", "")

                if text.startswith("/status"):
                    send_message(get_status())
                elif text.startswith("/alertas"):
                    send_message(get_alerts())
                elif text.startswith("/help"):
                    send_message(get_help())
                elif text.startswith("/"):
                    send_message("⚠️ Comando não reconhecido. Use /help")

        time.sleep(2)

if __name__ == "__main__":
    main()
