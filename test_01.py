# coding:utf-8
import tornado.web
import tornado.ioloop


class IndexHandler(tornado.web.RequestHandler):
    #主路由处理类
    def get(self):
        """对应的http的get请求方式"""
        self.write("hello cast")


if __name__=="__main__":
    app=tornado.web.Application([(r"/",IndexHandler),

                                 ])

    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()