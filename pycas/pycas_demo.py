# -*- coding: utf-8 -*-
import cas
import tornado.web
class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        casClient2 = cas.CASClientV2(service_url="http://127.0.0.1:8080/login", 
                                     server_url="cas服务器认证地址")
        #获取ticket信息
        casTicket = self.get_argument("ticket", None)
        if casTicket is None:
            return self.redirect(casClient2.get_login_url())
        # 验证ticket 是否有效，并解析用户信息
        verifyInfos = casClient2.verify_ticket(casTicket)
        # verifyInfos 是一个元组，（user, dict, str）
        print (verifyInfos)
        # 取得用户之后认证就算结束了
    pass