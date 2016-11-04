from openerp.osv import osv, fields
from openerp.tools.translate import _
import time

class SaleLineYtd(osv.osv):
    _name = 'sale.line.ytd'
    _columns = {
        'name': fields.datetime('Report Date'),
        'partner_id': fields.many2one('res.partner', 'Partner'),
        'product_id' : fields.many2one('product.product', 'Product'),
        'pre_profit_amt':fields.float('Profit Amt (Previous)'),
        'pre_avg_profit':fields.float('Average Profit (Previous)'),
        'pre_net_subtotal':fields.float('Net Price Subtotal (Previous)'),
        'pre_qty':fields.float('Qty (Previous)'),
        'pre_unit_price':fields.float('Unit Price (Previous)'),
        'pre_subtotal':fields.float('Subtotal (Previous)'),
        'curr_profit_amt':fields.float('Profit Amt (Current)'),
        'curr_avg_profit':fields.float('Average Profit (Current)'),
        'curr_net_subtotal':fields.float('Net Price Subtotal (Current)'),
        'curr_qty':fields.float('Qty (Current)'),
        'curr_unit_price':fields.float('Unit Price (Current)'),
        'curr_subtotal':fields.float('Subtotal (Current)'),
    }
    _defaults = {
        "name": lambda *a: time.strftime("%Y-%m-%d %H:%M:%S")
    }

class SaleOrderLineYtd(osv.osv):
    _inherit = 'sale.line.ytd'

    _columns = {
        'percent_change_profit': fields.float('% Change Profit'),
        'percent_change_qty': fields.float('% Change Quantity'),
        'percent_change_subtotal': fields.float('% Change Subtotal'),
    }
