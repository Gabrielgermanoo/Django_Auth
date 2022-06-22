from import_export import resources
from comp.models import Users

class MemberResource(resources.ModelResources):
    class Meta:
        model = Users