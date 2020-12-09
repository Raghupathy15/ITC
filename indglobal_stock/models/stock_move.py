# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class StockMove(models.Model):
    _inherit = "stock.move"

    display_assign_lot = fields.Boolean(compute='_compute_display_assign_lot')

    @api.depends('has_tracking', 'picking_type_id.use_create_lots', 'picking_type_id.use_existing_lots', 'state')
    def _compute_display_assign_lot(self):
        for move in self:
            move.display_assign_lot = (
                    move.has_tracking == 'lot' and
                    move.state in ('partially_available', 'assigned', 'confirmed') and
                    move.picking_type_id.use_create_lots and
                    not move.picking_type_id.use_existing_lots
            )

    # Assign lot numbers
    def button_create_lots(self):
        self.ensure_one()
        rounding_method = 'UP'
        purchase_uom = self.product_id.uom_po_id
        purchase_qty =self.product_uom._compute_quantity(
                self.product_uom_qty, purchase_uom, rounding_method=rounding_method)
        purchase_qty= int(purchase_qty)
        if len(self.move_line_nosuggest_ids) < purchase_qty:
            purchase_qty = purchase_qty - len(self.move_line_nosuggest_ids)
        else:
            return self.action_show_details()
        move_line_vals = {
            'product_id': self.product_id.id,
            'product_uom_id': self.product_id.uom_po_id.id,
            'qty_done': 1,
        }
        move_lines_commands = []
        for i in range(purchase_qty):
            lot = self.env['ir.sequence'].next_by_code('lot.seq') or '/'
            move_line_cmd = dict(move_line_vals, lot_name=lot)
            move_lines_commands.append((0, 0, move_line_cmd))
            i += 1
        self.write({'move_line_nosuggest_ids': move_lines_commands})
        return self.action_show_details()