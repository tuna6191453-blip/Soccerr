# Sinyal Filtre Eşikleri
VOLUME_THRESHOLD_HIGH = 50000 # EUR cinsinden yüksek hacim sınırı
VOLUME_PERCENT_SMART = 0.65 # %65 ve üzeri tek yön hacmi
ODDS_DROP_HIGH = 0.08 # %8 ve üzeri oran düşüşü
ODDS_DROP_MEDIUM = 0.04 # %4 ve üzeri orta düşüş

# Sinyal Türleri
SIGNAL_GREEN = "GREEN_SMART_MONEY" # Akıllı Para (Yüksek Hacim + Yüksek Düşüş)
SIGNAL_YELLOW = "YELLOW_NEWS_WARN" # Haber/Sakatlık Uyarısı (Orta Hacim + Ani Düşüş)
SIGNAL_RED = "RED_TRAP_RISK" # Tuzak Risk (Sabit/Yükselen Oran + Gizli Hacim)
SIGNAL_NEUTRAL = "NEUTRAL"

# Tema
THEME_COLOR_PRIMARY = "#00FF66"
THEME_COLOR_BG = "#0E1117"
