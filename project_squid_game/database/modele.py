import sqlite3 as sql3




class MyGamePlayer(object):
    def __init__(self, name_db = "SQ_DB_V_BETA"):

        self.name_db = name_db



    def insert_database(self, name, path_img, date_creation):
        try:

            entity_db = sql3.connect("../project_game_squid_game/database/SQ_DB_V_BETA.db")
            print(f"connexion réussie avec --->{self.name_db}")
            entity_cursor = entity_db.cursor()

            query_create_table = """CREATE TABLE IF NOT EXISTS player(
                                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                                 name TEXT,
                                 path  TEXT,
                                 date  TEXT
                                 
                                 
                                 
                                  
                                 )"""
            entity_cursor.execute(query_create_table)
            entity_db.commit()

            query_insert = """
                            INSERT INTO player(name, path, date) VALUES(?, ?, ?)
            """



            value = (name, path_img, date_creation)
            entity_cursor.execute(query_insert, value)

            entity_db.commit()

        except Exception as E:
            print(f"erreur de type--->{E}")
            entity_db.rollback()

        finally:
            entity_db.close()



    def get_account_data(self):
        entity_db = sql3.connect("../project_game_squid_game/database/SQ_DB_V_BETA.db")
        entity_cursor = entity_db.cursor()
        sql = "SELECT * from player"
        entity_cursor.execute(sql)
        entity_db.commit()
        result_list_account = entity_cursor.fetchall()
        entity_db.close()
        return result_list_account


    def drop_account_data(self,drop_name, error):
        try:
            entity_db = sql3.connect("../project_game_squid_game/database/SQ_DB_V_BETA.db")
            entity_cursor = entity_db.cursor()
            sql = "DELETE FROM player WHERE name = (?)"
            l_drop_name = drop_name
            entity_cursor.execute(sql, (l_drop_name,))
            entity_db.commit()
        except Exception as E:
            print(f"Erreur de type: ->{E}")
            error = f"{E}"

        finally:
            entity_db.close()









