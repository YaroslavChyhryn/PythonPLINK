# Jun Python Test case - PLINK

### urls
1. not-admin/ - Admin
2. api/v1/ - Api Root
3. api/v1/register - accept json and if its valid create user
4. api/v1/token - if user authenticated return his token
5. api/v1/requests - return all registration requests from client ip
6. api/v1/note - all user notes
7. api/v1/note/[note_id] - read, update, delete specific note
8. api-auth/login/ - login
9. api-auth/logout/ - logout


### create user json example
```
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"email": "yaroslav@mail.com", "password": "A12345678", "first_name": "yaroslav", "last_name": "chyhryn"}' \
http://localhost:8000/api/v1/register
```

## Example of .env
```
DEBUG=**any or delete for DEBUG=False**
SECRET_KEY=**your secret key here**
```
## Example of request with token
```
curl -X GET http://127.0.0.1:8000/api/v1/note/  -H "Authorization: Token **token_value_here**"
```
