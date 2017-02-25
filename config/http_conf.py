import os
from bottle import run
def bottle_run():
    if os.getenv("heroku_flg"):
        # heroku本番用の設定
        run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    else:
        # ローカル用の設定
        run(host='localhost', port=8080, debug=True, reloader=True)

