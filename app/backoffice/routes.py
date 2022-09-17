from app.backoffice import back_bp
from app.backoffice.models import Account, Branch, Customer, Employee
from app.backoffice.forms import AddEmployeeForm, AddCustomerForm
from app import db


from flask import render_template, url_for, redirect, flash



@back_bp.route("/backoffice/branch-details")
def backoffice():
    branch = Branch.query.first()
    return render_template(
        "branch-details.html",
        branch=branch
    )

@back_bp.route("/backoffice/create-branch")
def create_branch():
    return "No branch"

@back_bp.route("/backoffice/add-customer", methods=["POST","GET"])
def add_customer():
    form = AddCustomerForm()
    if form.validate_on_submit():
        customer = Customer.query.filter_by(
            nin=form.nin_number.data, 
            phone=form.phone.data, 
            email=form.email.data).first()
        branch = Branch.query.filter_by(rcode=form.branch.data).first()
        if branch is None:
            return redirect(url_for("back_bp.create_branch"))
        if customer is None:
            customer = Customer({
                "fname": form.fname.data,
                "lname": form.lname.data,
                "branch": branch,
                "gender": form.gender.data,
                "d_o_b": form.d_o_b.data,
                "phone": form.phone.data,
                "nin": form.nin_number.data,
                "email": form.email.data,
                "address": form.address.data,
                "occupation": form.occupation.data
            })
            account = Account({
                "kind": form.kind.data,
                "holder": customer,
                "branch": branch,
                "nin": form.nin_number.data,
            })
            db.session.add_all([account, customer])
            db.session.commit()
            flash("Customer added successfully")
        else:
            flash("Customer already exists!")
        return redirect(url_for("back_bp.backoffice"))
    return render_template(
        "add-customer.html",
        form=form
    )


@back_bp.route("/backoffice/add-employee", methods=["POST","GET"])
def add_employee():
    form = AddEmployeeForm()
    if form.validate_on_submit():
        #branch = Branch.query.filter_by(rcode=form.rcode.data).first_or_404()
        customer = Customer.query.filter_by(c_id=form.c_id.data).get_or_404()
        employee = Employee.query.filter_by(e_id=form.e_id.data).first()

        if employee is None:
            employee = Employee({
                "title": form.title.data,
                "branch": None
            })
    return render_template(
        "add-employee.html",
        
    )
