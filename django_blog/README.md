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
