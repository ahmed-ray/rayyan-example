app = Flask(__name__)

# Sample data (replace this with a database in a real-world scenario)
job_listings = [
    {"id": 1, "title": "Software Developer", "company": "Tech Co", "location": "City A"},
    {"id": 2, "title": "Data Scientist", "company": "Data Corp", "location": "City B"},
]

@app.route('/')
def index():
    return render_template('index.html', job_listings=job_listings)

@app.route('/post_job', methods=['GET', 'POST'])
def post_job():
    if request.method == 'POST':
        title = request.form['title']
        company = request.form['company']
        location = request.form['location']

        job_id = len(job_listings) + 1
        new_job = {"id": job_id, "title": title, "company": company, "location": location}
        job_listings.append(new_job)

        return redirect(url_for('index'))

    return render_template('post_job.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_query = request.form['search_query'].lower()
        results = [job for job in job_listings if search_query in job['title'].lower() or search_query in job['company'].lower()]

        return render_template('search_results.html', results=results, query=search_query)

    return render_template('search.html')

if __name__ == '__main__':
    app.run(debug=True)