# Copyright (c) 2023, rohit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _

class ServerSideScripting(Document):
    pass
	
 ########## EVENTS ############
 
    # def validate(self):
    #     frappe.msgprint('hello frappe validate')
    
    # def before_save(self):
    #     frappe.throw('hello frappe from before_save')

    # def before_insert(self):
    #     frappe.throw('hello farppe from before insert')
    
    # def after_insert(self):
    #     frappe.throw('hello farppe from after insert')
    
    # def on_update(self):
    #     frappe.msgprint('hello farppe from on update')
    
    # def before_submit(self):
    #     frappe.msgprint('hello farppe from before submit')
    
    # def on_submit(self):
    #     frappe.msgprint('hello farppe from on submit')
        
    # def on_cancel(self):
    #     frappe.msgprint('hello farppe from on cancel')
        
    # def on_trash(self):
    #     frappe.msgprint("hello frappe from on trash")
        
    # def after_delete(self):
    #     frappe.msgprint('hello farppe from after delete')
    

########## VALUE FETCHING ###########

    # def validate(self):
        # frappe.msgprint(_("Hello My Full Name is '{0}'").format(self.first_name + " " + self.middle_name+ " " + self.last_name))  
        
        # for row in self.get('family_members'):
        #     frappe.msgprint(_("{0}. The family member name is '{1}' and relation is '{2}'").format(row.idx, row.name1, row.relation))
    
    
        
    