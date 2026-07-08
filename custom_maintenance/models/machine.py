from odoo import models, fields, api

class MaintenanceMachine(models.Model):
    _name = 'maintenance.machine'
    _description = 'Industrial Machine'

    name = fields.Char(string='Machine Name', required=True)
    serial_number = fields.Char(string='Serial Number', required=True)
    description = fields.Text(string='Machine Description')
    
    job = fields.Selection([
        ('production', 'Production'),
        ('logistics', 'Logistics'),
        ('packaging', 'Packaging')
    ], string='Job Type', required=True, default='production')
    
    working_site = fields.Char(string='Working Site', required=True)
    manufacturer = fields.Char(string='Manufacturer')
    acquisition_date = fields.Date(string='Date of Acquiring', default=fields.Date.today)
    cost = fields.Float(string='Acquisition Cost')
    
    # Relationships
    team_id = fields.Many2one('maintenance.team', string='Assigned Maintenance Team')
    part_ids = fields.One2many('maintenance.part', 'machine_id', string='Machine Parts')
    active = fields.Boolean(string='Active', default=True)


class MaintenancePart(models.Model):
    _name = 'maintenance.part'
    _description = 'Machine Component Part'

    name = fields.Char(string='Part Name', required=True)
    serial_number = fields.Char(string='Serial Number', required=True)
    manufacturer = fields.Char(string='Manufacturer')
    cost = fields.Float(string='Cost')
    
    # Relationships
    machine_id = fields.Many2one('maintenance.machine', string='Belongs to Machine', ondelete='cascade')