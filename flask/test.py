import matplotlib.pyplot as plt
from flask import Flask, render_template, Response
import io

app = Flask(__name__)

@app.route('/')
def plot():
    # Generate your plot using Matplotlib
    x = [1, 2, 3, 4, 5]
    y = [10, 8, 6, 4, 2]
    plt.plot(x, y)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('My Plot')

    # Convert the plot to HTML image data
    img_data = io.BytesIO()
    plt.savefig(img_data, format='png')
    img_data.seek(0)

    # Return the plot as a Flask response with the appropriate content type
    return Response(img_data.getvalue(), mimetype='image/png')

if __name__ == '__main__':
    app.run()
