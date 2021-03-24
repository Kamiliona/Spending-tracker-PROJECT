from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository

merchants_blueprint = Blueprint("merchants", __name__)

@merchants_blueprint.route("/merchants")
def merchants():
    merchants = merchant_repository.select_all()
    return render_template("merchants/index.html", merchants = merchants)

@merchants_blueprint.route("/merchants/new", methods=['GET'])
def new_task():
    merchants = merchant_repository.select_all()
    return render_template ("merchants/new.html", merchants = merchants)

@merchants_blueprint.route("/merchants", methods=['POST'])
def create_merchant():
    # if you entered Tesco for the input field, request.form['merchant] will be tesco
    merchant_name = request.form['merchant_name']
    new_merchant = Merchant(merchant_name)
    merchant_repository.save(new_merchant)
    return redirect ('/merchants')

@merchants_blueprint.route("/merchants/<id>/delete", methods=['POST'])
def delete_merchant(id):
    merchant_repository.delete(id)
    return redirect('/merchants')