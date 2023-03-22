import socketio
import eventlet

sio = socketio.Server()

@sio.on('connect')
def connect(sid, environ):
    print('Client connected:', sid)

@sio.on('disconnect')
def disconnect(sid):
    print('Client disconnected:', sid)

@sio.on('message')
def message(sid, data):
    print('Message received:', data)

if __name__ == '__main__':
    app = socketio.WSGIApp(sio)
    eventlet.wsgi.server(eventlet.listen(('0.0.0.0', 8000)), app)
