# -*- coding: utf-8 -*-
{
    'name': "Helpdesk Stock",

    "summary": "Module to link Helpdesk with Stock Picking",
    "version": "12.0.1.0.0",
    "category": "",
    "author": "Qubiq"
    "Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "auto_install": "True",


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

}
