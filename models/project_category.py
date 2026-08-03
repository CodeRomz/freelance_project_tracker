from odoo import fields, models

class ProjectCategory(models.Model):
    _name = 'project.category'
    _description = 'Project Category'

    name = fields.Char(string='Name', required=True)

    _check_unique_name = model.constraint("UNIQUE(name)", "The project category is unique")