from odoo import api, fields, models, _
from odoo.addons import decimal_precision as dp
import re
from odoo.exceptions import ValidationError

import qrcode
import base64
from io import BytesIO

class ProductTemplate(models.Model):
	_inherit = "product.template"

	default_code = fields.Char('Product Code', compute='_compute_default_code',inverse='_set_default_code', store=True)
	product_description = fields.Char("Description")
	manufacturer = fields.Char("Manufacturer")
	brand = fields.Char("Brand")
	batch_tracked = fields.Selection([('yes', 'Yes'),('no', 'No')], string='Batch Tracked')
	pkd_tracked = fields.Selection([('yes', 'Yes'),('no', 'No')], string='PKD Tracked')
	conversion_factor = fields.Integer("Conversion Factor")
	conversion_unit_id = fields.Many2one('uom.uom',"Conversion Unit")
	spl_price = fields.Float("Special Price")
	adhoc_amount = fields.Float("Adhoc amount")
	purchased_at = fields.Char("Purchased At")
	health_item = fields.Selection([('yes', 'Yes'),('no', 'No')], string='Health care item')
	# Tax details
	tax_inclusive_rate = fields.Float("Tax Inclusive Rate")
	vat = fields.Selection([('yes', 'Yes'),('no', 'No')], string='VAT')
	collect_tax = fields.Selection([('yes', 'Yes'),('no', 'No')], string='Collect Tax Suffered')
	# UOM Details
	uom1_id = fields.Many2one('uom.uom',"UOM 1")
	uom1_conversion_id = fields.Many2one('uom.uom',"UOM 1 Conversion")
	uom2_id = fields.Many2one('uom.uom',"UOM 2")
	uom2_conversion_id = fields.Many2one('uom.uom',"UOM 2 Conversion")
	# Default UOM Details
	purchase_default_uom_id = fields.Many2one('uom.uom',"Purchase default UOM")
	sale_default_uom_id = fields.Many2one('uom.uom',"Sale default UOM")
	# Reporting UOM details
	reporting_uom_id = fields.Many2one('uom.uom',"Reporting UOM")
	reporting_unit = fields.Integer("Reporting Unit")