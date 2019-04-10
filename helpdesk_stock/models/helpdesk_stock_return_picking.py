# Copyright 2018 Angel Moya
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields, _
from odoo.exceptions import UserError
import logging

class HelpdeskStockReturnPicking(models.TransientModel):
    _inherit = 'stock.return.picking'

    ticket_id = fields.Many2one(
        string="Helpdesk Ticket",
        comodel_name="helpdesk.ticket",
        help="Ticket related",
    )

    def create_returns(self):
        res = super(HelpdeskStockReturnPicking, self).create_returns()
        # super(subClass, instance).method(args)
        #logging.info('----------------------')
        #logging.info(res)
        #logging.info(self)
        if not self.ticket_id:
            raise UserError(_('You have to select a helpdesk ticket'))
        picking_id = self.env['stock.picking'].browse(res['res_id'])
        logging.info(picking_id)
        picking_id.update({'ticket_id': self.ticket_id})
        self.ticket_id.write({'picking_id': picking_id.id})
        return res
