1. The pre-login requests should have a verification of source as to from where the requests are coming from. Can use headers to identify.
2. The login and registration apis
3. Get user profile api
4. Create a database and users table to authenticate.
5. Should use at least one of the three JWT, Passport.js or Sanctum to generate session tokens.
6. CRUD operations on articles (Every user can create articles of a blog)
7. The articles apis should be authenticated and authorized as well except GET, which will be open for all.

Expected APIs
1.	 /api/v1/register
2.	 /api/v1/login
3.	 /api/v1/get-profile (requires auth)
4.	 CRUD apis for articles
