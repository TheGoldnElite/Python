from flask_app import app
from flask import render_template,redirect,request,flash,session
from flask_app.models.recipe import Recipe
from flask_app.models.user import User




@app.route('/recipes/new')
def newrecipes():


    return render_template("newrecipes.html")

@app.route("/create/recipe",methods=['POST'])
def create_recipe():
    if Recipe.validate_recipe(request.form):
        data={
            'name': request.form['name'],
            'description': request.form['description'],
            'instructions':request.form['instructions'],
            'user_id':session['user_id']
        }
        Recipe.save_recipe(data)
    else:  
        print("is not valid")
        return redirect ('/recipes/new')
    

    return redirect('/dashboard')


@app.route("/instructions/<int:recipe_id>")
def instructions(recipe_id):
    if 'user_id' not in session:
        flash("You must be logged in to view this website")
        return redirect('/')

    data={
        "user_id":session['user_id']
    }
    user=User.get_id(data)

    data = {
        "recipe_id": recipe_id
    }
    recipe=Recipe.recipeone(data)
    
    return render_template("instructions.html",user=user,recipe=recipe)

@app.route("/edit/<int:recipe_id>")
def edit(recipe_id):
    data = {
        "recipe_id": recipe_id
    }
    recipe=Recipe.recipeone(data)
    return render_template("edit.html",recipe=recipe)



@app.route("/update/<int:recipe_id>",methods=['POST'])
def update_recipe(recipe_id):
    if Recipe.validate_recipe(request.form):
        data={
            'name': request.form['name'],
            'description': request.form['description'],
            'instructions':request.form['instructions'],
            'recipe_id': recipe_id
        }
        
    else:  
        return redirect (f"/edit/{recipe_id}")
    Recipe.update_recipe(data)
    

    return redirect('/dashboard')


@app.route("/delete/<int:recipe_id>")
def delete(recipe_id):
    data = {
        "recipe_id": recipe_id
    }
    Recipe.delete(data)
    return redirect("/dashboard")