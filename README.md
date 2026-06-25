# Student API — Flask + MySQL CRUD

REST API built with Flask, SQLAlchemy ORM, and MySQL. Manages **Students** and **Courses** with full CRUD operations.

---

## Setup

```bash
# 1. Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate

# Create and activate virtual environment for cmd
python -m venv .venv
.venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Create a .env file in the project root
cp .env.example .env   # then fill in your credentials

# 4. Create the database in MySQL
mysql -u root -p -e "CREATE DATABASE hagathon_db;"

# 5. Run the app (tables are created automatically on first start)
python run.py
```