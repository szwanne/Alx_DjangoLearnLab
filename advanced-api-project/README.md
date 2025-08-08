# Book API Endpoints

## Endpoints

- GET `/api/books/` – List all books
- GET `/api/books/<int:pk>/` – Retrieve book by ID
- POST `/api/books/create/` – Create new book (auth required)
- PUT `/api/books/<int:pk>/update/` – Update book (auth required)
- DELETE `/api/books/<int:pk>/delete/` – Delete book (auth required)

## Permissions

- Read access: Available to all
- Write access: Restricted to authenticated users

## Filters

- Search by `title` or `author__name`: `/api/books/?search=Rowling`

## 🔍 API Filtering, Searching, and Ordering

### 📘 BookListView Endpoint

- `GET /api/books/` — List all books with filter, search, and ordering options.

### 🧰 Query Parameters

#### 📌 Filtering

| Parameter          | Description                       |
| ------------------ | --------------------------------- |
| `title`            | Filter books by title             |
| `publication_year` | Filter books by publication year  |
| `author`           | Filter by author ID (foreign key) |

**Example:**

#### 🔎 Searching

| Parameter | Description                         |
| --------- | ----------------------------------- |
| `search`  | Search by `title` or `author__name` |

**Example:**

#### ↕️ Ordering

| Parameter  | Description                          |
| ---------- | ------------------------------------ |
| `ordering` | Order by `title`, `publication_year` |

**Examples:**

## 🧪 API Testing

Unit tests are located in `api/test_views.py`. They cover:

- Book CRUD operations
- Permission and authentication rules
- Filtering, searching, and ordering behavior

### 🔧 Run Tests

### 🔍 Sample Assertions

- `GET /api/books/` → 200 OK
- `POST /api/books/create/` → 401 Unauthorized (unauthenticated)
- `POST /api/books/create/` → 201 Created (authenticated)
- `PUT /api/books/<id>/update/` → 200 OK
- `DELETE /api/books/<id>/delete/` → 204 No Content
