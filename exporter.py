import pandas as pd
from typing import List, Dict
import json

def export_as_csv(data: List[Dict[str, str]], filename: str) -> None:
    """
    Exporte la liste de dictionnaires `data` dans un fichier CSV.
    """
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False, encoding="utf-8-sig")
    print(f"Exporté {len(data)} entrées dans {filename}")

def export_as_json(data: List[Dict[str, str]], filename: str) -> None:
    """
    Exporte la liste de dictionnaires `data` dans un fichier JSON.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"Exporté {len(data)} entrées dans {filename}")