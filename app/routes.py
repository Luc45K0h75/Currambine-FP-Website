from flask import Blueprint, render_template

main = Blueprint('main', __name__)

# SEO metadata for each route — passed to templates for dynamic <title> and <meta description>
SEO = {
    'index': {
        'title': 'Currambine Family Practice | GP, Dental & Specialist Care in Perth',
        'description': 'Currambine Family Practice offers comprehensive GP, dental, psychology and specialist services in Currambine, WA. Book an appointment today.'
    },
    'about': {
        'title': 'About Us | Currambine Family Practice',
        'description': 'Meet the team at Currambine Family Practice. Our experienced doctors and specialists are committed to providing quality healthcare in Currambine, WA.'
    },
    'services': {
        'title': 'Our Services | Currambine Family Practice',
        'description': 'Explore the full range of medical services offered at Currambine Family Practice, including general practice, dental, psychology, physiotherapy and more.'
    },
    'contact': {
        'title': 'Contact Us | Currambine Family Practice',
        'description': 'Get in touch with Currambine Family Practice. Find our address, phone number and opening hours, or send us a message online.'
    },
    'fees': {
        'title': 'Fees & Billing | Currambine Family Practice',
        'description': 'Information on consultation fees, bulk billing eligibility and payment options at Currambine Family Practice.'
    },
    'faq': {
        'title': 'FAQ | Currambine Family Practice',
        'description': 'Answers to frequently asked questions about appointments, referrals, prescriptions and services at Currambine Family Practice.'
    },
    'appointments': {
        'title': 'Book an Appointment | Currambine Family Practice',
        'description': 'Book an appointment online with a GP or specialist at Currambine Family Practice in Currambine, WA.'
    },
}


@main.route('/')
def index():
    return render_template('index.html', seo=SEO['index'])


@main.route('/about')
def about():
    return render_template('about.html', seo=SEO['about'])


@main.route('/services')
def services():
    return render_template('services.html', seo=SEO['services'])


@main.route('/contact')
def contact():
    return render_template('contact.html', seo=SEO['contact'])


@main.route('/fees')
def fees():
    return render_template('fees.html', seo=SEO['fees'])


@main.route('/faq')
def faq():
    return render_template('faq.html', seo=SEO['faq'])


@main.route('/appointments')
def appointments():
    return render_template('appointments.html', seo=SEO['appointments'])