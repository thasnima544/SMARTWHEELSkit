// Function to redirect to camera.html (for live monitoring)
function redirectToPage() {
    window.location.href = "camera.html";
  }
  
  // Function to start YOLOv8 Obstacle Detection using webcam
  function startObstacleDetection() {
    fetch('http://localhost:5000/run-yolov8')
      .then(response => {
        if (!response.ok) throw new Error('Failed to start YOLOv8 model');
        return response.text();
      })
      .then(data => {
        alert('Obstacle detection started! Check your webcam feed.');
        console.log('YOLOv8 Response:', data);
      })
      .catch(error => console.error('Error starting YOLOv8:', error));
  }
  
  // Function to run Path Optimization Python code and display output
  function runPathOptimization() {
    fetch('http://localhost:5000/run-path-optimization')
      .then(response => {
        if (!response.ok) throw new Error('Failed to run path optimization code');
        return response.json();
      })
      .then(data => {
        alert('Path Optimization Result: ' + data.result);
        console.log('Path Optimization Output:', data.result);
      })
      .catch(error => console.error('Error running path optimization:', error));
  }
  
  // Function to start Health Monitoring (ECG data)
  function startHealthMonitoring() {
    const ecgSocket = new WebSocket('ws://your-esp32-ip:81');
  
    ecgSocket.onopen = () => {
      console.log('Connected to ECG sensor.');
      alert('Connected to ECG sensor. Waiting for data...');
    };
  
    ecgSocket.onmessage = (event) => {
      const ecgReading = event.data;
      document.getElementById('ecgData').innerText = `ECG Reading: ${ecgReading}`;
      console.log('Live ECG Data:', ecgReading);
    };
  
    ecgSocket.onerror = (error) => {
      console.error('WebSocket Error:', error);
      alert('Failed to connect to ECG sensor.');
    };
  }
  
  // Event listeners for buttons
  document.getElementById('yolov8Button').addEventListener('click', startObstacleDetection);
  document.getElementById('pathOptimizationButton').addEventListener('click', runPathOptimization);
  document.getElementById('healthMonitoringButton').addEventListener('click', startHealthMonitoring);
  
