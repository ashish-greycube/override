
from __future__ import unicode_literals

import frappe

@frappe.whitelist()
def get_product_info_for_website(item_code):
	print('===================================================================================')
	print('===================================================================================')
	print('Overrided custom method get_product_info_for_website is called')
	print('===================================================================================')
	print('===================================================================================')