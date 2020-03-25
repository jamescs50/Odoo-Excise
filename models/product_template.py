from odoo import fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    excise_active = fields.Boolean('Track Excise',default=False)
    excise_abv = fields.Float('ABV',help='Average By Volume (% Alcohol')
    excise_category = fields.Many2one('excise.category','Excise Category')
    excise_volume = fields.Float('Excisable Volume (L)', help='Volume for the basis of the Excise calculation')
    