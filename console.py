import pdb 
from models.merchant import Merchant
from models.tag import Tag
from models.transaction import Transaction

import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository
import repositories.transaction_repository as transaction_repository

transaction_repository.delete_all()
merchant_repository.delete_all()
tag_repository.delete_all()

merchant1 = Merchant("Amazon")
merchant_repository.save(merchant1)

merchant2 = Merchant("Netflix")
merchant_repository.save(merchant2)
merchant3 = Merchant("'); DELETE FROM tasks; --")

tag1 = Tag("Groceries")
tag_repository.save(tag1)

tag2 = Tag("Entertainment")
tag_repository.save(tag2)
tag3 = Tag("'); DELETE FROM tasks; --")

transaction1 = Transaction(merchant1, tag1, "50")
transaction_repository.save(transaction1)

transaction2 = Transaction(merchant1, tag2, "5.50")
transaction_repository.save(transaction2)

transaction3 = Transaction(merchant2, tag2, "9")
transaction_repository.save(transaction3)


pdb.set_trace()


