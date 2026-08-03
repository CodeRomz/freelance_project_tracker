from odoo import models, fields, api
from odoo.exceptions import UserError

class FreelanceProject(models.Model):
    _name = 'freelance.project'
    _description = 'Freelance Project'


    name = fields.Char(string='Project Name', required=True)
    description = fields.Text(string='Description')
    price = fields.Float(string='Price')
    state = fields.Selection([('open', 'Open'), ("progress", "In-progress"), ("completed", "Completed")], default='open')
    client_id = fields.Many2one("res.partner", string='Client ID')
    freelancer_id = fields.Many2one("res.partner", string='Freelancer')
    category_id = fields.Many2one('project.category', string='Category')

    def claim_project(self):
        for record in self:
            if record.state == 'completed':
                raise UserError(_('This project is already completed.'))
            elif not record.freelancer_id:
                raise UserError(_('Please assign this project to a freelancer first'))
            else:
                record.state = 'progress'

    def complete_project(self):
        for record in self:
            if record.state == 'open' and not record.freelancer_id:
                raise UserError(_('Please assign this project to a freelancer'))
            else:
                record.state = 'completed'

