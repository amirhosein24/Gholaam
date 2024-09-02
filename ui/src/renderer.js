// renderer.js
window.addEventListener('DOMContentLoaded', () => {
    const recordButton = document.getElementById('record-button');
    let isRecording = false;
  
    recordButton.addEventListener('click', async () => {
      if (!isRecording) {
        try {
          const response = await fetch('http://127.0.0.1:9090/start-recording', {
            method: 'POST',
          });
          if (response.ok) {
            recordButton.textContent = 'Stop Recording';
            recordButton.classList.add('recording');
            isRecording = true;
          } else {
            alert('Failed to start recording.');
          }
        } catch (error) {
          alert('Failed to start recording.');
          console.error(error);
        }
      } else {
        try {
          const response = await fetch('http://127.0.0.1:9090/stop-recording', {
            method: 'POST',
          });
          if (response.ok) {
            const data = await response.json();
            recordButton.textContent = 'Start Recording';
            recordButton.classList.remove('recording');
            isRecording = false;
            alert(`Recording saved as ${data.filename}`);
          } else {
            alert('Failed to stop recording.');
          }
        } catch (error) {
          alert('Failed to stop recording.');
          console.error(error);
        }
      }
    });
  });
  