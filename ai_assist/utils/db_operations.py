from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from settings import CONNECTION_URL

Base = declarative_base()


class DatabaseOperations:
    def __init__(self, connection_url, database_name):
        self.connection_url = f"{connection_url}/{database_name}"
        self.engine = create_engine(self.connection_url)
        self.Session = sessionmaker(bind=self.engine)

        print("self.connection_url", self.connection_url)
        print("self.engine", self.engine)
        print("self.Session", self.Session)

    def connect(self):
        try:
            self.Session.configure(bind=self.engine)
            print('Connected to database!')
        except Exception as error:
            print('Error connecting to database:', error)

    def disconnect(self):
        try:
            self.Session.close_all()
            print('Disconnected from database.')
        except Exception as error:
            print('Error disconnecting from database:', error)

    def create_tables(self):
        try:
            Base.metadata.create_all(self.engine)
            print('Tables created successfully!')
        except Exception as error:
            print('Error creating tables:', error)

    def fetch_record(self, model, query):
        session = self.Session()
        try:
            # Convert the keys in the query dictionary to strings
            query = {str(key): value for key, value in query.items()}
            record = session.query(model).filter_by(**query).first()
            return record
        except Exception as error:
            print('Error fetching record:', error)
        finally:
            session.close()
    
    def fetch_all_records(self, model, query):
        session = self.Session()
        try:
            # Convert the keys in the query dictionary to strings
            query = {str(key): value for key, value in query.items()}
            records = session.query(model).filter_by(**query).all()
            return records
        except Exception as error:
            print('Error fetching record:', error)
        finally:
            session.close()

    def insert_record(self, record):
        session = self.Session()
        try:
            session.add(record)
            session.commit()
            # Refresh the record to get the latest data from the database
            session.refresh(record)
            print('Record inserted successfully!')
            return record  # Return the inserted record
        except Exception as error:
            session.rollback()
            print('Error inserting record:', error)
        finally:
            session.close()

    def update_record(self, model, query, update):
        session = self.Session()
        try:
            session.query(model).filter_by(**query).update(update)
            session.commit()
            print('Record updated successfully!')
        except Exception as error:
            session.rollback()
            print('Error updating record:', error)
        finally:
            session.close()

    def delete_record(self, record):
        session = self.Session()
        try:
            session.delete(record)
            session.commit()
            print('Record deleted successfully!')
        except Exception as error:
            session.rollback()
            print('Error deleting record:', error)
        finally:
            session.close()


db_client = DatabaseOperations(CONNECTION_URL, 'test')
db_client.connect()
