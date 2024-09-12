from App.models import *
from rest_framework import serializers
from django.contrib.auth.models import User
from App.models import *


# from rest_framework.validators import UniqueValidator
# from rest_framework_jwt.settings import api_settings



class OTPSerializer(serializers.Serializer):
    email = serializers.EmailField()

class VerifyOTPSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)
    new_password = serializers.CharField(max_length=128)

    def validate(self, data):
        try:
            user = MyUser.objects.get(email=data['email'])
        except MyUser.DoesNotExist:
            raise serializers.ValidationError("Mtumiaji mwenye email hii teyari yupo.")

        otp_instance = OTP.objects.filter(user=user, otp=data['otp']).last()
        if not otp_instance or not otp_instance.is_valid():
            raise serializers.ValidationError("OTP sio sahihi au imeshaisha muda wake.")
        return data

    def save(self):
        user = MyUser.objects.get(email=self.validated_data['email'])
        user.set_password(self.validated_data['new_password'])
        user.save()
        OTP.objects.filter(user=user).delete()
        return user

        

#______________DJANGO REACT AUTHENTICATION_________________

class MikoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mikoa
        fields = '__all__'

class LevelZaWafugajiSerializer(serializers.ModelSerializer):
    class Meta:
        model = LevelZaWafugaji
        fields = '__all__'


class UserStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStatus
        fields = '__all__'

class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = '__all__'

class AinaZaKukuSerializer(serializers.ModelSerializer):
    class Meta:
        model = AinaZaKuku
        fields = '__all__'

class AinaZaNdegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AinaZaNdege
        fields = '__all__'

class MyUserSerializer(serializers.ModelSerializer):
    Mkoa = MikoaSerializer(many=False)
    Role = UserRoleSerializer(many=False)
    Level = LevelZaWafugajiSerializer(many=False)
    # Status = UserStatusSerializer(many=False)
    AinaYaKuku = AinaZaKukuSerializer(many=False)
    class Meta:
        model = MyUser
        fields = '__all__'










class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('username', 'email','phone', 'password')




class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = (
            'username', 
            'email', 
            'phone',
            'company_name',
            'Mkoa',
            'AinaYaKuku',
            'profile_image',
            'Maelezo',
            'Role',
            'Location'
        )



#______________MWISHO HAPA DJANGO REACT AUTHENTICATION_________________





class UserDataSerializer(serializers.ModelSerializer):
    Mkoa = MikoaSerializer(many=False)
    Role = UserRoleSerializer(many=False)
    Level = LevelZaWafugajiSerializer(many=False)
    # Status = UserStatusSerializer(many=False)
    AinaYaKuku = AinaZaKukuSerializer(many=False)
    class Meta:
        model = MyUser
        fields = '__all__'
        # fields = ['id', 'username', 'email','phone','first_name','profile_image']












# kwa ajili ya kumregister mtu bila kutumia token
class UserCreationSerializer(serializers.ModelSerializer):
	username=serializers.CharField(max_length=25)
	email=serializers.EmailField(max_length=50)
	password=serializers.CharField(max_length=50)


	class Meta:
		model= MyUser
		fields= ['username','email','password']
		#fields='__all__'

	def validate(self,attrs):
		username_exists = MyUser.objects.filter(username=attrs['username']).exists()
		if username_exists:
			raise serializers.ValidationError(detail="User with username already exists")


		email_exists = MyUser.objects.filter(email=attrs['email']).exists()
		if email_exists:
			raise serializers.ValidationError(detail="User with email already exists")

		return super().validate(attrs)






class HudumaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Huduma
        fields = '__all__'

class MgawanjoWaHudumaSerializer(serializers.ModelSerializer):
    Category = HudumaSerializer(many=False)
    class Meta:
        model = MgawanjoWaHuduma
        fields = '__all__'

class IdadiYaKukuSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdadiYaKuku
        fields = '__all__'

        
class UmriWaKukuSerializer(serializers.ModelSerializer):
    class Meta:
        model = UmriWaKuku
        fields = '__all__'




class UnitZaVyakulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitZaVyakula
        fields = '__all__'       

class MakundiYaVyakulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MakundiYaVyakula
        fields = '__all__' 

class VipindiVyaKukuSerializer(serializers.ModelSerializer):
    class Meta:
        model = VipindiVyaKuku
        fields = '__all__' 

class SikuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Siku
        fields = '__all__' 


class VyakulaSerializer(serializers.ModelSerializer):
    Unit = UnitZaVyakulaSerializer(many=False)
    FoodGroup = MakundiYaVyakulaSerializer(many=False)
    class Meta:
        model = Vyakula
        fields = '__all__'


class TaarifaZaKukuSerializer(serializers.ModelSerializer):
    AinaYaKuku = AinaZaKukuSerializer(many=False)
    #UmriKwaWiki = UmriWaKukuSerializer(many=False)
    #Kipindi = VipindiVyaKukuSerializer(many=False)
    class Meta:
        model = TaarifaZaKuku
        fields = '__all__'







class MaktabaYaLisheCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaktabaYaLisheCategories
        fields = '__all__'

class MaktabaYaLisheContentsSerializer(serializers.ModelSerializer):  
    CategoryName = MaktabaYaLisheCategoriesSerializer(many=False)
    class Meta:
        model = MaktabaYaLisheContents
        fields = '__all__'



class MuongozoWaLisheSerializer(serializers.ModelSerializer):
    class Meta:
        model = MuongozoWaLishe
        fields = '__all__'


class MatumiziSahihiYaIndibataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatumiziSahihiYaIndibata
        fields = '__all__'


class JamiiYaMfugajiCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = JamiiYaMfugajiCategories
        fields = '__all__'

class JamiiYaMfugajiContentsSerializer(serializers.ModelSerializer):
    CategoryName = JamiiYaMfugajiCategoriesSerializer(many=False)
    class Meta:
        model = JamiiYaMfugajiContents
        fields = '__all__'







#--------------------CART AND CART ITEMS--------------------
class VyakulaCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = VyakulaCart
        fields = '__all__'


class VyakulaCartItemsSerializer(serializers.ModelSerializer):
    cart = VyakulaCartSerializer()
    product = VyakulaSerializer()

    #table = VyakulaTablesSerializer()
    class Meta:
        model = VyakulaCartItems
        fields = '__all__'



class VyakulaOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = VyakulaOrder
        fields = '__all__'


class VyakulaOrderItemsSerializer(serializers.ModelSerializer):
    order = VyakulaOrderSerializer()
    product = VyakulaSerializer()

    # table = VyakulaTablesSerializer()
    # Customer = VyakulaCustomersSerializer()
    class Meta:
        model = VyakulaOrderItems
        fields = '__all__'





class MudaWaKumbushoUsafishajiBandaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MudaWaKumbushoUsafishajiBanda
        fields = '__all__' 


class KumbushoUsafishajiBandaSerializer(serializers.ModelSerializer):  
    #Muda = MudaWaKumbushoUsafishajiBandaSerializer(many=False)
    class Meta:
        model = KumbushoUsafishajiBanda
        fields = '__all__'

class GetKumbushoUsafishajiBandaSerializer(serializers.ModelSerializer):  
    Muda = MudaWaKumbushoUsafishajiBandaSerializer(many=False)
    class Meta:
        model = KumbushoUsafishajiBanda
        fields = '__all__'



#------------------KUMBUSHO LA CHANJO--------------------

class AinaZaChanjoSerializer(serializers.ModelSerializer):  
    #Muda = MudaWaAinaZaChanjoSerializer(many=False)
    class Meta:
        model = AinaZaChanjo
        fields = '__all__'


class KumbushoLaChanjoSerializer(serializers.ModelSerializer):  
    #Muda = MudaWaKumbushoLaChanjoSerializer(many=False)
    AinaYaChanjo = serializers.PrimaryKeyRelatedField(
        queryset=AinaZaChanjo.objects.all(), many=True

    ) 
    class Meta:
        model = KumbushoLaChanjo
        fields = '__all__'


class GetKumbushoLaChanjoSerializer(serializers.ModelSerializer):  
    AinaYaKuku = AinaZaKukuSerializer(many=False)
    #UmriWaKuku = UmriWaKukuSerializer(many=False)
    AinaYaChanjo = AinaZaChanjoSerializer(many=True)
    class Meta:
        model = KumbushoLaChanjo
        fields = '__all__'





#----------------KUMBUSHO LA UATAMIAJI WA MAYAI-------------

class KumbushoLaUatamiajiWaMayaiSerializer(serializers.ModelSerializer):  
    #Muda = MudaWaKumbushoLaUatamiajiWaMayaiSerializer(many=False)
    # AinaYaChanjo = serializers.PrimaryKeyRelatedField(
    #     queryset=AinaZaChanjo.objects.all(), many=True

    # ) 
    class Meta:
        model = KumbushoLaUatamiajiWaMayai
        fields = '__all__'

class GetKumbushoLaUatamiajiWaMayaiSerializer(serializers.ModelSerializer):  
    #AinaYaNdege = AinaZaNdegeSerializer(many=False)
    class Meta:
        model = KumbushoLaUatamiajiWaMayai
        fields = '__all__'








#-----------KUMBUSHO LA MABADILIKO YA LISHE------------
class KumbushoLaMabadilikoYaLisheSerializer(serializers.ModelSerializer):  
    #Muda = MudaWaKumbushoLaMabadilikoYaLisheSerializer(many=False)
    class Meta:
        model = KumbushoLaMabadilikoYaLishe
        fields = '__all__'

class GetKumbushoLaMabadilikoYaLisheSerializer(serializers.ModelSerializer):  
    #Muda = MudaWaKumbushoLaMabadilikoYaLisheSerializer(many=False)
    class Meta:
        model = KumbushoLaMabadilikoYaLishe
        fields = '__all__'


class IdadiYaKilosSerializer(serializers.ModelSerializer):  
    
    class Meta:
        model = IdadiYaKilos
        fields = '__all__'



class DukaLakoSerializer(serializers.ModelSerializer):  
    
    class Meta:
        model = DukaLako
        fields = '__all__'

class GetDukaLakoSerializer(serializers.ModelSerializer):  
    Status = UserStatusSerializer(many=False)
    class Meta:
        model = DukaLako
        fields = '__all__'






class MaoniSerializer(serializers.ModelSerializer):  
    
    class Meta:
        model = Maoni
        fields = '__all__'








class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'