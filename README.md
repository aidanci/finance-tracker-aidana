# 💰 Mini projekt CRUD – Expense & Income Tracker

Projekt wykonany w ramach zadania **„CRUD × 2 encje” (część A)** oraz **rozszerzenia (część B)**.  
Aplikacja webowa napisana w **Python (Flask)** z wykorzystaniem **SQLite**.  
Umożliwia pełną obsługę CRUD (Create, Read, Update, Delete) dla encji **Transakcja (Income/Expense)**  
oraz autoryzację użytkowników za pomocą tokenu **JWT**.

---

## Cel projektu
Celem projektu jest stworzenie aplikacji webowej z pełnym przepływem:
**baza danych → REST API → frontend (HTML/JS)**.

Aplikacja realizuje wszystkie wymagania etapu **A**:
- relacyjna baza danych z migracją przy starcie (SQLite),
- REST API z poprawnymi kodami HTTP i walidacją danych,
- interfejs HTML pozwalający na dodawanie, edytowanie i usuwanie transakcji,
- README z instrukcją uruchomienia projektu w laboratorium.

Etap **B** rozszerza projekt o:
- logowanie / rejestrację użytkownika,
- token JWT i ochronę endpointów,
- oddzielną stronę publiczną „Opis aplikacji”.

---

## ⚙Technologie
- **Backend:** Python, Flask, Flask-Cors  
- **Baza danych:** SQLite  
- **Frontend:** HTML, CSS, JavaScript (fetch API, localStorage)

---

## Struktura projektu
```
expense-tracker/
├─ backend/
│  ├─ app.py
│  ├─ database.py
│  ├─ auth.py
│  ├─ transactions.py
├─ frontend/
│  ├─ index.html
│  └─ about.html
└─ requirements.txt
```

---

## Uruchomienie projektu lokalnie
1. Zainstaluj **Python 3.10+**
2. Utwórz i aktywuj środowisko wirtualne:
   ```bash
   python -m venv .venv
   # Aktywacja:
   # Windows:
   . .\.venv\Scripts\Activate.ps1
   # macOS / Linux:
   source .venv/bin/activate
   ```

3. Zainstaluj zależności:
   ```bash
   pip install -r requirements.txt
   ```

4. Uruchom aplikację:
   ```bash
   python -m backend.app
   ```

5. Otwórz w przeglądarce:
   ```
   http://localhost:5000
   ```

> Przy pierwszym uruchomieniu zostanie automatycznie utworzona baza danych `finance.db`.

---

## Aplikacja online
Projekt działa publicznie pod adresem:  
👉 [https://planety-aidana.onrender.com](https://planety-aidana.onrender.com)

---

## Endpointy REST API

### Transakcje (`/transactions`)
| Metoda | Endpoint | Opis | Kod |
|--------|-----------|------|------|
| `GET` | `/transactions` | Zwraca listę transakcji użytkownika | 200 |
| `GET` | `/transactions/<id>` | Zwraca szczegóły wybranej transakcji | 200 / 404 |
| `POST` | `/transactions` | Dodaje nową transakcję | 201 / 400 |
| `PUT` | `/transactions/<id>` | Aktualizuje transakcję | 200 / 400 / 404 |
| `DELETE` | `/transactions/<id>` | Usuwa transakcję | 200 / 404 |

### Przykład `POST /transactions`
```json
{
  "title": "Salary",
  "category": "Work",
  "type": "income",
  "amount": 3500,
  "date": "2025-11-01"
}
```

---

## Endpointy autoryzacji (`/auth`)

| Metoda | Endpoint | Opis | Kod |
|:--------|:----------|:------|:----|
| `POST` | `/auth/register` | Rejestracja nowego użytkownika | 201 / 400 |
| `POST` | `/auth/login` | Logowanie i pobranie tokenu JWT | 200 / 401 |

### Przykład `POST /auth/register`
```json
{
  "login": "testuser",
  "password": "12345"
}
```

### Odpowiedź:
```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5..."
}
```

> Token jest ważny przez **2 godziny**.  
> Wszystkie zapytania do `/transactions` muszą zawierać nagłówek:
> ```
> Authorization: Bearer <token>
> ```

---

## Frontend
Plik `index.html` umożliwia:
- logowanie / wylogowanie,
- dodawanie, edytowanie i usuwanie transakcji,
- przeglądanie historii wydatków i przychodów,
- automatyczne podliczanie **sum przychodów, wydatków i bilansu**.

Dane są pobierane i wysyłane do backendu za pomocą `fetch()`.

---

## Strona publiczna
Strona `/opis` (plik `about.html`) jest dostępna bez logowania  
i opisuje funkcje aplikacji.

---

## Testowe konto

| Login | Hasło | Rola |
|:-------|:------|:------|
| testuser | 12345 | USER |

---

## Wersje

| Wersja | Opis |
|:--------|:------|
| `v1.0-A` | CRUD dla encji Transakcja |
| `v1.1-B` | Autoryzacja + logowanie (JWT) + ochrona endpointów |
| `v1.2-C` | Dodano stronę publiczną „Opis aplikacji” |

---

## Autor
**Aidana Abylkasymova**  
ID **69486**