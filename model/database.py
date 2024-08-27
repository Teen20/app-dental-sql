import pyodbc
def get_connection():
    connection = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=AF-MSS995;'
        'DATABASE=MAX&DENT;'
        'Trusted_Connection=yes;'
    )
    return connection

