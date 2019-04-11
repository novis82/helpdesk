# Copyright 2018 Angel Moya
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields


class HelpdeskStockPicking(models.Model):
    _inherit = 'stock.picking'

    ticket_id = fields.Many2one(
        string="Helpdesk Ticket",
        comodel_name="helpdesk.ticket",
        help="Ticket related",
        readonly="True"
    )
