from chalice import Chalice, Response

app = Chalice(app_name="aoc")

Words = {
    "232": "Yule",
    "262": "Gingerbread",
    "1119": "Magi",
    "522": "Nutcracker",
    "3448043": "Tidings",
    "1019571": "Holly Jolly",
    "1559": "Kris Kringle",
    "71506": "Sleigh bells",
}

answer = {
    "2015": "232",
    "2016": "262",
    "2017": "1119",
    "2018": "522",
    "2019": "3448043",
    "2020": "1019571",
    "2021": "1559",
    "2022": "71506"
}

years = ["2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"]


@app.route("/{year}", methods=["GET"])
def get_year(year):
    if year not in years:
        return Response(
            body="Invalid year",
            status_code=400,
            headers={"Content-Type": "text/plain"},
        )
    if year == "2023":
        return Response(
            body="submit all the code words for the years 2015-2022 separated by a comma.",
            status_code=200,
            headers={"Content-Type": "text/plain"},
        )
    with open(f"./chalicelib/input/{year}.txt") as f:
        return Response(
            body=f.read(), status_code=200, headers={"Content-Type": "text/plain"}
        )


@app.route("/{year}", methods=["POST"], content_types=["text/plain"])
def post_year(year):
    request = app.current_request.raw_body.decode()
    if year not in years:
        return Response(
            body="Invalid year",
            status_code=400,
            headers={"Content-Type": "text/plain"},
        )
    
    if year == "2023":
        words = request.split(",")
        if len(words) != 8:
            return Response(
                body="Invalid number of words",
                status_code=400,
                headers={"Content-Type": "text/plain"},
            )
        if all(w in Words.values() for w in words):
            return Response(
                body="Correct! You saved Christmas!",
                status_code=200,
                headers={"Content-Type": "text/plain"},
            )
        
    if request == answer[year]:
        return Response(
            body=Words[request],
            status_code=200,
            headers={"Content-Type": "text/plain"},
        )


# return html page for help
@app.route("/", methods=["GET"])
def get_help():
    return Response(
        body=open("chalicelib/index.html").read(),
        status_code=200,
        headers={"Content-Type": "text/html"},
    )
