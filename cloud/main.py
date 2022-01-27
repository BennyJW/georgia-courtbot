import os
from flask import Flask
from contextlib import redirect_stdout
from datetime import date

# from data.dekalb_scraper import run


app = Flask(__name__)


@app.route("/")
def hello_world():

    name = os.environ.get("NAME", "World")

    today = date.today()
    file_name = f"/tmp/georgia_courtbot_{today.year}_{today.month}_{today.day}.csv"

    # with open(file_name, 'w') as f:
    #     with redirect_stdout(f):
    #         run("csv")

    return "Done!!"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

# if __name__ == '__main__':
#     today = date.today()

#     with open(f"/tmp/georgia_courtbot_{today.year}_{today.month}_{today.day}.csv", 'w') as f:
#         with redirect_stdout(f):
#             run("csv")

