from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from bunnies.models import Bunny, RabbitHole


class RabbitHoleSerializer(serializers.ModelSerializer):
    bunnies = serializers.PrimaryKeyRelatedField(many=True, queryset=Bunny.objects.all())
    bunny_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = RabbitHole
        fields = ('location', 'bunnies', 'bunny_count', 'latitude', 'longitude')
        read_only_fields = ('owner',)

    def create(self, validated_data):
        # Ignore incoming "owner" field and always populate with request.user
        validated_data["owner"] = self.context["request"].user
        return super().create(validated_data)


class BunnySerializer(serializers.ModelSerializer):
    home = serializers.SlugRelatedField(queryset=RabbitHole.objects.all(), slug_field='location')
    family_members = serializers.SerializerMethodField()

    def get_family_members(self, obj):
        return obj.home.bunnies.exclude(id=obj.id).values_list("name", flat=True)

    def validate_home(self, value):
        # Since the validation of bunnies limit is specific to the home of the new Rabbit object,
        # let's do field level validation
        if value.bunny_count == value.bunnies_limit:
            raise ValidationError("Bunny limit exceeded!")

    class Meta:
        model = Bunny
        fields = ('name', 'home', 'family_members')

