from rest_framework.schemas import AutoSchema
import coreapi
import coreschema


class ProduceListSchema(AutoSchema):

    def get_serializer_fields(self, path, method):
        return [
            coreapi.Field(
                name='filter',
                location='form',
                required=False,
                schema=coreschema.Integer(description='Параметр фильтрации')
            ),
        ]


class ProduceOrderSchema(AutoSchema):

    def get_serializer_fields(self, path, method):
        return [
            coreapi.Field(
                name='id',
                location='form',
                required=False,
                schema=coreschema.Integer(description='Параметр фильтрации')
            ),
            coreapi.Field(
                name='quantity',
                location='form',
                required=False,
                schema=coreschema.Integer(description='Количество')
            ),
        ]


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


class PaySchema(AutoSchema):
    def get_serializer_fields(self, path, method):
        return [
            coreapi.Field(
                name='id',
                location='form',
                required=True,
                schema=coreschema.String(description='id заказа')
            ),
            coreapi.Field(
                name='phone',
                location='form',
                required=True,
                schema=coreschema.String(description='Контактный телефон')
            )
        ]


class ServicesAddOrderSchema(AutoSchema):
    def get_serializer_fields(self, path, method):
        return [
            coreapi.Field(
                name='id',
                location='form',
                required=True,
                schema=coreschema.String(description='id услуги')
            ),
        ]

class PayServicesSchema(AutoSchema):
    def get_serializer_fields(self, path, method):
        return [
            coreapi.Field(
                name='id',
                location='form',
                required=True,
                schema=coreschema.String(description='id заказа')
            ),
            coreapi.Field(
                name='time_start',
                location='form',
                required=True,
                schema=coreschema.String(description='Желаемое время с')
            ),
            coreapi.Field(
                name='time_end',
                location='form',
                required=True,
                schema=coreschema.String(description='Желаемое время по')
            ),
            coreapi.Field(
                name='date',
                location='form',
                required=True,
                schema=coreschema.String(description='Дата')
            )
        ]