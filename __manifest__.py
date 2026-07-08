# -*- coding: utf-8 -*-
{


    'description': """
    """,

    'author': "wail sari bey",
    'website': "https://wailsb.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list

    'name': 'Custom Maintenance SI',
    'version': '18.0.1.0.0',
    'category': 'Maintenance',
    'summary': 'Internal Enterprise Information System for Machine Maintenance Pipelines',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/maintenance_sequence.xml',
        'views/maintenance_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3'
    # only loaded in demonstration mode
}

