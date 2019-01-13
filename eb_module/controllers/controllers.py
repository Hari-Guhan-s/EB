# -*- coding: utf-8 -*-
from odoo import http
from odoo.addons.web.models.ir_http import Http
import base64
from odoo import SUPERUSER_ID
import odoo.modules.registry
import sys
import json
from odoo.http import request
import logging

class new_EB_report(http.Controller):
   
   
   @http.route(['/user_EB_data'],auth="none",csrf=False,type="json") 
   def submit_detail(self):
       
       request_data = request.jsonrequest
       logging.info(request_data)
       try:
            request_data = request.jsonrequest
#             input_data=json.loads(request_data)
            record = request.env['eb_module.eb_module'].sudo().create({'name':request_data['name'],'value2':request_data['value']})
#             
#             logging.info(input_data)
           
#                
       except Exception as e:
            logging.info(e)
#             
       return True

#    def get_registry(self,request):
#         try:
#     #         path=os.path.dirname(os.path.abspath(__file__))
#     #         for file in os.listdir(path):
#     #             if file.endswith(".txt"):
#     #                 db_file=os.path.join(path,file)       
#     #         text_file=open(db_file)
#     #         dbname_text = text_file.readlines()
#     #         dbname = dbname_text[0]
#     #         try:
#     #             registry = openerp.modules.registry.Registry(dbname)
#     #         except:
#     #             pass
#             if request:
#                 environ = request.httprequest.environ
#                 fp=environ['wsgi.input']
#                 fs = cgi.FieldStorage(fp=fp,environ=environ)
#                 body=fs.value
#                 data = json.loads(body)
#             else:
#                 data=None
#     #         pool = pooler.get_pool(dbname)
#         except Exception as e:
#             logging.info('exception as e inside get regsitry')
#             logging.info(e)
#         return data


