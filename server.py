from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  title = 'Home Page'
  return render_template('index.html', title=title)

@app.route('/about')
def about():
  title = 'About Page'
  name = 'Hawkeye Smith'
  email = 'Hawkeye@email.com'
  mobile = '000-000-0000'
  age = 24
  return render_template('about.html',
                        title=title,
                        name=name,
                        email=email,
                        mobile=mobile,age=age)


@app.route('/favorite/foods')
def favorite_foods(): 
    foods = ['ข้าวมันไก่', 'ส้มตำ', 'พิซซ่า']
    title = "Favorite Foods"
    return render_template('favorite_foods.html', title=title, foods=foods)


@app.route('/favorite/sports')
def favorite_sports():
    title = 'favorite Sports Page'
    sports = ['ฟุตบอล', 'บาสเก็ตบอล', 'ว่ายน้ำ']
    return render_template('favorite_sports.html', title=title, sports=sports)

