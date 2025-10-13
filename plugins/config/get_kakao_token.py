import requests
# client_id, authorize_code 노출 주의, 실제 값은 임시로만 넣고 Git에 올라가지 않도록 유의

client_id = "c7eb3bb85225a724e370d057caee5cd4"
redirect_uri = "https://example.com/oauth"
authorize_code = "AoM5GMmCsfmuFCnlBu-lnPObl9yW64fzySgjFCYMPIKvVnvLCOaOPQAAAAQKDQ1fAAABmdzKvQghI_W2iNNaeg"

token_url = "https://kauth.kakao.com/oauth/token"
data = {
    "grant_type" : "authorization_code",
    "client_id" : client_id,
    "redirect_uri" : redirect_uri,
    "code" : authorize_code
}

response = requests.post(token_url, data=data)
tokens = response.json()
print(tokens)