import coreapi
import coreschema
from rest_framework.schemas import AutoSchema


class DeleteSchema(AutoSchema):
    def get_serializer_fields(self, path, method):
        return [
            coreapi.Field(
                name='id',
                location='form',
                required=True,
                schema=coreschema.String(description='id удаляемого обьекта')
            )
        ]

class addDishOrderSchema(AutoSchema):
    def get_serializer_fields(self, path, method):
        return [
            coreapi.Field(
                name='dish',
                location='form',
                required=True,
                schema=coreschema.Integer(description='Id блюда')
            ),
        ]


class changeDishOrderSchema(AutoSchema):
    def get_serializer_fields(self, path, method):
        return [
            coreapi.Field(
                name='order_item',
                location='form',
                required=True,
                schema=coreschema.Integer(description='Id заказанного блюда')
            ),
            coreapi.Field(
                name='quantity',
                location='form',
                required=True,
                schema=coreschema.Integer(description='Количество')
            ),
        ]