# Copyright (c) 2023, rohit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _

class ServerSideScripting(Document):
    pass

################# DOCUMENT METHODS #########################################
 
# 1. doc.insert()
# frappe.new_doc("doctype")
# Create New Document in Client side Scripting Using Server Side Script

    # def validate(self):
        # self.new_document()
        
    # def new_document(self):
    #     doc = frappe.new_doc('Client Side Scripting')
    #     doc.first_name = "Jake"
    #     doc.last_name = "Jay"
    #     doc.age = 25
    #     doc.append("family_members", {
    #         "name1" : "jain",
    #         "relation" : "Sister",
    #         "age" : 21
    #     })
    #     doc.insert()
    
    # some escape hatches that can be used to skip certain checks
    # doc.insert(
    #     ignore_permissions = True, # ignore write permissions during insert
    #     ignore_links = True, # ignore link validation in document
    #     igonre_if_duplicate = True # dont insert id DuplicateEntryError is thrown
    #     ignore_if_mandatory = True # insert even if mandatory fields are not set
    # )
 
 
 # 2. frappe.get_doc(doctype, name)
 # Returns a Document objetc of record identified by doctype and name
 
    # def validate(self):
        # self.get_document()
        
    # def get_document(self):
        # doc = frappe.get_doc('Client Side Scripting', self.client_side_doc)
        
        # frappe.msgprint(_("The first name is {0} and age is {1}").format(doc.first_name, doc.age))
        
        # for row in doc.get("family_members"):
        #     frappe.msgprint(_("{0}. The family member name is '{1}' and relation is '{2}'").format(row.idx, row.name1, row.relation))
       
        
# 3. frappe.delete_doc("doctype", "name")
# Delete doc with specific name from doctype list

    # def validate(self):
        # frappe.delete_doc("Client Side Scripting", "CLIENT-000001")
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
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
    
    
        
    