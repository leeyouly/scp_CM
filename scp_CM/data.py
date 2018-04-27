from spiderlib.data import DataStorage
import PyDB

class ImportCM_publicStorage(DataStorage):
    def __init__(self, db_url):
        self.db = self.build_connection(db_url)
        self.table_name = 'T_CM_PUBLIC_NEWS'
        self.db.set_metadata(self.table_name, [
            PyDB.DateField("datadate"),
            PyDB.StringField("news_title", is_key=True),
            PyDB.StringField("news_content"),
            PyDB.StringField("public_Id", is_key=True),
            PyDB.StringField("public_name"),
            PyDB.StringField("news_contenturl"),
            PyDB.StringField("news_html"),
            PyDB.StringField("news_imageurl"),
            PyDB.DateField("update_dt"),
            PyDB.StringField("news_contenturl",),
        ])

    def save_or_update(self, item):
        self.db.save_or_update(self.table_name, item)
        self.db.commit()


class ImportPuok_neaStorage(DataStorage):
    def __init__(self, db_url):
        self.db = self.build_connection(db_url)
        self.table_name = 'T_CM_WEBSITE_NEWS'
        self.db.set_metadata(self.table_name, [
            PyDB.DateField("datadate"),
            PyDB.StringField("news_type"),
            PyDB.StringField("news_title"),
            PyDB.StringField("news_content"),
            PyDB.StringField("news_contenturl"),
            PyDB.StringField("news_html"),
            PyDB.StringField("news_imageurl"),
            PyDB.DateField("update_dt"),
            PyDB.StringField("source"),
            PyDB.StringField("news_contenturl", is_key=True),
        ])

    def save_or_update(self, item):
        self.db.save_or_update(self.table_name, item)
        self.db.commit()
