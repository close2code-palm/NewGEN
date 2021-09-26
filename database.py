import psycopg2 as psycopg2

initial_query_users = "CREATE TABLE users(id, role) IF NOT EXISTS"
initial_query_contracts = "CREATE TABLE contracts(id, expire, bank, borrower, insurer)" \
                         "IF NOT EXISTS"

def do(statement):

        connection = psycopg2.connect(
    "dbname=tg_chain user=postgres password = <your_pass>"
)
        querer = connection.cursor()
        querer.execute(statement)
        querer.commit()

