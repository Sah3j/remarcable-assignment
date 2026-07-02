# Product Catalog — Django Take-Home Assignment

A Django application that models products, categories, and tags for a
construction-materials catalog, with a search-and-filter interface.

Users can search products by name/description, filter by category, filter by
one or more tags, and combine all three at once.

## Tech Stack

- Python 3.13
- Django (see `requirements.txt` for the exact version)
- SQLite (default Django database — no external database setup required)
- Django templates (no separate front-end framework)

## Features

- **Models** with correct relationships:
  - `Product` → `Category` via a many-to-one `ForeignKey`
  - `Product` ↔ `Tag` via a many-to-many `ManyToManyField`
- **Search** across product name and description (case-insensitive).
- **Filter** by category (single) and by tags (multiple).
- **Combined** search + filters, applied together.
- **Customized Django admin** for populating and managing data.
- **Seed command** to reproduce the sample dataset from an empty database.

## Setup & Running

These instructions assume Python 3.13 is installed.

1. **Clone the repository**
```bash
   git clone https://github.com/Sah3j/remarcable-assignment
   cd remarcable-assignment
```

2. **Create and activate a virtual environment**
```bash
   python3 -m venv venv
   source venv/bin/activate        # macOS / Linux
   # venv\Scripts\activate         # Windows
```

3. **Install dependencies**
```bash
   pip install -r requirements.txt
```

4. **Apply database migrations**
```bash
   python manage.py migrate
```

5. **Seed the database with sample data**
```bash
   python manage.py seed_products
```
   This creates 5 categories, 10 tags, and 22 products.

6. **(Optional) Create an admin superuser** — needed only to access the
   Django admin interface at `/admin/`:
```bash
   python manage.py createsuperuser
```

7. **Run the development server**
```bash
   python manage.py runserver
```
   Then open **http://127.0.0.1:8000/** for the product catalog,
   or **http://127.0.0.1:8000/admin/** for the admin interface.

## Sample Data

The dataset was originally populated through the Django admin interface
during development, as required. The `seed_products` management command is
provided so the same dataset can be reproduced from an empty database without
manual entry.

## How Search & Filtering Works

The product list view (`products/views.py`) starts from all products and
progressively narrows the queryset based on the query-string parameters:

- **Search (`q`)** uses a `Q`-object OR query to match either the name or the
  description, case-insensitively (`icontains`).
- **Category** filters by the selected category's ID.
- **Tags** filters by the selected tag IDs (`tags__in`), with `.distinct()`
  applied so a product matching multiple selected tags is not duplicated.

Because Django querysets are lazy, the filters are chained without hitting the
database until the template iterates over the results.

The HTML form uses `method="get"`, so all selections appear in the URL query
string. This makes searches bookmarkable and keeps the form state populated
after each submission.

## Assumptions & Notes

- **Search scope:** The assignment specifies searching products "by
  description." I extended search to also cover the product **name**, since
  users naturally search by product name. This is implemented with a `Q`-object
  OR query across both fields.
- **Category deletion:** `Product.category` uses `on_delete=models.PROTECT`,
  so a category that still has products cannot be deleted without first
  reassigning or removing those products. This prevents accidental data loss
  in a catalog context (as opposed to `CASCADE`, which would delete all
  products in a deleted category).
- **Database:** SQLite is used for zero-config setup. The `db.sqlite3` file is
  intentionally excluded from version control; the seed command reproduces the
  data instead.
- **Front-end:** Plain Django templates are used, per the assignment's note
  that styling is not important and the focus is functionality and queries.

## AI Usage Attribution

Per the assignment's AI policy: AI assistance (Claude) was used as a learning
and reference aid while building this project — for explanations of Django
concepts (model relationships, querysets, the admin interface, URL routing,
templates), for reviewing and debugging my code, and for drafting the sample
product dataset used by the seed script.

All code was written, understood, and tested by me. I can explain every part
of the implementation.

## Project Structure

```
config/               # Project settings and root URL configuration
products/
    models.py         # Category, Tag, Product models
    admin.py          # Admin registration and customization
    views.py          # Search-and-filter view
    urls.py           # App URL routing
    templates/
        products/
            list.html # Search/filter page
    management/
        commands/
            seed_products.py   # Sample-data seeding command
requirements.txt
README.md
```