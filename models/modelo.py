from odoo import models, fields, api

class Modelo(models.Model):
    _name = 'calcular.modelo'
    numero1 = fields.Integer('Numero1', required=True)
    numero2 = fields.Integer('Numero2', required=True)
    numero3 = fields.Integer('Numero3', required=True)
    total = fields.Float(string='Total', compute='_total')

    @api.one
    @api.depends('numero1', 'numero2' , 'numero3')
    def _total(self):
        self.total = self.numero1 + self.numero2 + self.numero3

