# 📝 My Blog - Django Application

A simple yet elegant blogging platform built with Django and Bootstrap 5.

## Features

✨ **Core Features**
- User Authentication (Register, Login, Logout)
- Create, Edit, Delete Blog Posts
- Responsive Design with Bootstrap 5
- Image Upload Support
- Author Attribution and Date Display
- Full Blog Post View with Details

🔐 **Security**
- Login Required for Creating/Editing Posts
- Permission-based Access Control
- CSRF Protection
- XSS Protection

📱 **Responsive UI**
- Mobile-friendly Navigation
- Bootstrap 5 Grid System
- Card-based Post Layout
- Professional Footer

## Tech Stack

- **Backend**: Django 5.0.4
- **Frontend**: Bootstrap 5, HTML5, CSS3
- **Database**: SQLite (Development) / PostgreSQL (Production)
- **Server**: Gunicorn + WhiteNoise
- **Deployment**: Render

## Installation

### Local Development

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/auth_blog.git
cd auth_blog
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Create .env file**
```bash
cp .env.example .env
```

5. **Run migrations**
```bash
python manage.py migrate
```

6. **Create superuser**
```bash
python manage.py createsuperuser
```

7. **Run development server**
```bash
python manage.py runserver
```

Visit `http://localhost:8000/` in your browser.

## Project Structure

```
auth_blog/
├── auth_blog/              # Project settings
│   ├── settings.py         # Django configuration
│   ├── urls.py             # URL routing
│   ├── wsgi.py             # WSGI configuration
│   └── asgi.py             # ASGI configuration
├── blog_app/               # Blog application
│   ├── models.py           # Post model
│   ├── views.py            # View functions
│   ├── forms.py            # Django forms
│   └── migrations/         # Database migrations
├── templates/              # HTML templates
│   ├── base.html           # Base template
│   ├── auth_app/           # App-specific templates
│   └── registration/       # Auth templates
├── media/                  # User uploads
├── manage.py               # Django CLI
├── requirements.txt        # Python dependencies
├── Procfile                # Render configuration
├── runtime.txt             # Python version
└── .env.example            # Environment variables template
```

## Available Pages

- **Home** (`/`) - Display all blog posts
- **Login** (`/accounts/login/`) - User login
- **Signup** (`/signup/`) - User registration
- **Create Post** (`/create/`) - Create new blog post (login required)
- **Post Detail** (`/post/<id>/`) - View full post
- **Edit Post** (`/post/<id>/edit/`) - Edit post (author only)
- **Delete Post** (`/post/<id>/delete/`) - Delete post (author only)

## Deployment on Render

### Step 1: Push to GitHub

```bash
git add .
git commit -m "Initial commit"
git push origin main
```

### Step 2: Create Render Account

1. Go to [render.com](https://render.com)
2. Sign up with GitHub
3. Create a new Web Service

### Step 3: Configure on Render

1. **Repository**: Select your GitHub repository
2. **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
3. **Start Command**: `gunicorn auth_blog.wsgi:application`
4. **Environment Variables**:
   - `SECRET_KEY`: Generate a new Django secret key
   - `DEBUG`: `False`
   - `ALLOWED_HOSTS`: `your-app-name.onrender.com`
   - `DATABASE_URL`: (optional, for PostgreSQL)

### Step 4: Deploy

1. Click "Deploy Web Service"
2. Wait for build to complete
3. Visit your live app URL

## Environment Variables

Required environment variables (see `.env.example`):

```
SECRET_KEY=your-django-secret-key
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1,your-domain.com
```

## Django Admin

Access the admin panel at `/admin/` with your superuser credentials.

## Future Features

📋 **Coming Soon**
- Comment Section
- Post Likes/Ratings
- Pagination
- Search Functionality
- Dark Mode Toggle
- Tag System
- Category System
- Email Notifications

## Troubleshooting

### Static Files Not Loading
```bash
python manage.py collectstatic --noinput
```

### Database Migration Issues
```bash
python manage.py makemigrations
python manage.py migrate
```

### Port Already in Use
```bash
python manage.py runserver 8001
```

## Security Tips for Production

- ✅ Always use environment variables for sensitive data
- ✅ Set `DEBUG=False` in production
- ✅ Use a strong `SECRET_KEY`
- ✅ Configure `ALLOWED_HOSTS` properly
- ✅ Use HTTPS only
- ✅ Enable CSRF protection
- ✅ Set secure cookie flags

## License

This project is open source and available under the MIT License.

## Support

For issues or questions, please open an issue on GitHub.

---

Built with ❤️ using Django & Bootstrap
