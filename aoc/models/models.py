 #-*- coding: utf-8 -*-

import string
from urllib import request
from datetime import timedelta
from odoo import models, fields, api, exceptions
from datetime import datetime



class aoc_cursos(models.Model):
    _name = 'aoc.cursos'
    nom= fields.Char(string="Nom",required=True,help="Donam el nom del grup")
    descripcio= fields.Text(string="descripcio")
    sesions= fields.One2many("aoc.sesions","cursos",string="sesio",required="True", ondelete="cascade")
class aoc_sesions(models.Model):
    _name = 'aoc.sesions'
    nom= fields.Char(string="Nom",required=True,help="Donam el nom de la sessió")
    fecha= fields.Date(string="Fecha",default=datetime.today())
    fechaf= fields.Date(string="Fecha final" ,compute='traurefinal', inverse='setduracio')
    duracio= fields.Float(string="Duració")
    asistents= fields.Integer(string="seients")
    cursos=fields.Many2one('aoc.cursos',string='curs',required=True)
    instructor= fields.Many2one('res.partner', string='instructor', domain=[('instructor','=',True)])
    cursos = fields.Many2one('aoc.cursos',string='Curs')
    assistents=fields.Many2many('res.partner',string='Asistents')
    activitat=fields.Boolean(string="Activitat",default="True")
    percen=fields.Float(string='Percentage',compute='percentage', store=True)
    hores=fields.Float(string='Hores',compute='horespas',store=True)
    @api.depends('duracio')
    def horespas(self):
        for x in self:
            if not x.duracio:
                x.percen=0
            else:
                x.hores= x.duracio*24
    @api.depends('asistents','assistents')
    def percentage(self):
        for x in self:
            if not x.asistents:
                x.percen=0
            else:
                x.percen=100*len(x.assistents) / x.asistents
    @api.onchange('asistents', 'assistents','duracio')
    def _verify_valid_seats(self):
        if self.asistents < 0:
            return {
                'warning': {
                    'title': "Incorrecte",
                    'message': "El nombre de seients no pot ser negatiu",
                },
            }
        if self.asistents < len(self.assistents):
            return {
                'warning': {
                    'title': "Incorrecte",
                    'message': "No poden haber mes asistets que seients",
                },
            }
        if self.duracio < 0:
            return {
                'warning': {
                    'title': "Incorrecte",
                    'message': "El temps de duracio no pot ser negatiu",
                },
            }
    @api.constrains('instructor', 'assistents')
    def comprovar(self):
        for r in self:
            if r.instructor and r.instructor in r.assistents:
                raise exceptions.ValidationError("Un instructor no pot estar en la seua propia sessió ")
    @api.depends('fecha', 'duracio')
    def traurefinal(self):
        for r in self:
            if not (r.fecha and r.duracio):
                r.fechaf = r.fecha
                continue

            
            diaini = fields.Datetime.from_string(r.fecha)
            duracio = timedelta(days=r.duracio, seconds=-1)
            r.fechaf = duracio + diaini

    def setduracio(self):
        for r in self:
            if not (r.fecha and r.fechaf):
                continue

            
            fecha = fields.Datetime.from_string(r.fecha)
            fechafin = fields.Datetime.from_string(r.fechaf)
            r.duracio = (fechafin - fecha).days + 1
class aoc_instructor(models.Model):
    _inherit='res.partner'
    sesion_ids= fields.Many2many('aoc.sesions',string="Sesions",readonly=True)
    instructor = fields.Boolean(string="Instructor",default="False")


#  name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100




