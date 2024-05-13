# # import frappe


# def change_label():
#     install_app(site_name)
#     print("hello world")
#     # meta = frappe.get_meta("Payment Reconciliation")

#     # field = meta.get_field("from_invoice_date")

#     # field.label = "New-Label"

#     # meta.save()

# import subprocess

# # def install_erpnext(site_name):
# #     try:
        
# #         # Install ERPNext
# #         subprocess.check_call(["bench", "get-app", "erpnext", "https://github.com/frappe/erpnext"])
# #         subprocess.check_call(["bench", "--site","install-app",site_name, "erpnext",  ])

# #         print("ERPNext installed successfully!")
# #     except subprocess.CalledProcessError as e:
# #         print(f"An error occurred while installing ERPNext: {e}")import subprocess

# def install_app(site_name):
#     try:
#         # Verify bench command
#         subprocess.check_call(["bench", "--version"])

    

#         # Confirm ERPNext app
#         subprocess.check_call(["bench", "--site", site_name, "list-apps"])
#         subprocess.check_call(["bench", "get-app", "erpnext", "https://github.com/frappe/erpnext"])
#         # Install ERPNext app
#         subprocess.check_call(["bench", "--site", site_name, "install-app", "erpnext"])

#         print("ERPNext installed successfully!")
#     except subprocess.CalledProcessError as e:
#         print(f"An error occurred while installing ERPNext: {e}")

# # Provide the site name as an argument
# site_name = "tijaabo"



# import subprocess
# import os

# def change_label():
#     install_erpnext("tijaabo")
#     print("hello world")
#     # meta = frappe.get_meta("Payment Reconciliation")
#     # field = meta.get_field("from_invoice_date")
#     # field.label = "New-Label"
#     # meta.save()

# def install_erpnext(site_name):
    
#     try:
        
#         # Install ERPNext
#         subprocess.check_call(["bench", "get-app", "erpnext", "https://github.com/frappe/erpnext"])
#         subprocess.check_call(["bench", "--site", site_name, "install-app", "erpnext"])

#         print("ERPNext installed successfully!")
#     except subprocess.CalledProcessError as e:
#         if "LockTimeoutError" in str(e):
#             # Remove the lock file
#             lock_file = os.path.join("sites", site_name, "locks", "install_app.lock")
#             os.remove(lock_file)
#             print(f"Lock file removed. Retry the installation.")
#         else:
#             print(f"An error occurred while installing ERPNext: {e}")

# change_label()


import subprocess
import os


def change_label():
    site_name = "tijaabo"
    file = os.path.abspath(__file__)
    folder = os.path.dirname(file)[:-21] 
    remove_lock_file(folder, site_name)
    install_erpnext(site_name)
    print("Hello, world!")


def remove_lock_file(folder, site_name):
    rm_file = os.path.join(folder, "sites", site_name, "locks", "install_app.lock")
    if os.path.exists(rm_file):
        os.remove(rm_file)
        print("Lock file removed successfully.")
    else:
        print("Lock file does not exist.")


def install_erpnext(site_name):
    try:
        # Install ERPNext
        subprocess.check_call(["bench", "get-app", "erpnext", "https://github.com/frappe/erpnext"])
        subprocess.check_call(["bench", "--site", site_name, "install-app", "erpnext"])

        print("ERPNext installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while installing ERPNext: {e}")
        

change_label()