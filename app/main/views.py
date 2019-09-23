from . import main
from flask import render_templates

@main.route('/')
def index():
    '''
    View function to route to index page
    '''


    title = 'Home'
    allBlogs = Blog.query.all()
    reviews = Review.query.all()

    quote = get_quotes()

    return render_template('index.html', title=title, quote=quote, blogs=allBlogs, reviews=reviews)
