from app import app
from flask import render_template, redirect, url_for, flash, get_flashed_messages
from datetime import datetime
import forms


@app.route('/')
@app.route('/index')
def index():
    from models import Task
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks, current_title='Custom Title')


@app.route('/add', methods=['GET', 'POST'])
def add():
    from models import Task, db
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        t = Task(title=form.title.data, date=datetime.utcnow())
        db.session.add(t)
        db.session.commit()
        #print('Submitted title', form.title.data)
        flash('Task added to the database')
        return redirect(url_for('index'))
        #return render_template('add.html', form=form, title=form.title.data)
    return render_template('add.html', form=form) #have access to the form

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit(task_id):
    from models import Task, db
    task = Task.query.get(task_id)
    #print(task)
    form = forms.AddTaskForm()
    # if task exists
    if task:
        if form.validate_on_submit():
            task.title = form.title.data
            task.date = datetime.utcnow()
            db.session.commit() # since the data already exists
            flash('Task has been updated')
            return redirect(url_for('index'))

        form.title.data = task.title
        return render_template('edit.html', form=form,task_id=task_id)
    else:
        flash('Task not found')
    return redirect(url_for('index'))


@app.route('/delete/<int:task_id>', methods=['GET', 'POST'])
def delete(task_id):
    from models import Task, db
    task = Task.query.get(task_id)
    #print(task)
    form = forms.DeleteTaskForm()
    # if task exists
    if task:
        if form.validate_on_submit():
            db.session.delete(task)
            db.session.commit() # since the data already exists
            flash('Task has been deleted')
            return redirect(url_for('index'))

        return render_template('delete.html', form=form,
                               task_id=task_id, title=task.title)
    else:
        flash('Task not found')
    return redirect(url_for('index'))