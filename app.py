from flask import Flask, render_template, request

app = Flask(__name__)

currency_rates = {
    "USD": 80.49,
    "KZT": 0.15,
    "RUB": 1.0,
}


@app.route("/")
def converter():
    form_data = dict(request.args)
    result = 0
    conversion_text = ""

    if len(form_data) > 0:
        amount = float(form_data["summ"])
        from_currency = form_data["from_currency"]
        to_currency = form_data["to_currency"]

        amount_in_rub = amount * currency_rates[from_currency]
        result = amount_in_rub / currency_rates[to_currency]

        conversion_text = f"{amount} {from_currency} = {round(result, 2)} {to_currency}"

    return render_template(
        "index.html", data={"result": result, "conversion_text": conversion_text}
    )


app.run()
