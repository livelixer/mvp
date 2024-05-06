from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        rake_club = float(request.form['rake_club'])
        rakeback = float(request.form['rakeback'])
        rake_me = float(request.form['rake_me'])
        rake_vitalik = float(request.form['rake_vitalik'])
        winrate_me = float(request.form['winrate_me'])
        winrate_vitalik = float(request.form['winrate_vitalik'])
        rebate_club = float(request.form['rebate_club'])
        overlay = float(request.form['overlay'])

        rebate_my = abs(winrate_me + rake_me) * 0.1
        rebate_vitalik = abs(winrate_vitalik + rake_vitalik) * 0.1

        if (winrate_me + rake_me) >= 0:
            my = (rake_me * 0.83) + winrate_me - rebate_my
        else:
            my = (rake_me * 0.83) + winrate_me + rebate_my

        if (winrate_vitalik + rake_vitalik) >= 0:
            vitalik = (rake_vitalik * 0.83) + winrate_vitalik - rebate_vitalik
        else:
            vitalik = (rake_vitalik * 0.83) + winrate_vitalik + rebate_vitalik

        ostatok = (rake_club - rake_vitalik - rake_me - rakeback) * 0.83 + (rebate_club - rebate_vitalik - rebate_my)

        my_funds = my + ostatok / 2 - overlay / 2

        return render_template('index.html', my_funds=my_funds)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
