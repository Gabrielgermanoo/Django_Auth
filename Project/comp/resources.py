from import_export import resources
from comp.models import Users

class UserResource(resources.ModelResource):
    class Meta:
        model = Users
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('id', 'login', 'password')

    def skip_row(self, instance, original):
        return super().skip_row(instance, original)
    