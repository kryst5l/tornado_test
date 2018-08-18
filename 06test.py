# coding:utf-8

import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
import configur

from tornado.web import url
from tornado.web import RequestHandler
from tornado.options import options,define

define("port",default=8008,type=int,help="监听端口")

#tornado.options.define("port",default=9997,type=int,help="监听端口")



class IndexHandler(RequestHandler):
    #主路由处理类
    def post(self):
        query_arg=self.get_argument("a",default="abc")
        query_args=self.get_arguments("a")
        body_arg=self.get_body_argument("a",strip=False)
        body_args=self.get_body_arguments("a")
        arg=self.get_argument("a")
        args=self.get_arguments("a")
        self.write("query_arg: %s <br/>" % query_arg)
        self.write("query_args: %s <br/>" % query_args)
        self.write("body_arg: %s <br/>" % body_arg)
        self.write("body_args: %s <br/>" % body_args)
        self.write("arg: %s <br/>" % arg)
        self.write("args: %s <br/>" % args)



if __name__=="__main__":
    tornado.options.parse_command_line()
    app=tornado.web.Application(
    [(r"/",IndexHandler)],
        debug=True
    )


    http_server=tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
    #start开启之后才开始监听
