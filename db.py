import pymysql
from pymysql.cursors import DictCursor
import re

DB_HOST = "classmysql.engr.oregonstate.edu"
DB_USER = "cs340_nairp"
DB_PASSWORD = "7244"
DB_NAME = "cs340_nairp"


def get_connection():
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        cursorclass=DictCursor
    )


def convert_query(query: str) -> str:
    """
    Convert SQL query placeholders from colon style to PyMySQL’s pyformat style.
    E.g. ":firstNameInput" becomes "%(firstNameInput)s".
    """
    return re.sub(r":(\w+)", r"%(\1)s", query)


def initialize_db():
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Tenants (
        tenantID INT AUTO_INCREMENT PRIMARY KEY,
        firstName VARCHAR(100) NOT NULL,
        lastName VARCHAR(100) NOT NULL,
        phoneNumber VARCHAR(10) NOT NULL,
        email VARCHAR(100) NOT NULL UNIQUE
    );
    """
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(create_table_query)
        conn.commit()
    finally:
        conn.close()
