def fetchone_as_dict(cursor):
    columns = [desc[0] for desc in cursor.description]
    row = cursor.fetchone()
    return dict(zip(columns, row) if row else None)