# -*- coding: utf-8 -*-
from odoo import http

# class HelpdeskStock(http.Controller):
#     @http.route('/helpdesk_stock/helpdesk_stock/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/helpdesk_stock/helpdesk_stock/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('helpdesk_stock.listing', {
#             'root': '/helpdesk_stock/helpdesk_stock',
#             'objects': http.request.env['helpdesk_stock.helpdesk_stock'].search([]),
#         })

#     @http.route('/helpdesk_stock/helpdesk_stock/objects/<model("helpdesk_stock.helpdesk_stock"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('helpdesk_stock.object', {
#             'object': obj
#         })