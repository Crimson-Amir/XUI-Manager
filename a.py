from sqlite_manager import ManageDb

sqlite_manager = ManageDb('v2ray')

sqlite_manager.custom('ALTER TABLE Product ADD COLUMN inbound_header_type TEXT DEFAULT "http"')
