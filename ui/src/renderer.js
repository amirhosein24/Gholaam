// renderer.js
const { ipcRenderer } = require('electron');
const axios = require('axios');

window.addEventListener('DOMContentLoaded', () => {
  const recordButton = document.getElementById('record-button');
  let isRecording = false;

  recordButton.addEventListener('click', async () => {
    if (!isRecording) {
      try {
        await axios.post('http://127.0.0.1:8000/start-recording');
        recordButton.textContent = 'Stop Recording';
        recordButton.classList.add('recording');
        isRecording = true;
      } catch (error) {
        alert('Failed to start recording.');
        console.error(error);
      }
    } else {
      try {
        const response = await axios.post('http://127.0.0.1:8000/stop-recording');
        recordButton.textContent = 'Start Recording';
        recordButton.classList.remove('recording');
        isRecording = false;
        alert(`Recording saved as ${response.data.filename}`);
      } catch (error) {
        alert('Failed to stop recording.');
        console.error(error);
      }
    }
  });
});
