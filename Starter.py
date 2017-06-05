import subprocess, time

subprocess.Popen(['python3','Broker.py'])
subprocess.Popen(['python3','Ring.py'])
time.sleep(0.5)
subprocess.Popen(['python3','Subscriber.py'])
