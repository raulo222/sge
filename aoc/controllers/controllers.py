# -*- coding: utf-8 -*-
# from odoo import http


# class Aoc(http.Controller):
#     @http.route('/aoc/aoc', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/aoc/aoc/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('aoc.listing', {
#             'root': '/aoc/aoc',
#             'objects': http.request.env['aoc.aoc'].search([]),
#         })

#     @http.route('/aoc/aoc/objects/<model("aoc.aoc"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('aoc.object', {
#             'object': obj
#         })
