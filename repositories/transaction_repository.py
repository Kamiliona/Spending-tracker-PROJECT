from db.run_sql import run_sql

from models.transaction import Transaction
from models.merchant import Merchant
from models.tag import Tag
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository

def save(transaction):
    sql = "INSERT INTO transactions (merchant_id, tag_id, amount ) VALUES (%s, %s, %s) RETURNING id"
    values = [transaction.merchant.id, transaction.tag.id, transaction.amount]
    results = run_sql(sql, values)
    transaction.id = results[0]['id']
    return transaction

def select_all():
    transactions = []

    sql = "SELECT * FROM transactions"
    results = run_sql(sql)
    for row in results:
        merchant = merchant_repository.select(row['merchant_id'])
        tag = tag_repository.select(row['tag_id'])
        transaction = Transaction(merchant, tag, row['amount'], row['id'])
        transactions.append(transaction)
    return transactions

def merchant(transaction):
    sql = "SELECT * FROM merchants WHERE id = %s"
    values = [transaction.merchant.id]
    results = run_sql(sql, values)[0]
    merchant = Merchant(results['name'], results['id'])
    return merchant

def tag(visit):
    sql = "SELECT * FROM tags WHERE id = %s"
    values = [transaction.tag.id]
    results = run_sql(sql, values)[0]
    tag = Tag(results['name'], results['id'])
    return tag

# NO DELETE CAUSE IT'S A SPENDING APP ??

def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM transactions WHERE id = %s"
    values = [id]
    run_sql(sql, values)



