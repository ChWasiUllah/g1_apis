from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from djoser.serializers import UserSerializer as BaseUserSerializer
from core.models import User

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        model = User
        fields = ['id','email','password','first_name','last_name']
    

# class UserCreateSerializer(BaseUserCreateSerializer):
#     confirm_password = serializers.CharField(write_only=True,style={"input_type": "password"})  # This field is for confirm password input 
#     class Meta(BaseUserCreateSerializer.Meta):
#         model = User
#         fields = ['id','username','email','password','confirm_password','first_name','last_name']
#         extra_kwargs = {
#             'password': {'write_only': True},  # Make the password field write-only for security reasons
#         }

#     def validate(self, data):
#         password_pattern = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>])[A-Za-z\d!@#$%^&*(),.?":{}|<>]{8,}$'
#         email_pattern = r'^[a-zA-Z0-9_.+-]+@gmail\.com$'
#         email = data.get('email')
#         password = data.get('password')
#         confirm_password = data.get('confirm_password')
#         def Error(validation_type,message,example=None):
#             if example is None:
#                 return {
#                 f'{validation_type}-validation-error': {'Message':message,
#                 },    
#             }
#             return {
#                 f'{validation_type}-validation-error': {'Message':message,
#                 'Example':example},    
#             }
#         if not re.match(email_pattern,email):
#             raise serializers.ValidationError(Error('email',"Please enter the valid Email address",'example@gmail.com'))
        
#         if password != confirm_password:
#             raise serializers.ValidationError(Error("password","Password and Confirm Password should be same"))
#         elif len(password)<8:
#             raise serializers.ValidationError(Error('password','Passwords Length should be 8 or more'))
#         elif not re.match(password_pattern,password):
#             raise serializers.ValidationError(Error('password','Password must be mixture of Numbers,Letters and Special Characters','Use at least 1 Specail Character, Use Mixture of Numbers and Letters'))
        
#         return data

#     def create(self, validated_data):
#         user = User.objects.create(
#             username=validated_data['username'],
#             password=validated_data['password'],
#             email=validated_data['email'],
#             first_name=validated_data['first_name'],
#             last_name=validated_data['last_name']
#         )
#         user.set_password(validated_data['password'])
#         user.save()
#         return user
    
# For adding more fields to user/me end point
class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields= ['id','email','first_name','last_name']
        