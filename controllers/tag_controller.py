from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.tag import Tag
import repositories.tag_repository as tag_repository

tags_blueprint = Blueprint("tags", __name__)

@tags_blueprint.route("/tags")
def tags():
    tags = tag_repository.select_all() # NEW
    return render_template("tags/index.html", tags = tags)

@tags_blueprint.route("/tags/new", methods=['GET'])
def new_task():
    tags = tag_repository.select_all()
    return render_template ("tags/new.html", tags = tags)

@tags_blueprint.route("/tags", methods=['POST'])
def create_tag():
    tag_name = request.form['tag_name']
    new_tag = Tag(tag_name)
    tag_repository.save(new_tag)
    return redirect ('/tags')

@tags_blueprint.route("/tags/<id>/delete", methods=['POST'])
def delete_tag(id):
    tag_repository.delete(id)
    return redirect('/tags')
