# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import UserError

class SaleOrder(models.Model):
	_inherit = "sale.order"

	doc_ref = fields.Char(string='Document Ref')
	forum_code = fields.Char(string='Forum Code')
	digital_signature = fields.Binary(string='Approver Sign')

	def action_cancel(self):
		res = super(SaleOrder, self).action_cancel()
		if not self.digital_signature:
			raise UserError(_('Please cancel after getting Approver Signature'))
		return res