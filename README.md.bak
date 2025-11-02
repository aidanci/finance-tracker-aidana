# Mini projekt CRUD – Planety

Projekt wykonany w ramach zadania **„CRUD × 2 encje” (część A)** oraz **rozszerzenia (część B)**.  
Aplikacja webowa napisana w **Python (Flask)** z wykorzystaniem **SQLite**.  
Umożliwia pełną obsługę CRUD (Create, Read, Update, Delete) dla encji **Planeta**,  
oraz autoryzację użytkowników za pomocą tokenu **JWT**.

---

## Cel projektu
Celem projektu jest stworzenie aplikacji webowej z pełnym przepływem:
**baza danych → REST API → prosty frontend (HTML/JS)**.

Aplikacja realizuje wszystkie wymagania etapu **A**:
- relacyjna baza danych z migracją przy starcie (SQLite),
- REST API z poprawnymi kodami HTTP i walidacją danych,
- prosty interfejs HTML pozwalający na dodawanie, edytowanie i usuwanie rekordów,
- README z instrukcją uruchomienia projektu w laboratorium.

---

## Technologie
- **Backend:** Python, Flask, Flask-Cors  
- **Baza danych:** SQLite  
- **Frontend:** HTML, JavaScript (fetch API)

---

## Struktura projektu
```
planets-python/
├─ backend/
│  ├─ app.py
│  ├─ database.py
│  ├─ planets.py
│  └─ validators.py
├─ frontend/
│  └─ index.html
└─ requirements.txt
```

---

## Uruchomienie projektu lokalnie
1. Zainstaluj Python 3.10+  
2️. W folderze projektu utwórz i aktywuj wirtualne środowisko:

```bash
python -m venv .venv
# Aktywacja:
# Windows:
. .\.venv\Scripts\Activate.ps1
# macOS / Linux:
source .venv/bin/activate
```

3️. Zainstaluj wymagane biblioteki:
```bash
pip install -r requirements.txt
```

4️. Uruchom aplikację:
```bash
python -m backend.app
```

5️. Otwórz w przeglądarce:  
[https://planety-aidana.onrender.com/](https://planety-aidana.onrender.com/)

> Przy pierwszym uruchomieniu zostanie automatycznie utworzona baza danych `planets.db`.

---

## Endpointy REST API

| Metoda | Endpoint | Opis | Kod odpowiedzi |
|--------|-----------|------|----------------|
| `GET` | `/planets` | Zwraca listę wszystkich planet | 200 |
| `GET` | `/planets/<id>` | Zwraca szczegóły planety o podanym ID | 200 / 404 |
| `POST` | `/planets` | Dodaje nową planetę | 201 / 400 |
| `PUT` | `/planets/<id>` | Aktualizuje dane planety | 200 / 400 / 404 |
| `DELETE` | `/planets/<id>` | Usuwa planetę | 200 / 404 |

### 🔹 Przykładowe dane (POST/PUT)
```json
{
  "name": "Tatooine",
  "system": "Outer Rim",
  "climate": "Arid",
  "population": 200000,
  "surfaceType": "Desert"
}
```

---

## Walidacja danych
Plik `validators.py` sprawdza:
- wymagane pola (`name`, `system`, `climate`, `surfaceType`),
- poprawny typ liczbowy dla `population`,
- unikalność planety w obrębie danego systemu,
- że `population >= 0`.

---

## Frontend
Plik `frontend/index.html` umożliwia pełną obsługę CRUD:
- dodawanie nowych planet,  
- edycję istniejących,  
- usuwanie wpisów,  
- przeglądanie wszystkich danych w tabeli.

Komunikacja odbywa się przez REST API (`fetch()`).

---

## Aplikacja online
Projekt działa publicznie pod adresem:  
[https://planety-aidana.onrender.com](https://planety-aidana.onrender.com)

---

## Zrzut ekranu
![Zrzut ekranu aplikacji](screenshot.png)

---

# Część B – Autoryzacja i logowanie

W ramach rozszerzenia aplikacji (etap **B**) dodano pełny moduł **autoryzacji użytkowników** oparty o token **JWT**.  
Dzięki temu wszystkie operacje **CRUD** na encji **Planeta** wymagają wcześniejszego zalogowania.

---

## Nowe funkcje

- **Endpoint** `/auth/register` – rejestracja nowego użytkownika  
- **Endpoint** `/auth/login` – logowanie i pobranie tokenu JWT  
- **Dekorator** `@token_required` – ochrona wszystkich endpointów `/planets`  
- **Tabela** `users` w bazie SQLite  
- **Prosty frontend** z formularzem logowania + obsługą tokenu w `localStorage`  
- **Przycisk Logout** i blokada widoku danych po wylogowaniu  

---

## Endpointy autoryzacji

| Metoda | Endpoint | Opis | Kod odpowiedzi |
|:--------|:----------|:------|:---------------|
| `POST` | `/auth/register` | Rejestruje nowego użytkownika | 201 / 400 |
| `POST` | `/auth/login` | Loguje użytkownika i zwraca token JWT | 200 / 401 |

---

### Przykład: `POST /auth/register`
```json
{
  "login": "testuser",
  "password": "12345"
}

**Odpowiedź:**

```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5..."
}
```

> Token jest ważny przez **2 godziny**.  
> Wszystkie żądania do `/planets` muszą zawierać nagłówek:
> ```
> Authorization: Bearer <token>
> ```

---

## Frontend (część B)

Na stronie `index.html` znajduje się:

- formularz logowania (**Login + Password**),
- przyciski **Login / Logout**,
- formularz **dodawania/edycji planety**,
- tabela z listą planet (widoczna tylko po zalogowaniu).

Token JWT jest automatycznie zapisywany w `localStorage`  
i dołączany do każdego zapytania API.

---

## Testowe konto

| Login | Hasło | Rola |
|:-------|:------|:------|
| testuser | 12345 | USER |

---

## Wersje

| Wersja | Opis |
|:--------|:------|
| `v0.1-A` | CRUD dla encji Planeta |
| `v0.2-B-1` | Część B – rozszerzenie modułu partnera |
| `v0.2-B-2` | Autoryzacja + logowanie (JWT) + ochrona endpointów |

---

## Autor

Aidana Abylkasymova  
ID **69486**