# main.py
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pyaudio
import wave
import threading
import datetime

app = FastAPI()
# audio = pyaudio.PyAudio()
# stream = None
# frames = []
# recording = False
# def record_audio():
#     global stream, frames, recording
#     stream = audio.open(
#         format=pyaudio.paInt16,
#         channels=2,
#         rate=44100,
#         input=True,
#         frames_per_buffer=1024
#     )
#     frames = []
#     while recording:
#         data = stream.read(1024)
#         frames.append(data)
#     stream.stop_stream()
#     stream.close()


# @app.post("/start-recording")
# def start_recording():
#     print("yoyo")
#     print("--------------------------------------")


#     global recording, thread
#     if recording:
#         return JSONResponse(content={"message": "Recording already in progress"}, status_code=400)
#     recording = True
#     thread = threading.Thread(target=record_audio)
#     thread.start()
#     return {"message": "Recording started"}


# @app.post("/stop-recording")
# def stop_recording():
#     global recording, frames
#     if not recording:
#         return JSONResponse(content={"message": "No recording in progress"}, status_code=400)
#     recording = False
#     thread.join()
#     filename = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".wav"
#     wf = wave.open(filename, 'wb')
#     wf.setnchannels(2)
#     wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
#     wf.setframerate(44100)
#     wf.writeframes(b''.join(frames))
#     wf.close()
#     return {"message": "Recording stopped", "filename": filename}
# thread = None


# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


# def record_audio():
#     global stream, frames, recording
#     stream = audio.open(
#         format=pyaudio.paInt16,
#         channels=2,
#         rate=44100,
#         input=True,
#         frames_per_buffer=1024
#     )
#     frames = []
#     while recording:
#         data = stream.read(1024)
#         frames.append(data)
#     stream.stop_stream()
#     stream.close()


@app.post("/start-recording")
def start_recording():
    print("started recondringgggggggggggggggg")


#     global recording, thread
#     if recording:
#         return JSONResponse(content={"message": "Recording already in progress"}, status_code=400)
#     recording = True
#     thread = threading.Thread(target=record_audio)
#     thread.start()
#     return {"message": "Recording started"}


@app.post("/stop-recording")
def stop_recording():
    print("stoped recondringgggggggggggggggg")


#     global recording, frames
#     if not recording:
#         return JSONResponse(content={"message": "No recording in progress"}, status_code=400)
#     recording = False
#     thread.join()
#     filename = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".wav"
#     wf = wave.open(filename, 'wb')
#     wf.setnchannels(2)
#     wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
#     wf.setframerate(44100)
#     wf.writeframes(b''.join(frames))
#     wf.close()
#     return {"message": "Recording stopped", "filename": filename}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=9090)
