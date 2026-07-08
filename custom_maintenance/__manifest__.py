# -*- coding: utf-8 -*-
{
    'name': 'Custom Maintenance SI',
    'version': '18.0.1.0.0',
    'category': 'Maintenance',
    'summary': 'Internal Enterprise Information System for Machine Maintenance Pipelines',
    'description': """
Industrial Maintenance Information System (SI)
==============================================
A robust, relational backend module designed to manage industrial equipment pipelines, asset hierarchies, and technical team operations within Odoo 18.

Core Architecture:
------------------
* **Asset Mapping:** Establishes a strict parent-child relationship between industrial machines and their underlying component parts (Many2one/One2many).
* **Automated Ticketing:** Implements an auto-sequenced (REQ-0000) ticketing system for logging hardware breakdowns and repair lifecycles.
* **Operation Tracking:** Granular logging of technical interventions, linking specific technicians and replacement parts to isolated maintenance events.
* **Role-Based Access Control (RBAC):** Inherits and extends Odoo's core user framework to securely manage technical team assignments and access rights.

Engineered to abstract complex database relationships into a streamlined, responsive user interface for floor technicians and logistics managers.
    """,
    'author': "Wail Sari Bey",
    'website': "https://wailsb.com",
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/maintenance_sequence.xml',
        'views/maintenance_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3'
}