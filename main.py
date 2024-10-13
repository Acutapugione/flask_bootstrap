from app import app as frontend_app  # , app2 as backend_app


# from werkzeug.middleware.dispatcher import DispatcherMiddleware
# from werkzeug.serving import run_simple
def main():
    frontend_app.run(debug=True)


# def main():
#     application = DispatcherMiddleware(frontend_app, {"/api": backend_app})

#     run_simple("localhost", 8080, application, use_reloader=True)


if __name__ == "__main__":
    main()
