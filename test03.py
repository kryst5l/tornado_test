# coding:utf-8

import tornado.web
import tornado.ioloop
import tornado.httpserver


class IndexHandler(tornado.web.RequestHandler):
    #主路由处理类
    def get(self):
        self.write("hello multi")


if __name__=="__main__":
    app=tornado.web.Application([
        (r"/",IndexHandler),
    ])


http_server=tornado.httpserver.HTTPServer(app)
#http_server.listen(8000)
#绑定端口
http_server.bind(8000)
#开启多进程
http_server.start(3)
#有两种情况，<=0
#>0
tornado.ioloop.IOLoop.current().start()
#start开启之后才开始监听
