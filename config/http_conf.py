from bottle import run
def bottle_run():
    # ローカル用の設定
    # run(host='localhost', port=8080, debug=True, reloader=True)

    # heroku用の設定
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

