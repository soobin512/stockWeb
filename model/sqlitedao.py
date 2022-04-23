import sqlite3

from model.bookmark.bookmarksql.bookmarksql import bookmarkSql
from model.news.newssql.newssql import NewsSql
from model.user.usersql.usersql import Sql

class SqliteDao:
    def __init__(self, dbName):
        self.__dbName = dbName;
    def getConn(self):
        con = sqlite3.connect(self.__dbName);
        cursor = con.cursor();
        return {'con':con,'cursor':cursor};
    def close(self, cc):
        if cc['cursor'] != None:
            cc['cursor'].close();
        if cc['con'] != None:
            cc['con'].close();
    def makeTable(self):
        cc = self.getConn();
        cc['cursor'].execute(Sql.make_userdb);
        cc['cursor'].execute(NewsSql.make_newsdb);
        cc['cursor'].execute(bookmarkSql.make_bookmarkdb);
        cc['con'].commit();
        self.close(cc);