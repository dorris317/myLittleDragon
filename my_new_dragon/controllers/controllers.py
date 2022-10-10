# -*- coding: utf-8 -*-
# from odoo import http


# class MyNewDragon(http.Controller):
#     @http.route('/my_new_dragon/my_new_dragon', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_new_dragon/my_new_dragon/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_new_dragon.listing', {
#             'root': '/my_new_dragon/my_new_dragon',
#             'objects': http.request.env['my_new_dragon.my_new_dragon'].search([]),
#         })

#     @http.route('/my_new_dragon/my_new_dragon/objects/<model("my_new_dragon.my_new_dragon"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_new_dragon.object', {
#             'object': obj
#         })
