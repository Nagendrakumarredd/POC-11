from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Voting App v2 deployed via GitOps!"

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)
import os

if __name__ == "__main__":
    # OpenShift passes the target port in an environment variable named PORT
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

