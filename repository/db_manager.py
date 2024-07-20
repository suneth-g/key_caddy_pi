import psycopg2
import asyncio

class KeyAllocationHandler:
    def __init__(self):
        self.device_client = None
        self.conn = None
        self.cursor = None

    def __enter__(self):
        self.conn = psycopg2.connect(
            dbname="smartkeycaddydevice",
            user="admin",
            password="admin",
            host="192.168.31.48",
            port="5432"
        )
        self.cursor = self.conn.cursor()
        print("Database connection started")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
        if exc_type:
            print(f"Exception type: {exc_type}")
            print(f"Exception value: {exc_value}")
            print(f"Traceback: {traceback}")
        return False  # Propagate exceptions

    def new_key_allocation(self,value):
        try:
            query = """INSERT INTO smartkeycaddyuser.keyallocation
            (keyallocationid, deviceid, checkindate, checkoutdate, keyname, keypincode, keyfobtagid, guestwelcomemessage, keypickupinstruction, isallocationsuccessful, status, updateddatetime) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
            self.cursor.execute(query,value)
            self.conn.commit()
            return "success"
        except Exception as e:
            print(f"Error in new_key_allocation - {e}")
            return e

    def new_key_transaction(self,value):

        try:
            query = """INSERT INTO smartkeycaddyuser.keytransaction
            (keyallocationid, keytransactiontype, keymessagejson, iskeymessagesent,updateddatetime, exception) 
            VALUES (%s, %s, %s, %s, %s, %s);"""
            self.cursor.execute(query, value)
            self.conn.commit()
            return "success"
        except Exception as e:
            print(f"Error in new_key_transaction - {e}")
            return e

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        print("Database connection closed")

    def __del__(self):
        self.close()