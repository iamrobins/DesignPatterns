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

    def __init__(self, conn=None, port=5858):
        if ORM._db_instance is None and conn is not None:
            ORM._db_instance = self.__DB(conn, port)

    def query(self, op, cmd):
        if ORM._db_instance is None:
            raise ValueError("Database connection is not initialized. Please initialize with connection parameters.")
        
        if op.lower() == "create":
            ORM._db_instance._create(cmd)
        elif op.lower() == "read":
            ORM._db_instance._read(cmd)
        elif op.lower() == "update":
            ORM._db_instance._update(cmd)
        elif op.lower() == "delete":
            ORM._db_instance._delete(cmd)

if __name__ == "__main__":
    # The client code.
    
    orm1 = ORM(conn="localhost", port=3306)
    orm2 = ORM()
    
    if orm1._db_instance == orm2._db_instance:
        print("Same Instance")
    else:
        print("Different Instance")

    db = orm1.query("create", "CREATE TABLE test (id INT PRIMARY KEY);")
    orm1.query("read", "SELECT * FROM test;")
    orm1.query("update", "UPDATE test SET id = 1 WHERE id = 0;")
    orm1.query("delte", "DELETE FROM test WHERE id = 1;")
