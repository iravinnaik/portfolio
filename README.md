# Portfolio Website with Wagtail CMS

## Overview

This repository contains the code for my personal portfolio website built using Wagtail CMS. Wagtail is a powerful and flexible open-source content management system based on Django, which allows for easy content management and customization.

## Features

- **Dynamic Content Management**: Wagtail provides a user-friendly interface for managing website content, including pages, images, and documents.
- **Customizable Templates**: The website's templates are fully customizable, allowing for a unique and personalized design.
- **Responsive Design**: The website is designed to be fully responsive, ensuring a seamless experience across different devices and screen sizes.
- **SEO-Friendly**: Wagtail includes built-in features for optimizing the website for search engines, such as customizable meta tags and sitemaps.
- **Integration with Django Ecosystem**: Being built on Django, Wagtail seamlessly integrates with other Django apps and libraries, allowing for additional functionality if needed.

## Installation

1. Clone this repository to your local machine:
git clone https://github.com/iravinnaik/portfolio.git

2. Create a virtual environment and activate it:
python3 -m venv venv
source venv/bin/activate

3. Install the dependencies:
pip install -r requirements.txt

4. Apply database migrations: python manage.py migrate

5. Create a superuser account:python manage.py createsuperuser

6. Start the development server: python manage.py runserver

7. Access the admin interface at `http://localhost:8000/admin/` and start adding content to your portfolio website!

## Customization

- **Templates**: Customize the HTML and CSS templates located in the `templates` directory to match your desired design.
- **Static Files**: Add any additional static files (e.g., images, CSS, JavaScript) to the `static` directory.
- **Settings**: Adjust the project settings in `settings.py` to configure various aspects of the website, such as database settings, security settings, and installed apps.
- **Models**: Define custom models in `models.py` to extend the functionality of your portfolio website.

## Deployment

When deploying your portfolio website to a production environment, make sure to:

- Set `DEBUG = False` in `settings.py` for security purposes.
- Configure a production-ready database (e.g., PostgreSQL).
- Collect static files using `python manage.py collectstatic`.
- Set up a web server (e.g., Nginx or Apache) to serve the application.
- Consider using a service like Heroku, AWS, or DigitalOcean for hosting.

## License

This project is licensed under the [MIT License](LICENSE).

