# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Wizard(models.TransientModel):
    _name = 'aoc.wizard'
    def defaultsessions(self):
        return self.env['aoc.sesions'].browse(self._context.get('active_ids'))
    Sessio = fields.Many2one('aoc.sesions', string="Sesions", required=True ,default=defaultsessions) 
    asis = fields.Many2many('res.partner', string="Asistents")
    
    @api.depends
    def subscribe(self):
        self.sesions.assistents |= self.asis
        return {}