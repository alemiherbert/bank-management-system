from app.backoffice.models import Customer
from flask_wtf import FlaskForm
from wtforms import DateField, StringField, SelectField, SubmitField
from wtforms import ValidationError
from wtforms.validators import DataRequired, Length


class AddEmployeeForm(FlaskForm):
    e_id = StringField("Customer ID")
    title = StringField("Title")
    rcode = SelectField("Branch", choices=["100", "101", "110", "111"])
    submit = SubmitField("Add Employee")


class AddCustomerForm(FlaskForm):
    fname = StringField(
        "First name",
        validators=[
            DataRequired("This field is required."),
            Length(min=2, max=32, message="The first name must have 2-32 characters")
            ])
    lname = StringField(
        "Last name", 
        validators=[
            DataRequired("This field is required."),
            Length(min=2, max=32, message="The last name must have 2-32 characters")
            ])
    gender = SelectField(
        "Gender", 
        choices=["Male", "Female"], 
        validators=[
            DataRequired("This field is required."),
            ])
    d_o_b = DateField(
        "Date of birth", 
        validators=[
            DataRequired("This field is required."),
            ])
    phone = StringField(
        "Phone", 
        validators=[
            DataRequired("This field is required."),
            Length(min=10, max=10, message="The phone number must have 10 characters")
            ])
    email = StringField(
        "Email", 
        validators=[
            DataRequired("This field is required."),
            Length(min=5, max=32, message="The email must have 5-32 characters")
            ])
    address = StringField(
        "Address", 
        validators=[
            DataRequired("This field is required."),
            Length(min=4, max=128, message="Thie address must have 4-128 characters")
            ])
    occupation = SelectField(
        "Occupation",
        validators=[DataRequired("This field is required.")],
        choices=[
            "Civil Servant",
            "Doctor",
            "Engineer",
            "Farmer",
            "Politician",
            "Lawyer",
            "Retail trader",
            "Social Worker",
            "Teacher",
        ],
    )
    branch = SelectField(
        "Branch",
        choices=["100", "101", "102", "102", "104", "105"],
        validators=[DataRequired("This field is required.")],
    )
    nationality = SelectField(
        "Nationality",
        choices=["Ugandan", "Kenyan", "Tanzanian", "Sudanese", "Rwandan", "Burundian"],
        validators=[DataRequired("This field is required.")],
    )
    kind = SelectField(
        "Account type",
        choices=["Savings Account", "Current Account", "Fixed Deposit"],
        validators=[DataRequired("This field is required.")],
    )
    limit = SelectField(
        "Daily withdrawal limit",
        choices=["1000000", "2000000", "3000000"],
        validators=[DataRequired("This field is required.")],
    )
    n_o_kin = StringField("Next of kin", validators=[DataRequired("This field is required.")])
    nin_number = StringField(
        "National ID number",
        validators=[
            DataRequired("This field is required."),
            Length(min=10, max=10, message="The NIN must have 10 characters.")
            ])
    submit = SubmitField("Save customer details")

    def validate_phone(self, field):
        if Customer.query.filter_by(phone=field.data).first():
            raise ValidationError("Phone number already exists.")


    def validate_email(self, field):
        if Customer.query.filter_by(email=field.data).first():
            raise ValidationError("Email address already exists.")


    def validate_nin(self, field):
        if Customer.query.filter_by(nin=field.data).first():
            raise ValidationError("NIN number already exists.")


    
