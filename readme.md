# Objednávkový systém pro bagety

Tento projekt je jednoduchý backendový systém pro správu objednávek baget. Umožňuje přijímat objednávky z frontendu,
evidovat je v databázi a spravovat přes Django administraci.

Tento projekt je čiště pro zábavu a jako testování technologií. Není určen pro reálné použití.

## Použité technologie

- Python
- Django
- Django REST Framework
- SQLite (lze změnit dle potřeby)
- django-cors-headers

## Co je vyřešeno

- Modely pro recepty, objednávky a položky objednávek
- REST API pro získání seznamu receptů a vytvoření objednávky
- Validace a ukládání objednávek včetně variant
- Základní Django administrace pro správu objednávek a jejich položek
- Povolení CORS pro komunikaci s frontendem

## Co je potřeba dále vyřešit

- Autentizace a autorizace uživatelů
- Lepší validace vstupních dat (např. kontrola dostupnosti surovin)
- Zpětná vazba o stavu objednávky (např. stav "přijato", "vyřízeno")
- Testy API a modelů
- Dokumentace API

## Spuštění projektu

1. Nainstalujte závislosti: `pip install -r requirements.txt`
2. Proveďte migrace: `python manage.py migrate`
3. Spusťte vývojový server: `python manage.py runserver`
4. Backend API je dostupné na `/api/`.

## Kontakt

Napište mi e-mail :)

www.hippou.cz