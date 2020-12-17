from flask import Flask, render_template
app = Flask(__name__)


works = [
    {
        'image': 'work-06.jpg',
        'link': '3DDesign',
        'name': '3D Design',
        'description': 'Design for manufacturing, worflow automation...'
    } ,
    {
        'image': 'work-03.jpg',
        'link': '3DPrinting',
        'name': 'Digital manufacturing',
        'description': 'Mainly 3D printing projects'
    },
    {
        'image': 'work-09.jpg',
        'link': 'programming',
        'name': 'Programming',
        'description': 'Main languajes: Java, Python, C'
    },
    {
        'image': 'work-10.jpg',
        'link': 'gameDev',
        'name': 'Game development',
        'description': 'Arcade games using Java or Python'
    },
    {
        'image': 'work-04.jpg',
        'link': 'electronics',
        'name': 'Electronics',
        'description': 'Arduino projects'
    },
    {
        'image': 'work-07.jpg',
        'link': 'Iot',
        'name': 'IoT',
        'description': 'Custom projects made with Arduino and Raspberry Pi'
    }
]


@app.route("/")
def home():
    return render_template('index_template.html', works=works)

@app.route("/user")
def user():
    return render_template('tutorial.html', var="Perez")

@app.route("/work")
def work():
    return render_template("secondary.html")


@app.route("/moddd")
def myWorks():
    return render_template("work/3dd.html")

@app.route("/<work>")
def open_work(work):
    return render_template("tutorial.html", var=work)


if __name__ == "__main__":
    app.run(debug=True)
