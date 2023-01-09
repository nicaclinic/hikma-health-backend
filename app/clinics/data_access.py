from db_util import get_connection
from language_strings.data_access import update_language_string
from language_strings.language_string import to_id
from web_errors import WebError


def add_clinic(clinic):
    update_language_string(clinic.name)
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute('INSERT INTO clinics (id, name, edited_at) VALUES (%s, %s, %s)',
                        [clinic.id, to_id(clinic.name), clinic.edited_at])


def get_most_common_clinic():
    primary = """
    select clinic_id, count(*) from visits where clinic_id is not null group by clinic_id order by count desc limit 1;
    """
    secondary = "SELECT id from clinics;"
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(primary)
            result = cur.fetchone()
            if not result:
                cur.execute(secondary)
                result = cur.fetchone()
            return result[0]

def all_clinic_data():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute('SELECT id, name, edited_at FROM clinics ORDER BY name', [])
            yield from cur


def clinic_data_by_id(clinic_id):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute('SELECT id, name, edited_at FROM users WHERE id = %s',
                        [clinic_id])
            row = cur.fetchone()
            if not row:
                raise WebError("id not found", status_code=404)
            return row