from rest_framework import serializers
from marketplace.models import Transcation
'''
class UserLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLog
        fields = ['fulname',]
'''
class products_boughtSerializer(serializers.ModelSerializer):
    #userlogid = UserLogSerializer()
    class Meta:
        model = Transcation
        fields = ('name','product_title','product_type','cost','date_backed') #email, phoneno
        #read_only_fields = ('force',)
