import psycopg2

from repository.database_config import postgre as cfg


def request_report(report_id):
    request = f"SELECT * FROM reports WHERE id={report_id}"
    connection = psycopg2.connect(dsn=cfg['dsn'], user=cfg['user'], password=cfg['password'])
    cursor = connection.cursor()
    cursor.execute(request)
    response = [query for query in cursor]
    cursor.close()
    connection.close()
    return response


