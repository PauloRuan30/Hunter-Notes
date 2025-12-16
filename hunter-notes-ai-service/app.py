from flask import Flask, request, jsonify
from PIL import Image
import io
import os

app = Flask(__name__)

@app.route('/identify-monster', methods=['POST'])
def identify_monster():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected image file'}), 400

    try:
        # Read the image file
        image_data = file.read()
        image = Image.open(io.BytesIO(image_data))

        # --- Agno/Image Recognition Integration Placeholder ---
        # In a real scenario, you would pass 'image' to your Agno model
        # For example:
        # recognized_monster = agno_model.predict(image)
        # For now, return a dummy based on some simple logic or a fixed value
        
        # This is a very basic placeholder for demonstration.
        # In a real Agno integration, the model would process the image
        # and return the identified monster.
        print(f"Received image with format: {image.format}, size: {image.size}")
        
        dummy_monster_name = "Great Jagras" 
        # Example of how to simulate different results:
        # if "rathalos" in file.filename.lower():
        #     dummy_monster_name = "Rathalos"
        # elif "diablos" in file.filename.lower():
        #     dummy_monster_name = "Diablos"

        return jsonify({'monster_name': dummy_monster_name}), 200
    except Exception as e:
        app.logger.error(f"Error processing image: {e}")
        return jsonify({'error': f"Failed to process image: {str(e)}"}), 500

if __name__ == '__main__':
    # Using a different port to avoid conflict with Go backend
    port = int(os.environ.get('PORT', 5001)) 
    app.run(debug=True, host='0.0.0.0', port=port)
