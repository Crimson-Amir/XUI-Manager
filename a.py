from sqlite_manager import ManageDb

sqlite_manager = ManageDb('v2ray')

sqlite_manager.update({'Product': {'server_domain': 'finland.ggkala.shop'}}, where='server_domain = "german.ggkala.shop" or server_domain = "america.ggkala.shop"')
