import pandas as pd
from config import *

def analyze_matches(df: pd.DataFrame) -> pd.DataFrame:
    # 1. Oran Düşüş Yüzdesi (O_drop)
    df["odds_drop_pct"] = (df["open_odds"] - df["current_odds"]) / df["open_odds"]
    
    # 2. Sinyal Skoru Hesaplama: S = O_drop * P_vol
    df["signal_score"] = df["odds_drop_pct"] * df["home_volume_pct"] * 100
    
    # 3. Akıllı Sinyal Etiketleme
    def classify_signal(row):
        is_high_vol = row["total_volume"] >= VOLUME_THRESHOLD_HIGH
        is_smart_vol = row["home_volume_pct"] >= VOLUME_PERCENT_SMART
        is_high_drop = row["odds_drop_pct"] >= ODDS_DROP_HIGH
        
        if is_high_vol and is_smart_vol and is_high_drop:
            return SIGNAL_GREEN
        elif is_high_vol and is_smart_vol and not is_high_drop:
            return SIGNAL_RED
        elif is_high_drop and not is_high_vol:
            return SIGNAL_YELLOW
        else:
            return SIGNAL_NEUTRAL
            
    df["signal_type"] = df.apply(classify_signal, axis=1)
    return df
