from rest_framework import serializers

from store.models import Store, Location, Product
from store.serializers.location_serializers import LocationSerializer
from store.serializers.product_serializers import ProductSerializer


class StoreSerializer(serializers.ModelSerializer):
    location = LocationSerializer(many=True)
    product = ProductSerializer(many=True)

    def create(self, validated_data):
        if validated_data['level'] == 0 and validated_data['supplier']:
            raise serializers.ValidationError('Завод не может иметь поставщика')

        location_data = validated_data.pop('location')
        product_data = validated_data.pop('product')
        store = Store.objects.create(**validated_data)

        locations = []
        for data in location_data:
            location_object, _ = Location.objects.get_or_create(**data)
            locations.append(location_object)

        location = getattr(store, 'location')
        location.set(locations)

        products = []
        for data in product_data:
            product_object, _ = Product.objects.get_or_create(**data)
            products.append(product_object)

        product = getattr(store, 'product')
        product.set(products)

        return store

    def update(self, store, validated_data):
        if validated_data['level'] == 0 and validated_data['supplier']:
            raise serializers.ValidationError('Завод не может иметь поставщика')

        location_data = validated_data.pop('location')
        product_data = validated_data.pop('product')

        locations = []
        for data in location_data:
            location_object, _ = Location.objects.get_or_create(**data)
            locations.append(location_object)

        location = getattr(store, 'location')
        location.set(locations)

        products = []
        for data in product_data:
            product_object, _ = Product.objects.get_or_create(**data)
            products.append(product_object)

        product = getattr(store, 'product')
        product.set(products)

        return super().update(store, validated_data)

    class Meta:
        model = Store
        fields = '__all__'
        read_only_fields = ['created', 'debt']

