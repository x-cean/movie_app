from datamanager.sqlite_data_manager import SQLiteDataManager


db = SQLiteDataManager(SQLiteDataManager("sqlite:///data/data.sqlite"))


print(db)