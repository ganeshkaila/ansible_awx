DATABASES = {
    'default': {
        'ATOMIC_REQUESTS': True,
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "awx",
        'USER': "awx",
        'PASSWORD': "awxpass",
        'HOST': "postgres",
        'PORT': "5432",
    }
}

BROADCAST_WEBSOCKET_SECRET = "NnVDVzpTSzA1UU15LV86eHhmRXMtOkIyUDdlLUJva3FvYjlnOmc6RnNfYXlLcXBGLjE2ZFF4c0lRendSandiVnpzbVBnVF92SUY6OnU2Q1ROM1hubGhaclgtN1JSOVgwdkRFWHRvTUpQY3c6OFNENERFa3Z0Qzdock1RVHgwcUM="
