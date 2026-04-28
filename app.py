from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///text_entries.db'
db = SQLAlchemy(app)

class TextEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/save', methods=['POST'])
def save_entry():
    content = request.json.get('content')
    new_entry = TextEntry(content=content)
    db.session.add(new_entry)
    db.session.commit()
    return jsonify({'message': 'Entry saved!', 'id': new_entry.id}), 201

@app.route('/api/entries', methods=['GET'])
def get_entries():
    entries = TextEntry.query.all()
    return jsonify([{'id': entry.id, 'content': entry.content, 'created_at': entry.created_at} for entry in entries])

@app.route('/api/delete/<int:id>', methods=['DELETE'])
def delete_entry(id):
    entry = TextEntry.query.get_or_404(id)
    db.session.delete(entry)
    db.session.commit()
    return jsonify({'message': 'Entry deleted!'}), 204

if __name__ == '__main__':
    app.run(debug=True)