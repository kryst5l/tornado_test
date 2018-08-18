# coding:utf-8

import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
import configur

from tornado.web import url

tornado.options.define("port",default=9997,type=int,help="监听端口")



class IndexHandler(tornado.web.RequestHandler):
    #主路由处理类
    def get(self):

        self.write('<a href="%s">php</a>'%self.reverse_url("php_url"))
        #self.write('<a href="/php">php</a>')


class SubjectHandler(tornado.web.RequestHandler):
    def initialize(self,name):
        print("call initialize")
        self.subject=name


    def get(self):
        print("call get")
        self.write("Subject name: %s" % self.subject)


# class PhpHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.write('<a href="%s">php</a>'%self.reverse_url("php_url"))


if __name__=="__main__":
    tornado.options.parse_command_line()
    app=tornado.web.Application(
    [

        (r"/",IndexHandler),
        (r"/subject",SubjectHandler,{"name":"python"}),
        (r"/c", SubjectHandler, {"name": "c"}),
        url(r"/php", SubjectHandler, {"name": "PHP"},name="php_url"),
    ],
        debug=True
           )


http_server=tornado.httpserver.HTTPServer(app)
http_server.listen(tornado.options.options.port)
tornado.ioloop.IOLoop.current().start()
#start开启之后才开始监听
