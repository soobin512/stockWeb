# bookmark
from django.shortcuts import render

from home.main import key_search
from menu.detail.detail_crowling import detail_crowling
from menu.detail.detailstocksvo import detailstocksvo
from model.bookmark.bookmarkdao.bookmarkdao import bookmarkDAO
from model.bookmark.bookmarksql.bookmarksql import bookmarkSql
from model.bookmark.bookmarkvo.bookmarkvo import bookmarkVO
from model.news.newsdao.newsdao import NewsDAO
from model.sqlitedao import SqliteDao

sqlitedao = SqliteDao('shop');
sqlitedao.makeTable();
bookmarkdao = bookmarkDAO('shop');

def bookmark_selectall(request):
    try:
        last = []

        email = request.session['sessionemail']
        print(email)
        data = bookmarkdao.selectall(email)
        print(data)

        li = []
        for u in data:
            a = bookmarkVO.pr(u)
            li.append(a);
        print(li[0][1])
        url = li[0][2]

        crowling = detail_crowling(url)
        data = detailstocksvo(crowling[0], crowling[1], crowling[2], crowling[3], crowling[4], crowling[5], crowling[6],
                              crowling[7], crowling[8], crowling[9], crowling[10], crowling[11], crowling[12], crowling[13],
                              crowling[14], crowling[15])
        last.append(data)
        context = {
            'center': 'sidemenu/my.html',
            'data': last
        }
        return render(request, 'index.html', context)

    except:
        context = {
            'center': 'sidemenu/my.html',
        }
        return render(request, 'index.html', context)

def bookmark_insert(request):

    try:
        url = request.POST["bookmarkurl"]
        stockname = request.POST["bookmarkstockname"]
        email = request.session['sessionemail']
        data = bookmarkVO(email, stockname, url)
        print('한번 확인 : ',data)
        # result.append(data)
        # print('중간 확인 :',result )
        bookmarkdao.insert(data);
        print('최종 확인 : ')

        # 화면 유지
        last = []
        ## 주식 정보 크롤링 ##
        print("url 확인", url)
        crowling = detail_crowling(url)
        data = detailstocksvo(crowling[0], crowling[1], crowling[2], crowling[3], crowling[4], crowling[5], crowling[6],
                              crowling[7], crowling[8], crowling[9], crowling[10], crowling[11], crowling[12], crowling[13],
                              crowling[14], crowling[15])
        last.append(data)
        ### 주식 뉴스 ###
        name = crowling[2]

        newsdao = NewsDAO('shop');
        news = newsdao.select(name);

        context = {
            'center': 'detail/detail.html',
            'items': last,
            'itemlist': news
        }

        return render(request, 'index.html', context)

    # 로그인 안했을시
    except:
        url = request.POST["bookmarkurl"]
        last = []
        ## 주식 정보 크롤링 ##
        print("url 확인", url)
        crowling = detail_crowling(url)
        data = detailstocksvo(crowling[0], crowling[1], crowling[2], crowling[3], crowling[4], crowling[5], crowling[6],
                              crowling[7], crowling[8], crowling[9], crowling[10], crowling[11], crowling[12],
                              crowling[13],
                              crowling[14], crowling[15])
        last.append(data)
        ### 주식 뉴스 ###
        name = crowling[2]

        newsdao = NewsDAO('shop');
        news = newsdao.select(name);

        context = {
            'center': 'detail/detail.html',
            'items': last,
            'itemlist': news
        }

        return render(request, 'index.html', context)

def bookmark_delete(request):

    try:
        url = request.POST["bookmarkstockurl"]
        name = request.POST["bookmarkname"]
        email = request.session['sessionemail']

        delvalue = bookmarkVO(email, name, url)
        bookmarkdao.delete(delvalue)

        # 화면 유지
        last = []
        ## 주식 정보 크롤링 ##
        print("url 확인", url)
        crowling = detail_crowling(url)
        data = detailstocksvo(crowling[0], crowling[1], crowling[2], crowling[3], crowling[4], crowling[5], crowling[6],
                              crowling[7], crowling[8], crowling[9], crowling[10], crowling[11], crowling[12],
                              crowling[13],
                              crowling[14], crowling[15])
        last.append(data)
        ### 주식 뉴스 ###
        name = crowling[2]

        newsdao = NewsDAO('shop');
        news = newsdao.select(name);

        context = {
            'center': 'detail/detail.html',
            'items': last,
            'itemlist': news
        }

        return render(request, 'index.html', context)

    # 로그인 안했을시
    except:
        url = request.POST["bookmarkurl"]
        last = []
        ## 주식 정보 크롤링 ##
        print("url 확인", url)
        crowling = detail_crowling(url)
        data = detailstocksvo(crowling[0], crowling[1], crowling[2], crowling[3], crowling[4], crowling[5], crowling[6],
                              crowling[7], crowling[8], crowling[9], crowling[10], crowling[11], crowling[12],
                              crowling[13],
                              crowling[14], crowling[15])
        last.append(data)
        ### 주식 뉴스 ###
        name = crowling[2]

        newsdao = NewsDAO('shop');
        news = newsdao.select(name);

        context = {
            'center': 'detail/detail.html',
            'items': last,
            'itemlist': news
        }

        return render(request, 'index.html', context)
