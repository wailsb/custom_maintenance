from odoo import models, fields

class MaintenanceTeam(models.Model):
    _name = 'maintenance.team'
    _description = 'Maintenance Technical Team'

    name = fields.Char(string='Team Name', required=True)
    role = fields.Selection([
        ('electrical', 'Electrical Systems'),
        ('mechanical', 'Mechanical & Hydraulics'),
        ('electronic', 'Automation & Digital Controls')
    ], string='Team Role', required=True)
    
    # Relationships
    member_ids = fields.Many2many('res.users', string='Team Members')


class ResUsers(models.Model):
    _inherit = 'res.users' # Inherits from Odoo's core user/person model

    # Extended custom fields for your team members
    technical_certification = fields.Char(string='Specialist Certification')
    hourly_rate = fields.Float(string='Internal Hourly Cost')