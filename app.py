from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from repository.database import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin123@127.0.0.1:3306/Char-real-time'
app.config['SECRET_KEY'] = 'SECRET_KEY_WEBSOCKET'

db.init_app(app)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

# verificar as mensagens
@socketio.on('message')
def handle_message(msg):
    emit('message', msg, broadcast=True)
    print(f"message {msg} sent")
    
if __name__ == '__main__':
    socketio.run(app, debug=True)