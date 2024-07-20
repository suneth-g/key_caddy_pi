import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QStackedWidget, QInputDialog, QMessageBox,QLineEdit
from PyQt5.QtCore import Qt
from asyncqt import QEventLoop
import asyncio
from azure.iot.device.aio import IoTHubDeviceClient
from azure.iot.device import MethodResponse
import psycopg2
import datetime
import json
#import qasync
#from evdev import InputDevice, categorize, ecodes, events
from typing import List

from screens.screen_admin import Ui_screen_admin
from screens.screen_drop import Ui_screen_drop
from screens.screen_help import Ui_screen_help
from screens.screen_keyload import Ui_screen_keyload
from screens.screen_main import Ui_screen_main
from screens.screen_password import Ui_screen_password
from screens.screen_pick import Ui_screen_pick
from screens.screen_pin import Ui_screen_pin
from screens.screen_qr import Ui_screen_qr

from  repository.db_manager import KeyAllocationHandler

class IoTHandler:
    def __init__(self):
        self.cursor = 'test1'
        self.conn = 'test2'

    async def connect(self):
        # Replace with your device connection string
        conn_str = "HostName=azu-aue-smartkeyhub-iothub.azure-devices.net;DeviceId=smartkeybox_arena_bris;SharedAccessKey=pqH7ziHqCfFIoXPw7QaOZ+jgw/9wiaNmWAIoTEUWZeE="

        # Create instance of the device client using the connection string
        self.device_client = IoTHubDeviceClient.create_from_connection_string(conn_str)
#        print(dir(self.device_client.create_from_connection_string.connection_retry()))

        # Disable internal retries
 #       self.device_client.retry_policy = RetryPolicy.NO_RETRY

        # Connect the device client.
        await self.device_client.connect()
        
        self.device_client.on_method_request_received = self.method_handler
#        await self.check_keytransaction()

    async def check_keytransaction(self):
        while True:
            print("loop")
            query = """select count(*) from smartkeycaddyuser.keytransaction where iskeymessagesent = false limit 1;"""
            self.cursor.execute(query)
            out = self.cursor.fetchall()
            n = out[0][0]
            if out != 0:
                for i in range(n):
                    print(f"for - {n}")
                    try:
                        query = """select keytransactionid,keymessagejson from smartkeycaddyuser.keytransaction where iskeymessagesent = false limit 1;"""
                        self.cursor.execute(query)
                        out = self.cursor.fetchall()
                        telemetry = json.dumps(out[0][1])
                        print(telemetry)
                        await self.device_client.send_message(telemetry)
                        query = """update smartkeycaddyuser.keytransaction set iskeymessagesent = true where keytransactionid = %s returning keytransactionid """
                        value = out[0][0],
                        self.cursor.execute(query,value)
                        out = self.cursor.fetchall()
                        print()
                        self.conn.commit()
                    except Exception as e:
                        print(f"Error in check keytransaction: {e}")
            await asyncio.sleep(5)

    async def method_handler(self, method_request):
        print()
        print(f"Received direct method call: {method_request.name}")
     
        if (method_request.name == "key_allocation_request_handler"):
            await self.key_allocation_request_handler(method_request)
        elif (method_request.name == "your_other_method_handlers"):
            await self.key_allocation_request_handler(method_request)
    
    async def key_allocation_request_handler(self, method_request):
        try:
            json_data = method_request.payload
            with KeyAllocationHandler() as obj:
                for allocation in json_data['keyAllocation']:
                    values = (
                        allocation['keyAllocationId'],
                        json_data['deviceId'],
                        allocation['checkInDate'],
                        allocation['checkOutDate'],
                        allocation['keyName'],
                        allocation['keyPinCode'],
                        allocation['keyFobTagId'],
                        allocation['guestWelcomeMessage'],
                        allocation['keyPickupInstruction'],
                        True,
                        'KeyAllocated',
                        datetime.datetime.now()
                        )
                    kaout = obj.new_key_allocation(values)
                    if kaout == "success":
                        allocation['isallocationsuccessful'] = True
                        allocation['status'] = 'KeyAllocated'
                        keymessagejson = json.dumps(allocation)
                        values = (
                            allocation['keyAllocationId'],
                            'KeyCreated',
                            keymessagejson,
                            True,
                            datetime.datetime.now(),
                            ""
                            )
                        ktout = obj.new_key_transaction(values)
                    else:
                        allocation['isallocationsuccessful'] = False
                        allocation['status'] = str(kaout)
                        if obj.conn:  # Check if connection exists before rolling back
                            obj.conn.rollback()  # Rollback the transaction

            method_response = MethodResponse.create_from_method_request(method_request, 200, json_data)
        except Exception as e:
            print(f"Error in key_allocation_request_handler: {e}")
            method_response = MethodResponse.create_from_method_request(method_request, 500, {"error": str(e)})
        await self.device_client.send_method_response(method_response)

    def __del__(self):
        print("close")
        self.cursor.close()
        self.conn.close()

#Index(0)
class screen_main(QMainWindow, Ui_screen_main):
    def __init__(self, parent=None):
        super(screen_main, self).__init__(parent)
        self.setupUi(self)
        self.btn_keypickup.clicked.connect(self.open_screen_pick)
        self.btn_keydropoff.clicked.connect(self.open_screen_drop)
        self.btn_admin.clicked.connect(self.open_screen_password)
        self.btn_help.clicked.connect(self.open_screen_help)

    def open_screen_pick(self):
        self.parent().setCurrentIndex(1)

    def open_screen_drop(self):
        self.parent().setCurrentIndex(2)

    def open_screen_password(self):
        self.parent().setCurrentIndex(3)

    def open_screen_help(self):
        self.parent().setCurrentIndex(4)

#Index(1)
class screen_pick(QMainWindow, Ui_screen_pick):
    def __init__(self, parent=None):
        super(screen_pick, self).__init__(parent)
        self.setupUi(self)

#Index(2)
class screen_drop(QMainWindow, Ui_screen_drop):
    def __init__(self, parent=None):
        super(screen_drop, self).__init__(parent)
        self.setupUi(self)

#Index(3)
class screen_password(QMainWindow, Ui_screen_password):
    def __init__(self, parent=None,iot_handler=None):
        super(screen_password, self).__init__(parent)
        self.iot_handler = iot_handler
        self.setupUi(self,self.iot_handler)

#Index(4)
class screen_help(QMainWindow, Ui_screen_help):
    def __init__(self, parent=None):
        super(screen_help, self).__init__(parent)
        self.setupUi(self)

#Index(5)
class screen_pin(QMainWindow, Ui_screen_pin):
    def __init__(self, parent=None,iot_handler=None):
        super(screen_pin, self).__init__(parent)
        self.iot_handler = iot_handler
        self.setupUi(self,self.iot_handler)

#Index(6)
class screen_qr(QMainWindow, Ui_screen_qr):
    def __init__(self, parent=None):
        super(screen_qr, self).__init__(parent)
        self.setupUi(self)

#Index(7)
class screen_admin(QMainWindow, Ui_screen_admin):
    def __init__(self, parent=None,iot_handler=None):
        super(screen_admin, self).__init__(parent)
        self.iot_handler = iot_handler
        self.setupUi(self,self.iot_handler)

#Index(8)
class screen_keyload(QMainWindow, Ui_screen_keyload):
    def __init__(self, parent=None,iot_handler=None):
        super(screen_keyload, self).__init__(parent)
        self.iot_handler = iot_handler
        self.setupUi(self,self.iot_handler)

class MainWindow(QStackedWidget):
    def __init__(self, parent=None):
        self.iot_handler = IoTHandler()
        asyncio.create_task(self.iot_handler.connect())
        super(MainWindow, self).__init__(parent)
        self.screen_main = screen_main(self)
        self.screen_pick = screen_pick(self)
        self.screen_drop = screen_drop(self)
        self.screen_password = screen_password(self,self.iot_handler)
        self.screen_help = screen_help(self)
        self.screen_pin = screen_pin(self,self.iot_handler)
        self.screen_qr = screen_qr(self)
        self.screen_admin = screen_admin(self,self.iot_handler)
        self.screen_keyload = screen_keyload(self,self.iot_handler)

        self.addWidget(self.screen_main)
        self.addWidget(self.screen_pick)
        self.addWidget(self.screen_drop)
        self.addWidget(self.screen_password)
        self.addWidget(self.screen_help)
        self.addWidget(self.screen_pin)
        self.addWidget(self.screen_qr)
        self.addWidget(self.screen_admin)
        self.addWidget(self.screen_keyload)

        self.reading_task = None
        self.device_path = '/dev/input/event0'

        self.currentChanged.connect(self.on_screen_changed)  
        
        self.setCurrentIndex(0)
        self.setCursor(Qt.BlankCursor)  # Hide the mouse cursor

    def on_screen_changed(self, index):
        if index == 6:
            if self.reading_task is None:
                self.reading_task = asyncio.ensure_future(read_qr_code(self,index))
        elif index == 8:
            if self.reading_task is None:
                self.reading_task = asyncio.ensure_future(read_qr_code(self,index))
        else:
            if self.reading_task is not None:
                self.reading_task.cancel()
                self.reading_task = None

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
        if event.key() == Qt.Key_Backspace:
            self.setCurrentIndex(0)

async def read_qr_code(self,index):
    reader = InputDevice(self.device_path)
    tag_data = []
    try:
        while True:
            async for event in reader.async_read_loop():
                if event.type == ecodes.EV_KEY:
                    key_event = categorize(event)
                    if key_event.keystate == key_event.key_down:
                        key_code = key_event.keycode
                        if key_code.startswith("KEY_"):
                            key_name = key_code.split("_", 1)[1]
                            if len(key_name) == 1:  # Check if it's a printable character
                                tag_data.append(key_name)
                            elif key_name == "ENTER":
                                tag = ''.join(tag_data)
                                process_tag(self,tag, index)
                                tag_data = []  # Clear tag data for next tag
            await asyncio.sleep(0.01)
    except asyncio.CancelledError:
        pass  # Handle task cancellation properly
    except Exception as e:
        print(f"Error in read_qr_code: {e}")
    finally:
        reader.close()

def process_tag(self,tag,index):
    print(f"tag - {tag} {index}")
    if index  == 8:
        try:
            select_query =  """
                                UPDATE smartkeycaddyuser.keyallocation
                                SET binid = (
                                    SELECT binid
                                    FROM smartkeycaddyuser.bin
                                    WHERE inuse = false
                                    LIMIT 1
                                )
                                WHERE keyallocationid = (
                                    SELECT keyallocationid
                                    FROM smartkeycaddyuser.keyallocation
                                    WHERE status = 'KeyCreated'
                                    AND keyfobtagid = (
                                        SELECT keyfobtagid
                                        FROM smartkeycaddyuser.keyfobtag
                                        WHERE keyfobtag = %s
                                    )
                                )RETURNING keyallocationid,binid;
                            """
            value = (tag,)
            self.iot_handler.cursor.execute(select_query, value)
            out = self.iot_handler.cursor.fetchall()
            if out != []:
                UPDATE_query = """UPDATE smartkeycaddyuser.bin SET inuse = true WHERE binid = %s;"""
                value = out[0][1],
                self.iot_handler.cursor.execute(UPDATE_query, value)
                UPDATE_query = """UPDATE smartkeycaddyuser.keyallocation SET status = 'KeyLoaded' WHERE keyallocationid = %s;"""
                value = out[0][0],
                self.iot_handler.cursor.execute(UPDATE_query, value)
                insert_query = """INSERT INTO smartkeycaddyuser.keytransaction(keyallocationid, keytransactiontype, keymessagejson, iskeymessagesent,updateddatetime, exception) VALUES (%s, %s, %s, %s, %s, %s);"""
                value = (out[0][0],'KeyLoaded','{"":""}',False,datetime.datetime.now(),'')
                print(insert_query)
                print(value)
                print()
                self.iot_handler.cursor.execute(insert_query, value)
                self.iot_handler.conn.commit()
            else:
                print("no key to load")
        except Exception as e:
            print(f"Key load error - {e}")
            db_output = (f"DB operation failed: {e}")
    elif index == 6:
        try:
            query = """update smartkeycaddyuser.keyallocation set status = 'KeyPickedUp' where keypincode = %s and status = 'KeyLoaded' returning keyallocationid,binid;"""
            value = tag,
            self.iot_handler.cursor.execute(query, value)
            out = self.iot_handler.cursor.fetchall()
            self.iot_handler.conn.commit()
            print(f"out - {out}")
            if out != []:
                UPDATE_query = """UPDATE smartkeycaddyuser.bin SET inuse = false WHERE binid = %s;"""
                value = out[0][1],
                self.iot_handler.cursor.execute(UPDATE_query, value)
                insert_query = """INSERT INTO smartkeycaddyuser.keytransaction(keyallocationid, keytransactiontype, keymessagejson, iskeymessagesent,updateddatetime, exception) VALUES (%s, %s, %s, %s, %s, %s);"""
                value = (out[0][0],'KeyPickedUp','{"":""}',False,datetime.datetime.now(),'')
                self.iot_handler.cursor.execute(insert_query, value)
                self.iot_handler.conn.commit()
            else:
                print("no key to pickup")
        except Exception as e:
            print(f"key pickup error - {e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    main_window = MainWindow()
#    main_window.showFullScreen()  # Ensures full screen display on the 7-inch display
    main_window.setFixedSize(720,1000)
    main_window.show()  # Ensures full screen display on the 7-inch display

    with loop:
        sys.exit(loop.run_forever())