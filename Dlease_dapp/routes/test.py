from flask import Blueprint, render_template

test = Blueprint('test', __name__)

@test.route('/test', methods=['GET'])
def test_endpoint():
   return render_template('test.html')