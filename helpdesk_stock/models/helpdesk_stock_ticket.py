# Copyright 2018 Angel Moya
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields


class HelpdeskStockTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    picking_id = fields.Many2one(
        string="Picking",
        comodel_name="stock.picking",
        help="Picking related",
        readonly="True"
    )
