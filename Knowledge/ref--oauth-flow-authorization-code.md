---
category: knowledge
tags:
  - reference
platform: n/a
status: done
created: 2026-06-17
aliases:
  - Client Registration
---

# Client Registration

In order to use an OAuth API, we'll need to first register the application. Typically this involves setting up a developer account at the service, then answering some questions about your application, uploading a logo, etc.
## Step 1: Build the authorization URL and redirect the user to the authorization server
### 1. Build the Authorization URL
Before authorization begins, it first generates a random string to use for the `state` parameter. The client will need to store this to be used in the next step.
```lua
https://authorization-server.com/authorize?
  response_type=code
  &client_id=khjsE0m7g9WUMaTOSfKJD1DS
  &redirect_uri=https://www.oauth.com/playground/authorization-code.html
  &scope=photo+offline_access
  &state=54kJsn5RUkvzjZhT
```

For this demo, a random state parameter (shown above) is generated and saved it in a cookie.

Click "Authorize" below to be taken to the authorization server. You'll need to enter the username and password that was generated for you.

![[images/login_password_OAuth.png]]

## Step 2 : After the user is redirected back to the client, verify the state matches
### 2. Verify the state parameter

A button asking for approval appeared with the following link:
`https://www.oauth.com/playground/authorization-code.html?state=5ZtMskLxh7duF_iO&code=eZgeMH9Z-MmZWMZgvn5uNd7WfK5-bDVb4g3ty2cc2uPAqyYW`

Clicking the button, the user was redirected back to the client, and you'll notice a few additional query parameters in the URL:
`?state=5ZtMskLxh7duF_iO&code=FHF4RAeI3SSxCdPQ8-QojeRf4w7UHeurTBDKXoPEB3ZZZ00P`

You need to first verify that the `state` parameter matches the value stored in this user's session so that you protect against CSRF attacks.

Depending on how you've stored the `state` parameter (in a cookie, session, or some other way), verify that it matches the state that you originally included in step 1. Previously, we had stored the state in a cookie for this demo.

The state stored by the client (`5ZtMskLxh7duF_iO`) match the state in the redirect (`5ZtMskLxh7duF_iO`)?

## Step 3 : Exchange the authorization code for an access token
### 3. Exchange the Authorization Code

Now you're ready to exchange the authorization code for an access token.

The client builds a POST request to the token endpoint with the following parameters:
```lua
POST https://authorization-server.com/token

grant_type=authorization_code
&client_id=khjsE0m7g9WUMaTOSfKJD1DS
&client_secret=O21qZp4-8zyouRS_4WNPysgp1H-PaPVImPEBWT2ch58vzIFo
&redirect_uri=https://www.oauth.com/playground/authorization-code.html
&code=2JeXuRVjGT51gG5M2V2wgdEOpL4JaFXtwNfr6HuWqLSU3kpB
```

Note that the client's credentials are included in the POST body in this example. Other authorization servers may require that the credentials are sent as a HTTP Basic Authentication header.

#### Token Endpoint Response

Here's the response from the token endpoint! The response includes the access token and refresh token.
``` json
{
  "token_type": "Bearer",
  "expires_in": 86400,
  "access_token": "Q1BQEsJ2YhRuqNoXe9vxFLkCoH46xDPs2hKyUEX3P0Je62ZJNC1zCSnEmDCLLyDYwBbwVHT4",
  "scope": "photo offline_access",
  "refresh_token": "DpYe9OA17RdKkEf2nu_25wfT"
}
```

Great! Now your application has an access token, and can use it to make API requests on behalf of the user.
