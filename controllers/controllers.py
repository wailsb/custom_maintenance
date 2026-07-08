# -*- coding: utf-8 -*-
# from odoo import http


# class CustomMaintenance(http.Controller):
#     @http.route('/custom_maintenance/custom_maintenance', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_maintenance/custom_maintenance/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_maintenance.listing', {
#             'root': '/custom_maintenance/custom_maintenance',
#             'objects': http.request.env['custom_maintenance.custom_maintenance'].search([]),
#         })

#     @http.route('/custom_maintenance/custom_maintenance/objects/<model("custom_maintenance.custom_maintenance"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_maintenance.object', {
#             'object': obj
#         })

