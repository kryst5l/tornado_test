# coding:utf-8

import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
import configur

tornado.options.define("port",default=8000,type=int,help="监听端口")
tornado.options.define("subjects",default=[],help="学科名")


class IndexHandler(tornado.web.RequestHandler):
    #主路由处理类
    def get(self):
        self.write("hello httpserver")


if __name__=="__main__":
    #tornado.options.parse_command_line()
    tornado.options.options.parse_config_file("./config")
    #print tornado.options.options.subjects
    app=tornado.web.Application([
        (r"/",IndexHandler),
    ])


http_server=tornado.httpserver.HTTPServer(app)
#http_server.listen(8000)
#http_server.listen(tornado.options.options.port)
http_server.listen(configur.port)
tornado.ioloop.IOLoop.current().start()
#start开启之后才开始监听
