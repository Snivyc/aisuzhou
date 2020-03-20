from flask import Flask, jsonify, render_template
from flask_cors import CORS
from tongji import *

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route("/")
def b():
    return render_template("index.html", id=8, b_ids = [1,2], bb_ids = [2,3])

@app.route("/a/<id>/")
def a(id):
    a_set = {int(id)}
    b_set = get_related_id(int(id))
    b_ids = list(b_set - a_set)

    b_ids.sort()

    bb_set = set()
    for i in b_ids:
        for j in get_related_id(i):
            bb_set.add(j)

    bb_set = bb_set - b_set - a_set
    bb_ids = list(bb_set)
    bb_ids.sort()

    # print(b_ids)
    return render_template("b.html", id = id, b_ids = b_ids, bb_ids = bb_ids)

@app.route('/api/getpoints/<id>/')
def hello_world(id):
    longest_path = paths[int(id)]
    t1 = set(longest_path)
    t2 = get_related_points(longest_path) - t1
    t3 = get_related_points(t2) - t2 - t1
    return jsonify(path_to_xypath(t3, 2) + path_to_xypath(t2, 1) + path_to_xypath(t1, 3))

    # return jsonify(s3 + s2 + s1)
