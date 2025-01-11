import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

# Název souboru
soubor = "tlak_data.csv"

# Funkce pro načítání dat ze souboru s ošetřením kódování
def nacti_data(soubor):
    if os.path.exists(soubor):
        try:
            # Zkus načíst data s UTF-8
            df = pd.read_csv(soubor, encoding="utf-8")
        except UnicodeDecodeError:
            print("Chyba dekódování UTF-8. Zkouším jiné kódování...")
            try:
                # Pokud UTF-8 nefunguje, zkus Windows-1250 (středoevropské kódování)
                df = pd.read_csv(soubor, encoding="Windows-1250")
            except Exception as e:
                print(f"Chyba při načítání souboru: {e}")
                print("Vytvářím prázdný DataFrame.")
                df = pd.DataFrame(columns=["Datum a čas", "Sys", "Dias", "Puls", "Lék podán", "Druh léku", "Poznámka"])
        # Konverze datového sloupce
        if "Datum a čas" in df.columns:
            df["Datum a čas"] = pd.to_datetime(df["Datum a čas"], errors="coerce")
    else:
        print(f"Soubor '{soubor}' neexistuje. Vytvářím nový DataFrame.")
        df = pd.DataFrame(columns=["Datum a čas", "Sys", "Dias", "Puls", "Lék podán", "Druh léku", "Poznámka"])
    return df

# Načti data
df = nacti_data(soubor)

# Název adresáře pro export
EXPORT_DIR = "export_tlak"

# Kontrola existence adresáře, pokud neexistuje, vytvoříme ho
if not os.path.exists(EXPORT_DIR):
    os.makedirs(EXPORT_DIR)

# Funkce pro export všech dat
def export_all_data(df):
    if df.empty:
        print("DataFrame je prázdný, export není možný.")
        return

    datum_vypisu = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = os.path.join(EXPORT_DIR, f"tlak_data_export_{datum_vypisu}.txt")

    nadpis = (
        "Eva \n"
        "Rodné číslo: XXXXXXX\n"
        "Vývoj tlaku - Bilet či Nebilet to je oč tu běží ...:\n\n"
    )

    # Formátujeme data pro export
    export_df = df.copy()
    export_df["Datum a čas"] = export_df["Datum a čas"].dt.strftime("%Y-%m-%d %H:%M:%S")
    tabulka = export_df.to_string(index=False, formatters={
        "Datum a čas": lambda x: f"{x:<25}",
        "Sys": lambda x: f"{x:<5}" if pd.notna(x) else "---",
        "Dias": lambda x: f"{x:<5}" if pd.notna(x) else "---",
        "Puls": lambda x: f"{x:<5}" if pd.notna(x) else "---",
        "Lék podán": lambda x: f"{str(x):<10}",
        "Druh léku": lambda x: f"{x:<10}" if pd.notna(x) else "---",
        "Poznámka": lambda x: f"{x:<30}" if pd.notna(x) else "---"
    })

    zapati = f"\n\nDatum výpisu: {datum_vypisu}\nProgrammed by: Pavel"

    try:
        # Export do hlavního souboru
        with open(filename, "w", encoding="utf-8") as txt_file:
            txt_file.write(nadpis)
            txt_file.write(tabulka)
            txt_file.write(zapati)
        print(f"Data byla úspěšně exportována do souboru: {filename}")

        # Export do záložního souboru (také v adresáři export_tlak)
        backup_filename = os.path.join(EXPORT_DIR, "tlak_data.txt")
        with open(backup_filename, "w", encoding="utf-8") as backup_file:
            backup_file.write(nadpis)
            backup_file.write(tabulka)
            backup_file.write(zapati)
        print(f"Záložní export byl úspěšně proveden do souboru: {backup_filename}")

    except Exception as e:
        print(f"Chyba při exportu dat: {e}")

# Funkce pro export libovolného počtu měření
def export_data(df, count):
    if df.empty:
        print("DataFrame je prázdný, export není možný.")
        return

    export_df = df.tail(count).copy()
    export_df["Datum a čas"] = export_df["Datum a čas"].dt.strftime("%Y-%m-%d %H:%M:%S")
    datum_vypisu = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = os.path.join(EXPORT_DIR, f"tlak_export_posledni_{count}_{datum_vypisu}.txt")

    nadpis = (
        "Eva \n"
        "Rodné číslo: XXXXXXX\n"
        "Vývoj tlaku - Bilet či Nebilet to je oč tu běží ...:\n\n"
    )

    tabulka = export_df.to_string(index=False, formatters={
        "Datum a čas": lambda x: f"{x:<25}",
        "Sys": lambda x: f"{x:<5}" if pd.notna(x) else "---",
        "Dias": lambda x: f"{x:<5}" if pd.notna(x) else "---",
        "Puls": lambda x: f"{x:<5}" if pd.notna(x) else "---",
        "Lék podán": lambda x: f"{str(x):<10}",
        "Druh léku": lambda x: f"{x:<10}" if pd.notna(x) else "---",
        "Poznámka": lambda x: f"{x:<30}" if pd.notna(x) else "---"
    })

    zapati = f"\n\nDatum výpisu: {datum_vypisu}\nProgrammed by: Pavel"

    try:
        with open(filename, "w", encoding="utf-8") as txt_file:
            txt_file.write(nadpis)
            txt_file.write(tabulka)
            txt_file.write(zapati)
        print(f"Data byla úspěšně exportována do souboru: {filename}")
    except Exception as e:
        print(f"Chyba při exportu dat: {e}")

# Hlavní smyčka programu
while True:
    print("\nMožnosti:")
    print("1. Zadání měření (tlak, puls, lék, poznámka)")
    print("2. Přidání samostatné poznámky")
    print("3. Export všech dat (včetně záložního exportu)")
    print("4. Export posledních 10 měření")
    print("5. Export libovolného počtu měření")
    print("6. Ukončení programu")
    volba = input("Vyberte možnost (1-6): ").strip()

    if volba == "6":
        break

    elif volba == "1":
        datum = input("Zadejte datum a čas (formát YYYY-MM-DD HH:MM): ")
        try:
            casovy_udaj = datetime.strptime(datum, "%Y-%m-%d %H:%M")
            systolicky = int(input("Zadejte systolický tlak: "))
            diastolicky = int(input("Zadejte diastolický tlak: "))
            puls = int(input("Zadejte puls: "))
            lek = input("Byl podán lék? (ano/ne): ").strip().lower() == "ano"
            druh_leku = "Nebilet" if lek else None
            poznamka = input("Poznámka: ").strip()

            df = pd.concat([df, pd.DataFrame({
                "Datum a čas": [casovy_udaj],
                "Sys": [systolicky],
                "Dias": [diastolicky],
                "Puls": [puls],
                "Lék podán": [lek],
                "Druh léku": [druh_leku],
                "Poznámka": [poznamka if poznamka else None]
            })], ignore_index=True)
        except ValueError:
            print("Neplatný vstup. Zkuste to znovu.")

    elif volba == "2":
        datum = input("Zadejte datum a čas (formát YYYY-MM-DD HH:MM): ")
        try:
            casovy_udaj = datetime.strptime(datum, "%Y-%m-%d %H:%M")
            poznamka = input("Zadejte poznámku: ").strip()
            df = pd.concat([df, pd.DataFrame({
                "Datum a čas": [casovy_udaj],
                "Sys": [None],
                "Dias": [None],
                "Puls": [None],
                "Lék podán": [None],
                "Druh léku": [None],
                "Poznámka": [poznamka]
            })], ignore_index=True)
        except ValueError:
            print("Neplatný časový údaj. Zkuste to znovu.")

    elif volba == "3":
        export_all_data(df)

    elif volba == "4":
        export_data(df, 10)

    elif volba == "5":
        try:
            pocet = int(input("Kolik posledních měření chcete exportovat? "))
            export_data(df, pocet)
        except ValueError:
            print("Zadejte prosím platné číslo.")
    else:
        print("Neplatná volba, zkuste to znovu.")

# Uložení dat při ukončení programu
try:
    df.to_csv(soubor, index=False, encoding="utf-8")
    print("Data byla uložena do souboru.")
except Exception as e:
    print(f"Chyba při ukládání dat: {e}")
