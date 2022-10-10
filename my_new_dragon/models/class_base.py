from odoo import models, fields, api


class ClassBase(models.Model):
    _name = 'class.base'
    _description = 'Description module'

    name = fields.Char(string='Name')
    studentNumber = fields.Integer(string='Student Number')
    stage = fields.Char(string='Stage')