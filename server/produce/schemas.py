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