# -*- coding: utf-8 -*-
{
    'name': "helpdesk_stock",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'helpdesk',
        'stock',
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/helpdesk_stock_ticket_view.xml',
        'views/helpdesk_stock_return_picking_views.xml',
        'views/helpdesk_stock_picking_form_views.xml',
        'report/helpdesk_picking_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
