# -*- coding: utf-8 -*-

from odoo import models, fields, api

class eb_module(models.Model):
    _name = 'eb_module.eb_module'

    name = fields.Char('Customer Name')

    value2 = fields.Float('Reading Value')
    description = fields.Text()
