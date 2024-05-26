from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(
        required = False,
        write_only = True,
    )
    
    email = serializers.EmailField(
        required=True,
        validators = [UniqueValidator(queryset=User.objects.all())]
        )
    
    class Meta:
        model = User
        exclude = [
            # "password",
            "last_login",
            "date_joined",
            "groups",
            "user_permissions",
        ]
        # fields = "__all__"
    
    def validate(self, attrs):
        if attrs.get('password', False):
            from django.contrib.auth.password_validation import validate_password # doğrulama fonksiyonu
            from django.contrib.auth.hashers import make_password # şifreleme fonksiyonu
            password = attrs['password'] # Password al.
            validate_password(password) # Validation'dan geçir.
            attrs.update(
                {
                    'password': make_password(password) # Password şifrele ve güncelle.
                }
            )
        return super().validate(attrs) # Orjinal methodu çalıştır.
    
# ------- TokenSerializer -------
# ---- Kullanıcı login olurken token key ile birlikte user datası da dönsün! ----
from dj_rest_auth.serializers import TokenSerializer

class UserTokenSerializer(TokenSerializer):
    
    user = UserSerializer()
    
    class Meta(TokenSerializer.Meta):
        fields = ('key', 'user')
        