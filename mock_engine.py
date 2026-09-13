import random
import pandas as pd

TEAMS = [
    ("Real Madrid", "Barcelona"),
    ("Man City", "Arsenal"),
    ("Galatasaray", "Fenerbahçe"),
    ("Inter", "AC Milan"),
    ("Bayern Munich", "Dortmund"),
    ("PSG", "Marseille")
]

def generate_live_matches(count=10):
    data = []
    for i in range(count):
        home, away = random.choice(TEAMS)
        open_odds = round(random.uniform(1.50, 3.20), 2)
        
        # Rastgele Senaryo Üretimi (Smart Money, Trap veya Haber)
        scenario = random.choice(["smart", "trap", "news", "normal"])
        
        if scenario == "smart":
            current_odds = round(open_odds * random.uniform(0.85, 0.91), 2)
            total_vol = random.randint(60000, 250000)
            home_vol_pct = random.uniform(0.68, 0.88)
        elif scenario == "trap":
            current_odds = round(open_odds * random.uniform(0.99, 1.05), 2)
            total_vol = random.randint(80000, 300000)
            home_vol_pct = random.uniform(0.70, 0.90)
        elif scenario == "news":
            current_odds = round(open_odds * random.uniform(0.80, 0.88), 2)
            total_vol = random.randint(10000, 35000)
            home_vol_pct = random.uniform(0.50, 0.60)
        else:
            current_odds = round(open_odds * random.uniform(0.96, 1.02), 2)
            total_vol = random.randint(5000, 40000)
            home_vol_pct = random.uniform(0.35, 0.55)
            
        data.append({
            "match_id": f"M{1000+i}",
            "home_team": home,
            "away_team": away,
            "open_odds": open_odds,
            "current_odds": current_odds,
            "total_volume": total_vol,
            "home_volume_pct": home_vol_pct,
            "match_time": f"{random.randint(12,22)}:00"
        })
    return pd.DataFrame(data)
