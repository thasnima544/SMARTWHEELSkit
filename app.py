from flask import Flask, render_template
import subprocess
import os

app = Flask(__name__)

# Route to run YOLOv8 obstacle detection
@app.route('/run-yolov8')
def run_yolov8():
    try:
        subprocess.Popen(['python', 'detect.py', '--weights', r'C:\Users\mehaj\OneDrive\Desktop\best.pt', '--source', '0'])
        return "YOLOv8 model started using laptop webcam!"
    except Exception as e:
        return str(e), 500

# Route to run path optimization
@app.route('/run-path-optimization')
def run_path_optimization():
    try:
        subprocess.run(['python', r'C:\Users\mehaj\OneDrive\Desktop\nsdbhvhgb\path_optimization.py'], check=True)
        return render_template('display.html', image='output.png')
    except Exception as e:
        return str(e), 500

# Route to display health monitoring (ECG from ESP32)
@app.route('/health-monitoring')
def health_monitoring():
    try:
        # You can replace 'ecg_data.txt' with real-time data streaming from ESP32
        with open('ecg_data.txt', 'r') as file:
            ecg_data = file.read()
        return render_template('health.html', ecg_data=ecg_data)
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)
