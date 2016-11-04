from openerp.osv import osv, fields

class ProductProduct(osv.osv):

    _inherit = 'product.product'
    _columns = {
        'boat_length': fields.char('Boat Length', size=10),
        'fuel_capacity': fields.char('Fuel Capacity', size=10),
        'model_options_id': fields.many2one('product.category', 'Model Options'),
        'variant_group_id': fields.many2one('product.variant.group', 'Variant Group'),
    }

    def search(self, cr, uid, args, offset=0, limit=None, order=None, context=None, count=False):
        print context
        if context is None:
            context = {}
        if context.get('boat_model_id'):

            product_obj = self.pool.get('product.product').read(cr, uid, context['boat_model_id'],['model_options_id'])
            lookup_category = product_obj['model_options_id'][0]
            if product_obj:
                args = [('categ_id','=',lookup_category)] + args
            else:
                args = [('categ_id', '=', 0)] + args
        return super(ProductProduct, self).search(cr, uid, args, offset=offset, limit=limit, order=order, context=context, count=count)

class SaleOrder(osv.osv):

    _inherit = 'sale.order'

    _columns = {
        'boat_model_id': fields.many2one('product.product',"Boat Model",domain=[('categ_id.name','=','Boat Models')]),
    }

class SaleOrderLine(osv.osv):

    _inherit = 'sale.order.line'

    _columns = {
        'variant_id': fields.many2one('product.variant',"Variant")
    }


class ProductVariantGroup(osv.osv):

    _name = 'product.variant.group'
    _columns = {
        'name': fields.char('Variant Group', size=64),
        'description': fields.text('Description'),
        'variants': fields.one2many('product.variant', 'variant_group_id', 'Variants'),
    }


class ProductVariant(osv.osv):
    _name = 'product.variant'

    _columns = {
        'name': fields.char('Variant', size=64),
        'description': fields.text('Description'),
        'variant_group_id': fields.many2one('product.variant.group', 'Variant Group'),
    }


    def _name_search(self, cr, user, name='', args=None, operator='ilike', context=None, limit=100, name_get_uid=None):
        if context is None:
            context = {}
        if context.get('product_lookup'):
            product_look_up = context.get('product_lookup')
            product_obj = self.pool.get('product.product').read(cr, user, [product_look_up], context=context)

            # In Openerp v7 we get error if variant_group_id is False
            # To counter it we specify this if...else condition
            if product_obj['variant_group_id']:
                args = [('variant_group_id', '=', product_obj['variant_group_id'].id)] + args
            else:
                args = [('variant_group_id', '=', 0)] + args

            # For Odoo v8, the method has already handled this exception
            # args = [('variant_group_id', '=', product_obj['variant_group_id'].id)] + args

        return super(ProductVariant,self)._name_search(cr, user, name=name, args=args, operator=operator, context=context, limit=limit, name_get_uid=name_get_uid)