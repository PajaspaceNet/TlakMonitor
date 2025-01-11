# TlakMonitor
 ![logo_prog2](https://github.com/user-attachments/assets/055a751a-2bd9-4bd1-8a18-235465112349)<br>



Tento program vzniknul puivodne k monitorovani 
podavani NEBILETU a jeho vliv na stav pacientky ,  velmi se mi osvedcil .  Je vyborne pro naslednou dokumentaci -- pokud bude i jinemu slouzit, 
treba jako inspirace atd ...budu rad
Slouží k zaznamenávání a správě měření krevního tlaku, pulzu a podávání léků. Dále umožňuje export naměřených dat do souboru pro další zpracování nebo analýzu. Jedná se o ukázkový projekt vhodný pro správu jednoduchých zdravotních dat.

# Funkce programu

Záznam krevního tlaku, pulzu a podaného léku: Program umožňuje snadno zadávat naměřené hodnoty.

Správa poznámek: Možnost přidat samostatné poznámky k datům.

# Export dat:

Export všech záznamů do textového souboru.

Export posledních 10 nebo libovolného počtu záznamů.

Automatické vytvoření záložního souboru při exportu.

Práce s CSV souborem: Program ukládá a načítá záznamy z CSV souboru.

# Požadavky

Pro spuštění programu je potřeba mít nainstalovaný:

Python 3.7+

Knihovny:

pandas

matplotlib (pokud budeš přidávat vizualizace v budoucnu)

# Instalace

Klonuj tento repozitář:

```git clone https://github.com/tvoje-username/monitoring-krevniho-tlaku.git```<br>
```cd monitoring-krevniho-tlaku```<br>

Nainstaluj požadované knihovny:

```pip install -r requirements.txt```<br>



# Použití

Spusť program:

```python tlak_monitor.py```

# Nabídka programu:

Zadání měření - Umožňuje zadat systolický a diastolický tlak, puls, podaný lék a případnou poznámku.

Přidání poznámky - Přidává samostatnou poznámku bez měření.

Export všech dat - Exportuje všechna zaznamenaná data do souboru export_tlak/tlak_data_export_<datum>.txt a vytvoří záložní kopii.

Export posledních 10 měření - Exportuje posledních 10 záznamů.

Export libovolného počtu měřeníUživatel zadá počet posledních měření, která budou exportována.

Ukončení programuPři ukončení program automaticky uloží všechna data do souboru tlak_data.csv.


## Struktura CSV souboru

*CSV soubor obsahuje následující sloupce:*

Datum a čas: Datum a čas měření.

Sys: Systolický krevní tlak.

Dias: Diastolický krevní tlak.

Puls: Srdeční puls.

Lék podán: Informace o podání léku (ano/ne).

Druh léku: Název podaného léku.

Poznámka: Jakýkoli dodatečný komentář.

Příklad exportovaných dat
```
Eva
Rodné číslo: XXXXXXX
Vývoj tlaku - Bilet či Nebilet to je oč tu běží ...:

Datum a čas             Sys   Dias  Puls  Lék podán  Druh léku   Poznámka
2025-01-10 12:00:00     120   80    65    ano        Nebilet     Po běhu
2025-01-11 08:30:00     130   85    70    ne         ---         ---


Datum výpisu: 2025-01-11_12-34-56
Programmed by: Pavel
```

# Struktura projektu ktera se vytvori automaticky

![tlak_monitor](https://github.com/user-attachments/assets/67e62761-975f-40f9-b2d7-e3e2cb2cf7a7)


# Možná vylepšení / ToDo

Přidání vizualizace dat pomocí knihovny matplotlib (graf vývoje krevního tlaku).

Automatické zálohování souboru tlak_data.csv na cloudové úložiště (např. Google Drive).

Lokalizace programu (např. anglická verze).

Webové nebo mobilní rozhraní.

# Licence

Tento projekt je k dispozici pod licencí MIT. Klidně si jej uprav, použij nebo sdílej
