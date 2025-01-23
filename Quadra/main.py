from website import create_app

app = create_app()

# Para Correr el servidor unicamente desde main.py
if __name__ == '__main__':
    app.run(debug=True)