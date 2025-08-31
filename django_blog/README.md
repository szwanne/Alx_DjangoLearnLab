Authentication Flow:

Registration

Users fill out username, email, password1, and password2.

Django validates password strength and matching.

On success, user is logged in automatically.

Login

Users enter username and password.

If valid, they are redirected to their profile.

Logout

Users click logout link → session is cleared.

Profile Management

Authenticated users can update username and email.

Forms validated and updated via POST request.

## Post CRUD features

- URLs:

  - List: /posts/ (GET) - shows all posts
  - Create: /posts/new/ (GET, POST) - authenticated users only
  - Detail: /posts/<pk>/ (GET) - public
  - Edit: /posts/<pk>/edit/ (GET, POST) - only post author
  - Delete: /posts/<pk>/delete/ (POST) - only post author

- Forms:

  - Uses PostForm (ModelForm) with 'title' and 'content'.
  - Author is set from request.user in the CreateView's form_valid().

- Permissions:

  - LoginRequiredMixin prevents anonymous creation.
  - UserPassesTestMixin on Update/Delete ensures only the author can change/remove a post.

- Templates:

  - `post_list.html`, `post_detail.html`, `post_form.html`, `post_confirm_delete.html` in blog/templates/blog/.

- Commands:
  - `python manage.py makemigrations` / `migrate`
  - `python manage.py runserver`
