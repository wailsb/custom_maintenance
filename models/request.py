from odoo import models, fields, api
from odoo.exceptions import ValidationError

class MaintenanceRequest(models.Model):
    _name = 'maintenance.request'
    _description = 'Maintenance Ticket Request'

    name = fields.Char(string='Reference', required=True, copy=False, readonly=True, default='New')
    date_opened = fields.Datetime(string='Date/Time Opened', default=fields.Datetime.now, readonly=True)
    issue_description = fields.Text(string='Issue Description', required=True)
    
    state = fields.Selection([
        ('draft', 'Draft / Breakdown'),
        ('open', 'Under Repair'),
        ('success', 'Resolved successfully'),
        ('fail', 'Unresolved / Scrapped')
    ], string='Status', default='draft', tracking=True)

    # Relationships
    machine_id = fields.Many2one('maintenance.machine', string='Machine Affected', required=True)
    team_id = fields.Many2one('maintenance.team', string='Assigned Team', compute='_compute_team_id', store=True, readonly=False)
    operation_ids = fields.One2many('maintenance.operation', 'request_id', string='Executed Operations')
    active = fields.Boolean(string='Active', default=True)

    # Auto-assign the default team linked to the chosen machine
    @api.depends('machine_id')
    def _compute_team_id(self):
        for request in self:
            if request.machine_id.team_id:
                request.team_id = request.machine_id.team_id

    # Auto-generate a clean ticket sequence number when saving
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'New') == 'New':
                vals['name'] = self.env['ir.sequence'].next_by_code('maintenance.request') or 'REQ-NEW'
        return super().create(vals_list)

    def action_start_repair(self):
        self.state = 'open'

    def action_close_request_success(self):
        # Business logic validation: Ensure operations were documented before closing
        if not self.operation_ids:
            raise ValidationError("You cannot close a request without logging at least one operation details report.")
        
        # Move all underlying operations to finished states
        self.operation_ids.write({'status': 'done'})
        self.state = 'success'
        self.active = False # Automatically archives the request out of current workspaces


class MaintenanceOperation(models.Model):
    _name = 'maintenance.operation'
    _description = 'Technical Maintenance Task Record'

    description = fields.Text(string='Execution Operation Details', required=True)
    action_type = fields.Selection([
        ('repair', 'Repaired Existing Part'),
        ('replace', 'Replaced with New Component')
    ], string='Action Taken', required=True)
    
    status = fields.Selection([
        ('draft', 'Planned'),
        ('done', 'Completed')
    ], string='Status', default='draft')

    # Relationships
    request_id = fields.Many2one('maintenance.request', string='Parent Request Reference', ondelete='cascade')
    part_id = fields.Many2one('maintenance.part', string='Target Part Handled')
    worker_ids = fields.Many2many('res.users', string='Assigned Operators')