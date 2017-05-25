from . import main
from flask import render_template, redirect, url_for, request
from .forms import Drug, PremiseForm, PatientForm, LoginForm, Register
from ..models import Premise, DrugDB, User, Patient
from .. import db
from flask_login import current_user, login_user


@main.route('/drugs', methods=['GET', 'POST'])
def drugs():
    drug_form = Drug()
    premise = Premise.query.filter_by(user_id=current_user.id).order_by('-id').first()
    if drug_form.validate_on_submit():
        patient = Patient.query.filter_by(premise_id=premise.id).order_by('-id').first()
        drug = DrugDB()
        drug.name = drug_form.drugName.data
        drug.route = drug_form.drugRoute.data
        drug.dose = drug_form.drugStrenght.data
        drug.duration = drug_form.drugDuration.data
        drug.user_id = current_user.id
        drug.premise_id = premise.id
        drug.patient_id = patient.id
        db.session.add(drug)
        db.session.commit()
        return redirect(url_for('.drugs'))
    return render_template("drug.html", drug_form=drug_form)


@main.route('/premise', methods=['GET', 'POST'])
def premise():
    form = PremiseForm()
    if form.validate_on_submit():
        premise = Premise(name=form.name.data,
                          state=form.state.data,
                          town=form.town.data,
                          lga=form.lga.data,
                          user_id=current_user.id)
        db.session.add(premise)
        db.session.commit()
        return redirect(url_for('.patient'))
    return render_template("premise.html", form=form)


@main.route('/patient', methods=['GET', 'POST'])
def patient():
    form = PatientForm()
    premise = Premise.query.filter_by(user_id=current_user.id).order_by('-id').first()
    if form.validate_on_submit():
        patient = Patient(name=form.patientName.data,
                          age=form.patientAge.data,
                          state=form.patientState.data,
                          lga=form.patientLGA.data,
                          user_id=current_user.id,
                          premise_id=premise.id)
        db.session.add(patient)
        db.session.commit()
        return redirect(url_for('.drugs'))
    return render_template('patient.html', form=form)


@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    user = User.query.filter_by(email=form.email.data).first()
    if user is not None:
        login_user(user)
        return redirect(request.args.get('next') or url_for('.premise'))
    return render_template("login.html", form=form)


@main.route('/')
@main.route('/register', methods=['GET', 'POST'])
def register():
    form = Register()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('.login'))
    return render_template('register.html', form=form)
