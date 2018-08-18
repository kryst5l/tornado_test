# coding:utf-8

import tornado.web
import tornado.ioloop
import tornado.httpserver


class IndexHandler(tornado.web.RequestHandler):
    #主路由处理类
    def get(self):
        self.write("hello world")


if __name__=="__main__":
    app=tornado.web.Application([
        (r"/",IndexHandler),
    ])


http_server=tornado.httpserver.HTTPServer(app)
http_server.listen(8000)

tornado.ioloop.IOLoop.current().start()
#start开启之后才开始监听
