from django.db import connection
from collections import namedtuple

def query(query="", params=[]):
    """
    Execute a query and return the cursor.
    """
    with connection.cursor() as cursor:
        cursor.execute(query, params)
        row = dictfetchall(cursor)
    return row

def dictfetchall(cursor):
    """
    Return all rows from a cursor as a dict.
    Assume the column names are unique.
    """
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


def namedtuplefetchall(cursor):
    """
    Return all rows from a cursor as a namedtuple.
    Assume the column names are unique.
    """
    desc = cursor.description
    nt_result = namedtuple("Result", [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]