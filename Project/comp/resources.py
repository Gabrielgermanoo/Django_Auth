from import_export import resources
from comp.models import Users

class MemberResource(resources.ModelResource):
    class Meta:
        model = Users
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('login',)
        exclude = ('id')
    