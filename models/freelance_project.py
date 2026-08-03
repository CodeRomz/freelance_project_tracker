from odoo import models, fields, api
from odoo.exceptions import UserError

class FreelanceProject(models.Model):
    _name = 'freelance.project'
    _description = 'Freelance Project'


    name = fields.Char(string='Project Name', required=True)
    description = fields.Text(string='Description')
    price = fields.Float(string='Price')
    state = fields.Selection([('open', 'Open'), ("progress, Inprogress"), ("completed", "Completed")], default='open')
    client_id = fields.Many2one("res.partner", string='Client ID')
    freelancer_id = fields.Many2one("res.partner", string='Freelancer')

