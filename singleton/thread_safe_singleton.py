import threading

class ORM:
    class __DB:
        def __init__(self, conn, port=5858) -> None:
            self.__conn = conn
            self.__port = port
            self.__connect()

        def __connect(self):
            print(f"Connected to Database! URL: {self.__conn}, port: {self.__port}")

        def _create(self, query: str):
            print(f"Running the create query: {query}")

        def _read(self, query: str):
            print(f"Running the read query: {query}")

        def _update(self, query: str):
            print(f"Running the update query: {query}")

        def _delete(self, query: str):
            print(f"Running the delete query: {query}")

    _db_instance = None
    _lock = threading.Lock()

    def __init__(self, conn=None, port=5858):
        if conn is not None:
            with ORM._lock:
                if ORM._db_instance is None:
                    ORM._db_instance = self.__DB(conn, port)

    def query(self, op, cmd):
        if ORM._db_instance is None:
            raise ValueError("Database connection is not initialized. Please initialize with connection parameters.")

        with ORM._lock:
            if op.lower() == "create":
                ORM._db_instance._create(cmd)
            elif op.lower() == "read":
                ORM._db_instance._read(cmd)
            elif op.lower() == "update":
                ORM._db_instance._update(cmd)
            elif op.lower() == "delete":
                ORM._db_instance._delete(cmd)

def run_queries():
    orm = ORM(conn="localhost", port=3306)
    orm.query("create", "CREATE TABLE test (id INT PRIMARY KEY);")
    orm.query("read", "SELECT * FROM test;")
    orm.query("update", "UPDATE test SET id = 1 WHERE id = 0;")
    orm.query("delete", "DELETE FROM test WHERE id = 1;")

if __name__ == "__main__":
    # The client code.

    threads = []
    for _ in range(5):  # Create 5 threads to run the same set of queries concurrently
        thread = threading.Thread(target=run_queries)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    # After threads finish, check the instance
    if ORM._db_instance:
        print("Database instance initialized.")
    else:
        print("Database instance not initialized.")
