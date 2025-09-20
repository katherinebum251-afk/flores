# app.py
.actions{padding:18px;border-top:1px solid #faf0c9;background:#fffef7;display:flex;gap:10px;align-items:center}
.btn{padding:10px 12px;border-radius:10px;border:0;background:#f6c84c;font-weight:700}
</style>
</head>
<body>
<div class="wrapper">
<div class="hero">
<div class="svgbox">
<svg viewBox="0 0 300 200" xmlns="http://www.w3.org/2000/svg">
<rect width="300" height="200" rx="20" fill="#fffef7"/>
<g transform="translate(60,100)">
<circle r="20" fill="#6b4f1d"/>
<g fill="#f6c84c">
<ellipse rx="10" ry="30" transform="rotate(0)"/>
<ellipse rx="10" ry="30" transform="rotate(45)"/>
<ellipse rx="10" ry="30" transform="rotate(90)"/>
<ellipse rx="10" ry="30" transform="rotate(135)"/>
</g>
</g>
<g transform="translate(110,80) scale(0.8)">
<circle r="20" fill="#6b4f1d"/>
<g fill="#f6c84c">
<ellipse rx="10" ry="30" transform="rotate(0)"/>
<ellipse rx="10" ry="30" transform="rotate(45)"/>
<ellipse rx="10" ry="30" transform="rotate(90)"/>
<ellipse rx="10" ry="30" transform="rotate(135)"/>
</g>
</g>
<g transform="translate(200,100)">
<circle r="15" fill="#fff" stroke="#ccc" stroke-width="1"/>
<circle r="10" fill="#fafafa"/>
<circle r="5" fill="#f0f0f0"/>
</g>
<g transform="translate(240,80) scale(1.2)">
<circle r="15" fill="#fff" stroke="#ccc" stroke-width="1"/>
<circle r="10" fill="#fafafa"/>
<circle r="5" fill="#f0f0f0"/>
</g>
</svg>
</div>
<div class="text">
<h2>Para Marguii</h2>
<p>{{ message }}</p>
<div class="from">De: {{ sender }}</div>
</div>
</div>
<div class="actions">
<button class="btn" onclick="navigator.clipboard && navigator.clipboard.writeText(location.href).then(()=>alert('Enlace copiado!'))">Copiar enlace</button>
</div>
</div>
</body>
</html>
'''


@app.route('/')
def index():
default_message = 'Hola Marguii, este ramo de flores amarillas, girasoles y rosas blancas es para iluminar tu día.\n\nCon cariño.'
return render_template_string(BASE_HTML, default_message=default_message, preview_message=default_message, preview_style='amistoso')


@app.route('/send', methods=['POST'])
def send_card():
sender = request.form.get('sender', '').strip() or 'Alguien especial'
message = request.form.get('message', '').strip()
style = request.form.get('style', 'amistoso')
if not message:
return redirect(url_for('index'))
card_id = str(uuid.uuid4())[:8]
cards[card_id] = {'sender':sender, 'message':message, 'style':style}
return redirect(url_for('show_card', card_id=card_id))


@app.route('/card/<card_id>')
def show_card(card_id):
data = cards.get(card_id)
if not data:
abort(404)
return render_template_string(CARD_HTML, sender=data['sender'], message=data['message'])


if __name__ == '__main__':
app.run(host='0.0.0.0', port=5000, debug=True)