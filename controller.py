
from main import app
@app.route('/')
def index():
    return "Hooray"
@app.route("/fish/<id>")
def get_fish(id):
    print(id)
    return "My fish is gourgeus"
@app.route("/fish")
def get_all_fishes():
    return "All fishes"

@app.route("/fish", methods = ["POST"])
def create_fish():
    return "fish was created"