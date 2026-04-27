# 🗄️ Database Setup Guide - Render PostgreSQL Integration

Your current auth_blog uses SQLite, which doesn't persist on Render. Posts are lost after each deployment! This guide will set up a **permanent PostgreSQL database** on Render.

---

## Option 1: PostgreSQL on Render (Easiest - Recommended) ⭐

### Step 1: Create PostgreSQL Database on Render

1. Go to [render.com dashboard](https://dashboard.render.com)
2. Click **"New +"** → **"PostgreSQL"**
3. Fill in:
   - **Name**: `auth-blog-db` (or any name)
   - **Database**: `auth_blog_db` (this is auto-generated, keep it)
   - **User**: `auth_blog` (auto-generated)
   - **Region**: Same as your web service
   - **PostgreSQL Version**: 15 (or latest)
4. Click **"Create Database"**

Wait 2-3 minutes for database to be created.

### Step 2: Get Database Connection String

1. After creation, you'll see your database dashboard
2. Scroll down to find **"Internal Database URL"**
3. Copy the full URL (looks like: `postgresql://user:password@host:5432/dbname`)
4. **Save this URL** - you'll need it in the next step

### Step 3: Update Your Django Project

#### 3.1 Install PostgreSQL Driver & URL Parser

Update your `requirements.txt`:

```txt
Django==4.2.11
Pillow==11.0.0
gunicorn==21.2.0
whitenoise==6.6.0
psycopg2-binary==2.9.9
dj-database-url==2.1.0
python-decouple==3.8
```

Key packages:
- `psycopg2-binary`: PostgreSQL driver for Django
- `dj-database-url`: Parses DATABASE_URL automatically ✅

#### 3.2 Update `settings.py`

Find the database section and we've already updated it to use `DATABASE_URL`:

```python
import dj_database_url

if config('DATABASE_URL', default=None):
    DATABASES = {
        'default': dj_database_url.config(default=config('DATABASE_URL'), conn_max_age=600)
    }
else:
    # Fallback to SQLite for local development
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
```

This automatically parses the `DATABASE_URL` environment variable! ✅

#### 3.3 Update `build.sh`

Update your build script to handle the PostgreSQL connection:

```bash
#!/bin/bash

# Exit on any error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Run database migrations
python manage.py migrate

# Create superuser automatically if using environment variables
if [ -n "$DJANGO_SUPERUSER_PASSWORD" ]; then
    python manage.py createsuperuser --username admin --email admin@example.com --noinput || true
fi

echo "Build complete! ✅"
```

### Step 4: Add Environment Variables to Render (Super Simple!)

1. Go to your **auth-blog** web service on Render dashboard
2. Click **"Environment"** tab
3. Add **just these variables:**

| Variable | Value |
|----------|-------|
| `DATABASE_URL` | `postgresql://user:password@host:5432/dbname` |
| `SECRET_KEY` | (your secret key) |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `auth-blog.onrender.com` |
| `DJANGO_SUPERUSER_PASSWORD` | `YourSecurePassword123` |

**That's it!** 🎉

**Getting DATABASE_URL:**
- Open your PostgreSQL database details on Render
- Copy the **"Internal Database URL"** (it looks like: `postgresql://auth_blog:password123@dpg-xxx.render.internal:5432/auth_blog_db`)
- Paste it into the `DATABASE_URL` variable

### Step 5: Deploy with New Database

1. Push your changes to GitHub:
   ```bash
   git add requirements.txt auth_blog/settings.py build.sh
   git commit -m "Add PostgreSQL database integration"
   git push origin main
   ```

2. Go to Render dashboard
3. Your web service should auto-redeploy
4. Monitor the build logs

### Step 6: Verify Database Connection

After deployment completes:

1. Check the deployment logs for any database errors
2. Visit your admin page: `https://your-app.onrender.com/admin/`
3. Login and create a test post
4. Refresh your browser - the post should still be there! ✅

---

## Option 2: PostgreSQL with Render + Environment Variables (More Secure)

If Render provides `DATABASE_URL` automatically, update settings.py:

```python
import os
import dj_database_url

# Check if DATABASE_URL is provided (Render does this)
if os.getenv('DATABASE_URL'):
    DATABASES = {
        'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'), conn_max_age=600)
    }
else:
    # Fallback for local development
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
```

Install `dj-database-url`:
```
pip install dj-database-url==2.1.0
```

---

## Option 3: External PostgreSQL (Neon, AWS RDS, etc.)

If you want to use Neon instead:

1. Sign up at [neon.tech](https://neon.tech)
2. Create a free PostgreSQL project
3. Copy connection string
4. Add to Render environment variables
5. Follow the same steps as Option 1

---

## Troubleshooting

### Error: "psycopg2 module not found"
**Solution:** Make sure `psycopg2-binary==2.9.9` is in `requirements.txt` and run:
```bash
pip install -r requirements.txt
```

### Error: "could not connect to database"
**Solution:** 
- Verify credentials in environment variables
- Check that PostgreSQL database is running on Render
- Ensure web service and database are in same region

### Migration Errors
**Solution:** Run migrations manually:
```bash
# Locally
python manage.py migrate

# Or via Render shell (if available)
```

### Lost Posts After Deployment?
**Solution:** Posts in SQLite were never persisted. After switching to PostgreSQL, create new posts - they'll now be permanent! ✅

---

## Summary of Changes

| Item | Before | After |
|------|--------|-------|
| Database | SQLite (temporary) | PostgreSQL (persistent) ✅ |
| Config Method | 5 env variables | 1 `DATABASE_URL` ✅ |
| Posts Lost? | YES 😞 | NO ✅ |
| Data Persistence | Per deployment | Permanent |
| Setup Complexity | Complex | Simple ✅ |

---

## Next Steps

1. ✅ Create PostgreSQL database on Render
2. ✅ Update `requirements.txt` with psycopg2-binary
3. ✅ Update `settings.py` with PostgreSQL config
4. ✅ Add environment variables to Render
5. ✅ Push to GitHub
6. ✅ Monitor deployment
7. ✅ Test with new posts

Your posts are now safe! 🎉

---

**Questions?** Check Render's PostgreSQL docs: https://render.com/docs/databases
