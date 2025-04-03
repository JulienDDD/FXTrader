import MetaTrader5 as mt5

mt5.initialize()

account = 10674218
password = "gCL8mIF^"
server = "VantageInternational-Demo"

authorized = mt5.login(account, password=password, server=server)
if authorized:
    print("Connexion réussie")
else:
    print("Échec de la connexion", mt5.last_error())


symbol = "EURUSD"
lot = 0.1


if not mt5.symbol_select(symbol, True):
    print(f"Erreur: symbol {symbol} non dispo")
    mt5.shutdown()


order = {
    "action": mt5.TRADE_ACTION_DEAL,
    "symbol": symbol,
    "volume": lot,
    "type": mt5.ORDER_TYPE_BUY,
    "price": mt5.symbol_info_tick(symbol).ask,
    "deviation": 20,
    "magic": 234000,
    "comment": "Bot ICT",
    "type_time": mt5.ORDER_TIME_GTC,
    "type_filling": mt5.ORDER_FILLING_IOC,
}

# Envoyer l'ordre
result = mt5.order_send(order)
print(result)