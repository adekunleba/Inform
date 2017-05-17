from . import main
from flask import render_template, redirect, url_for
from .forms import Drug, PremiseForm, PatientForm
from ..models import Premise, DrugDB
from .. import db
from flask_login import current_user


@main.route('/')
@main.route('/index', methods=['GET', 'POST'])
def index():
    drug_form = Drug()
    patient_form = PatientForm()
    if drug_form.validate_on_submit():
        drug = DrugDB()
        drug.name = drug_form.drugName.data
        drug.route = drug_form.drugRoute.data
        drug.dose = drug_form.drugStrenght.data
        drug.duration = drug_form.drugDuration.data
        db.session.add(drug)
        db.session.commit()
        return redirect(url_for('.premise'))
    return render_template("patient.html", drug_form=drug_form, patient_form=patient_form)


@main.route('/premise', methods=['GET', 'POST'])
def premise():
    form = PremiseForm()
    if form.validate_on_submit():
        premise = Premise(name=form.name.data,
                          address=form.address.data)
        db.session.add(premise)
        db.session.commit()
        return redirect(url_for('.index'))
    return render_template("premise.html", form=form)

