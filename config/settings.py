# ┌────────────────────────────────────────────────────────────┐
# │                      FXTrader Bot Config                   │
# ├────────────────────────────────────────────────────────────┤
# │ Ce fichier contient les paramètres principaux de connexion│
# │ et de configuration globale pour le bot FXTrader.          │
# │ À adapter selon votre compte et stratégie.                 │
# └────────────────────────────────────────────────────────────┘

# === Infos de connexion à MetaTrader 5 ===
MT5_ACCOUNT_ID     = 12345678                      # 🧑 Numéro de compte 
MT5_PASSWORD       = "votre_mot_de_passe"          # 🔐 Mot de passe du compte
MT5_SERVER         = "VantageInternational-Demo"  # 🌐 Nom du serveur
MT5_PATH           = r"C:\Program Files\MetaTrader 5\terminal64.exe"  # 📁 Chemin vers MT5

# === Symboles à trader ===
TRADE_SYMBOLS = ["EURUSD", "GBPUSD", "XAUUSD", "BTCUSD"]  # 🔍 Liste des marchés à surveiller

# === Paramètres de trade ===
LOT_SIZE         = 0.1                 # 📊 Taille par défaut des positions
MAX_SPREAD       = 20                  # 🚫 Spread max autorisé (en points)
SL_PIPS          = 30                  # 🛡️ Stop loss (en pips)
TP_PIPS          = 60                  # 🎯 Take profit (en pips)
ALLOWED_HOURS    = range(8, 20)        # ⏰ Heures de trading autorisées (UTC ou local selon config MT5)

# === GPT / IA (à compléter plus tard) ===
USE_GPT          = True                # 🤖 Activer GPT pour l’aide à la décision
OPENAI_API_KEY   = "sk-..."            # 🧠 Clé API OpenAI (si utilisé)

# === Journalisation ===
LOG_FILE         = "logs/trade_log.txt"  # 📄 Fichier de log principal