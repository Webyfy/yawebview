import yawebview

window = yawebview.Window("DuckDuckGo", "https://duck.com", )
yawebview.start(options=yawebview.Options(
    single_instance_mode = True,
    app_id = "com.gitlab.webyfy.iot.yawebview.examples.sim"
))
