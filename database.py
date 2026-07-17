import sqlite3
import os

DB_FOLDER = "database"
DB_NAME = "diagnosis.db"

os.makedirs(DB_FOLDER, exist_ok=True)

DB_PATH = os.path.join(DB_FOLDER, DB_NAME)


def get_connection():
    return sqlite3.connect(DB_PATH)


def create_table():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS diagnosis_records(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            patient_name TEXT,

            age INTEGER,

            gender TEXT,

            disease TEXT,

            confidence REAL,

            severity TEXT,

            prediction_date TEXT,

            prediction_time TEXT,

            audio_file TEXT,

            pdf_report TEXT
        )
    """)

    conn.commit()
    conn.close()


def insert_record(
        patient_name,
        age,
        gender,
        disease,
        confidence,
        severity,
        prediction_date,
        prediction_time,
        audio_file,
        pdf_report
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

        INSERT INTO diagnosis_records(

        patient_name,
        age,
        gender,
        disease,
        confidence,
        severity,
        prediction_date,
        prediction_time,
        audio_file,
        pdf_report

        )

        VALUES(?,?,?,?,?,?,?,?,?,?)

    """,

    (

        patient_name,
        age,
        gender,
        disease,
        confidence,
        severity,
        prediction_date,
        prediction_time,
        audio_file,
        pdf_report

    )

    )

    conn.commit()

    conn.close()


def get_all_records():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

        SELECT *

        FROM diagnosis_records

        ORDER BY id DESC

    """)

    data = cursor.fetchall()

    conn.close()

    return data


def delete_record(record_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(

        "DELETE FROM diagnosis_records WHERE id=?",

        (record_id,)

    )

    conn.commit()

    conn.close()