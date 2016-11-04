from dateutil.relativedelta import relativedelta

from openerp.osv import osv, fields
from openerp.tools.translate import _
from datetime import datetime


class ResPartnerNew(osv.osv):
    _inherit = 'res.partner'

    # Generate comparisons between previous yr and current yr
    def get_comparison_saleline_ytd(self, cr, uid, ids, context=None):
        print "Method Called########################################"
        # fiscal_year_obj = self.pool.get('account.fiscalyear')
        # sale_line_ytd_obj = self.pool.get('sale.line.ytd')
        # today_date = datetime.now().strftime("%Y")
        # # Get Previous Year
        # pre_year = int(today_date) - 1
        # # Get Current Year
        # curr_year = int(today_date)
        # comparison_data = {}
        # for partner_brw in self.browse(cr, uid, ids):
        #     # Get All Sale Lines
        #     sale_lines = sale_line_ytd_obj.search(cr, uid, [('partner_id', 'in', [partner_brw.id])])
        #     # Delete all current sale lines to repopulate db with recalculated ones
        #     sale_line_ytd_obj.unlink(cr, uid, sale_lines)
        #     # Search to see if last year record exists where code is one year less than current &
        #     # company_id is the current partner's company id.
        #     fiscal_search = fiscal_year_obj.search(cr, uid, [('code', '=', pre_year),
        #                                                      ('company_id', '=', partner_brw.company_id.id)])
        #     # Fetch Previous year data
        #     for fiscal_date in fiscal_year_obj.browse(cr, uid, fiscal_search):
        #         #
        #         current_date = datetime.now() - relativedelta(years=1)
        #         print "current_date",current_date
        #         last_todays_date = current_date.strftime("%m/%d/%Y")
        #         cr.execute("""select distinct line.product_id, line.partner_id,  sum(line.profit_amt), sum(line.profit_perc), sum(line.actual_cost), sum(line.product_uom_qty), sum(line.price_unit), sum(line.price_subtotal_duplicate), product.default_code
        #             from sale_order_line as line
        #             inner join product_product product on line.product_id = product.id
        #             where line.order_id in (select id from sale_order where partner_id = %s and date_invoice <= '%s' and date_invoice >= '%s' and state != 'cancel')
        #             group by line.product_id, line.partner_id, product.default_code order by product.default_code""" % (
        #         partner_brw.id, last_todays_date, fiscal_date.date_start))
        #         data_previous = cr.fetchall()
        #         # print "Data Previous %s" % data_previous
        #         for data in data_previous:
        #             if data[5] > 0 and data[6] > 0:
        #                 price_subtotal_duplicate, product_uom_qty, profit_amt, actual_cost = data[7], data[5], data[2], \
        #                                                                                      data[4]
        #                 price_unit = price_subtotal_duplicate / product_uom_qty
        #                 profit_perc = (profit_amt / actual_cost) * 100 if actual_cost else 0.0
        #                 new_data = (data[0], data[1], data[2], profit_perc, data[4], data[5], price_unit, data[7])
        #             comparison_data[data[8]] = new_data
        #     fiscal_search = fiscal_year_obj.search(cr, uid, [('code', '=', curr_year),
        #                                                      ('company_id', '=', partner_brw.company_id.id)])
        #     # Fetch Current year data
        #     for fiscal_date in fiscal_year_obj.browse(cr, uid, fiscal_search):
        #         current_date = datetime.now()
        #         todays_date = current_date.strftime("%m/%d/%Y")
        #         cr.execute("""select distinct line.product_id, sum(line.profit_amt), sum(line.profit_perc), sum(line.actual_cost), sum(line.product_uom_qty), sum(line.price_unit), sum(line.price_subtotal_duplicate), product.default_code
        #             from sale_order_line as line
        #             inner join product_product product
        #             on line.product_id = product.id
        #             where line.order_id in (select id from sale_order where partner_id = %s and date_invoice <= '%s' and date_invoice >= '%s' and state != 'cancel')
        #             group by line.product_id, line.partner_id, product.default_code order by product.default_code""" % (
        #         partner_brw.id, todays_date, fiscal_date.date_start))
        #         data_current = cr.fetchall()
        #         data_current_dic = {}
        #         # print "Data Current %s" % data_current
        #         for data in data_current:
        #             data_current_dic[data[7]] = data
        #             key_default_code = data[7]
        #             # print "key_default_code %s" % key_default_code
        #             if data[7] in comparison_data.keys():
        #                 old_val = list(comparison_data[data[7]])
        #                 # Calculation of profit% and price unit values
        #                 if data[4] > 0 and data[5] > 0:
        #                     price_subtotal_duplicate, product_uom_qty, profit_amt, actual_cost = data[6], data[4], data[
        #                         1], data[3]
        #                     price_unit = price_subtotal_duplicate / product_uom_qty
        #                     profit_perc = (profit_amt / actual_cost) * 100 if actual_cost else 0.0
        #                     new_data = (data[0], data[1], profit_perc, data[3], data[4], price_unit, data[6])
        #                     data = new_data
        #                 old_val.extend(data[1:])
        #                 comparison_data[key_default_code] = tuple(old_val)
        #             else:
        #                 previous_val = [data[0], partner_brw.id, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        #                 previous_val.extend(data[1:-1])
        #                 comparison_data[data[7]] = tuple(previous_val)
        #
        #         difference = set(data_current_dic.keys()) ^ set(comparison_data.keys())
        #         for diff in difference:
        #             curr_val = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        #             if diff in comparison_data.keys():
        #                 old_val = list(comparison_data[diff])
        #                 old_val.extend(curr_val)
        #                 comparison_data[diff] = tuple(old_val)
        #     if comparison_data:
        #         # sorting values according to 'default_code'
        #         sorted_keys = sorted(comparison_data.keys())
        #         all_data = []
        #         change_counter = 0
        #         for key in sorted_keys:
        #             comp_data_tuple = comparison_data.get(key)
        #             all_data.append(comp_data_tuple)
        #             change_counter += 1
        #         stmnt = "insert into sale_line_ytd (product_id,partner_id,pre_profit_amt,pre_avg_profit,pre_net_subtotal,pre_qty,pre_unit_price,pre_subtotal,curr_profit_amt,curr_avg_profit,curr_net_subtotal,curr_qty,curr_unit_price,curr_subtotal) values \
        #                      (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        #         cr.executemany(stmnt, all_data)
        #     sale_lines = sale_line_ytd_obj.search(cr, uid, [('partner_id', 'in', [partner_brw.id])])
        return {
            'name': _('Open Sales Order Lines'),
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'sale.line.ytd',
            'view_id': False,
            'domain': "[('id','in',[" + ','.join(map(str, sale_lines)) + "])]",
            'type': 'ir.actions.act_window',
        }