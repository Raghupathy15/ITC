# -*- coding: utf-8 -*-

from odoo import api, fields, models, _, tools


class PuchaseExtend(models.Model):
    _inherit = "purchase.order"
    _description = "Purchase Order Extend"

    od_number = fields.Char(string='ODNumber')
    batch = fields.Char(string='Batch')

    def button_confirm(self):
        res = super(PuchaseExtend, self).button_confirm()
        self.order_line.uom_trigger()
        return res


class PurchaseOrderLineExtend(models.Model):
    _inherit = 'purchase.order.line'
    _description = 'Purchase Order Line'

    @api.onchange('product_id')
    def _onchange_hsn(self):
        for line in self:
            if line.product_id:
                for product_master in self.env['product.product'].search([('id', '=', line.product_id.id)]):
                    line.hsn_code = product_master.l10n_in_hsn_code

    hsn_code = fields.Char(string='HSN Code')

    def uom_trigger(self):
        for line in self:
            if line.product_id:
                for product_master in self.env['product.product'].search([('id', '=', line.product_id.id)]):
                    line.write({
                        'product_uom': product_master.uom_po_id.id
                    })
