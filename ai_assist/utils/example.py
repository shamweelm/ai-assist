import time
from db_models import Chats
from db_operations import DatabaseOperations

if __name__ == '__main__':
    connection_url = 'postgresql://shamweelmohammed:password@localhost:5432'

    # db = DatabaseOperations(engine)
    db = DatabaseOperations(connection_url, 'test')

    # Connect to the database
    db.connect()

    # # Create tables
    # db.create_tables()

    # Example: Insert a record
    new_record = Chats(id=12, name='sha', age=20)
    db.insert_record(new_record)

    # Example: Fetch a record
    query = {"name": 'sha'}
    db.connect()
    record = db.fetch_record(Chats, query)
    print(record)
    print(record.id, record.name)

    # Example: Update a record
    query = {"id": 12, "name": 'sha'}
    update = {'age': 30}
    db.update_record(Chats, query, update)

    # Example: Delete a record
    time.sleep(3)
    delete_query = {"id": 12, "name": 'sha'}
    deleted_record = db.fetch_record(Chats, delete_query)
    if deleted_record:
        db.delete_record(deleted_record)

    # Disconnect from the database
    db.disconnect()
