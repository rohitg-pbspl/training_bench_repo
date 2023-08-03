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


# 2. doc.save()
# frappe.new_doc("doctype")
# Save New Document in Client side Scripting Using Server Side Script

    # def validate(self):
        # self.save_document()
        
    # def save_document(self):
    #     doc = frappe.new_doc('Client Side Scripting')
    #     doc.first_name = "Jake"
    #     doc.last_name = "Jay"
    #     doc.age = 25
    #     doc.save()
    
    # some escape hatches that can be used to skip certain checks
    # doc.insert(
    #     ignore_permissions = True, # ignore write permissions during insert
    #     ignore_version = True, # do not create version record
    # )
 
 
# 3. doc.delete()
# frappe.delete_doc("doctype", "name")
# Delete doc with specific name from doctype list

    # def validate(self):
        # self.delete_document()
        # frappe.delete_doc("Client Side Scripting", "CLIENT-000001")   # this can also be used to delete doc
        
    # def delete_document(self):
    #     doc = frappe.get_doc('Client Side Scripting', "CSC0001")
    #     doc.delete()
    
# 4. doc.db_set()
    # def validate(self):
        # self.db_set_document()
        
    # def db_set_document(self):
        # doc = frappe.get_doc('Client Side Scripting', "CSC0001")
        # doc.db_set('age', 25)  
        
        
        
############################## GET DOCTYPE ###############################################
 # frappe.get_doc(doctype, name)
 # Returns a Document objetc of record identified by doctype and name
 
    def validate(self):
        self.get_document()
        
    def get_document(self):
        doc = frappe.get_doc('Client Side Scripting', self.client_side_doc)
        
        frappe.msgprint(_("The first name is {0} and age is {1}").format(doc.first_name, doc.age))
        
        # for row in doc.get("family_members"):
        #     frappe.msgprint(_("{0}. The family member name is '{1}' and relation is '{2}'").format(row.idx, row.name1, row.relation))
 
 
 
 ################################## EVENTS #################################################
 
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
    


############################################ VALUE FETCHING #####################################################

    # def validate(self):
        # frappe.msgprint(_("Hello My Full Name is '{0}'").format(self.first_name + " " + self.middle_name+ " " + self.last_name))  
        
        # for row in self.get('family_members'):
        #     frappe.msgprint(_("{0}. The family member name is '{1}' and relation is '{2}'").format(row.idx, row.name1, row.relation))
        
        
        
############################################## GET LIST #######################################################

# Data Base API

# frappe.db.get_list(doctype, filters, or_filters, fields, order_by, group_by, start, page_length)

    # def validate(self):
    #     self.get_list()
        
    # def get_list(self):
    #     doc = frappe.db.get_list('Client Side Scripting', 
    #                              filters={
    #                                  'enable':1
    #                              },
    #                              fields = ['first_name', 'age']
    #                              )
    #     for d in doc:
    #         frappe.msgprint(_("First Name is {0} and age is {1}").format(d.first_name, d.age))
            
            


############################################## GET VALUE #######################################################
            
# frappe.db.get_value(doctype, name, fieldname) or frappe.db.get_value(doctype, filters, fieldname)

    # def validate(self):
    #     self.get_value()
        
    # def get_value(self):
    #     first_name, age = frappe.db.get_value('Client Side Scripting', "CSC0008", ['first_name', 'age'])
    #     frappe.msgprint(_("First Name is {0} and age is {1}").format(first_name, age))
    #     print(first_name, age)
    
    


############################################## SET VALUE #######################################################

# frappe.db.set_value(doctype, name, fieldname, value)

    # def validate(self):
    #     self.set_value()
    
    # def set_value(self):
    #     frappe.db.set_value('Client Side Scripting', 'CSC0001', 'age', 78)
        
    #     first_name, age = frappe.db.get_value('Client Side Scripting', "CSC0001", ['first_name', 'age'])
    #     frappe.msgprint(_("First Name is {0} and age is {1}").format(first_name, age))
    #     print(first_name, age)
    
    
    
######################################## DOES EXISTS #############################################################

# frappe.db.exists(doctype, name)

    # def validate(self):
    #     if frappe.db.exists('Client Side Scripting', 'CSC-0001'):
    #         frappe.msgprint(_("Document exists in database"))
    #     else:
    #         frappe.msgprint(_('Document does not exists in database'))
    
    
    
############################ COUNT ENTRIES #########################################################################

# frappe.doctype.count(doctype, filters)
    
    # def validate(self):
    #     count = frappe.db.count('Client Side Scripting', {'enable':1})
    #     frappe.msgprint(_("There are {0} Client Side Scripting").format(count))
    
    
    
############################## GET DATA USING SQL QUERIES ###########################################################

# frappe.db.sql(query, filters, as_dict)

    # def validate(self):
    #     self.sql()
    
    # def sql(self):
    #     data= frappe.db.sql(""" SELECT 
    #                                 first_name, age 
    #                             FROM 
    #                                 `tabClient Side Scripting`
    #                             WHERE 
    #                                 enable=1 """, as_dict=1)
                            
    #     for d in data:
    #         frappe.msgprint(_("The Parent First Name is {0} and age is {1}").format(d.first_name, d.age))
    
    
        
        
            
        
    
        
    