from model.bookmark.bookmarkdao.bookmarkdao import bookmarkDAO
from model.bookmark.bookmarkvo.bookmarkvo import bookmarkVO
from model.sqlitedao import SqliteDao

sqlitedao = SqliteDao('shop');
sqlitedao.makeTable();
bookmarkdao = bookmarkDAO('shop');


# Delete Test
a = 'jejjej98@daum.net', '휴마시스'
try:
    bookmarkdao.delete(a);
    print('OK');
except Exception as e:
    print('에러 내용',e);

# Select All
result = bookmarkdao.selectall('jejjej98@daum.net');

li = []

for u in result:
    a = bookmarkVO.pr(u)
    li.append(a);

print(li)
#
# loginuser = userdao.select(email);
# UserVO.print(loginuser)
# userlist = []
# userlist.append(UserVO.print(loginuser));
# print(userlist[0][2])