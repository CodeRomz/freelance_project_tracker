from odoo import fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'
    _description = 'Partner Extension'

    listed_projects = fields.One2many(
        'freelance.project', 'category_id',
    )

    working_project_ids = fields.One2many(
        'freelance.project', 'freelancer_id',
    )

