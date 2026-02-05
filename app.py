from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Ganti dengan kunci rahasia yang aman

# Kriteria penilaian OSCE untuk pelepasan informasi
criteria = [
    "Pengenalan diri dan membangun rapport dengan pasien/keluarga",
    "Penjelasan diagnosis, kondisi kesehatan, dan alasan pelepasan",
    "Penjelasan rencana perawatan, obat-obatan, dan tindak lanjut",
    "Penanganan pertanyaan dan kekhawatiran pasien/keluarga",
    "Kesimpulan, penutupan, dan konfirmasi pemahaman"
]

@app.route('/')
def index():
    return render_template('index.html', criteria=criteria)

@app.route('/submit', methods=['POST'])
def submit():
    scores = []
    total = 0
    for i in range(len(criteria)):
        score = int(request.form.get(f'score_{i}', 0))
        scores.append(score)
        total += score
    
    # Simpan hasil dalam sesi
    session['scores'] = scores
    session['total'] = total
    session['criteria'] = criteria
    
    return redirect(url_for('result'))

@app.route('/result')
def result():
    scores = session.get('scores', [])
    total = session.get('total', 0)
    criteria = session.get('criteria', [])
    return render_template('result.html', criteria=criteria, scores=scores, total=total)

if __name__ == '__main__':
    app.run(debug=True)