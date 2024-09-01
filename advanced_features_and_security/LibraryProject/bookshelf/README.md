# Django Access Control System Documentation

This Django application demonstrates the use of groups and permissions to restrict access to certain parts of the application. The setup involves defining custom permissions, creating user groups, enforcing permissions in views, and testing the implementation.

## 1. Custom Permissions in Models

In the `models.py` file, custom permissions were added to a model to control actions such as viewing, creating, editing, or deleting instances of that model. 

### Example:

```python
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomModel(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    class Meta:
        permissions = [
            ('can_view', 'Can view model'),
            ('can_create', 'Can create model'),
            ('can_edit', 'Can edit model'),
            ('can_delete', 'Can delete model'),
        ]
```

In this example, the `CustomModel` has four custom permissions: `can_view`, `can_create`, `can_edit`, and `can_delete`.

## 2. Groups and Permissions Setup

User groups were created and configured with the relevant permissions. This was done using Django's admin interface.

### Groups:
- **Admins**: Full access, including `can_view`, `can_create`, `can_edit`, and `can_delete`.
- **Editors**: Permissions to `can_edit` and `can_create`.
- **Viewers**: Only permission to `can_view`.

### Steps:
1. Navigate to Django's admin interface.
2. Create the groups: Admins, Editors, and Viewers.
3. Assign the relevant permissions to each group.

## 3. Enforcing Permissions in Views

Views were modified to check for these permissions before allowing users to perform certain actions. The `@permission_required` decorator was used for this purpose.

### Example:

```python
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from .models import CustomModel

@permission_required('app_name.can_edit', raise_exception=True)
def edit_model(request, pk):
    instance = get_object_or_404(CustomModel, pk=pk)
    # Logic to edit the model
    return render(request, 'app_name/edit_model.html', {'instance': instance})
```

In this example, the `edit_model` view is protected by the `can_edit` permission. Only users with this permission can access the view.

## 4. Testing Permissions

Permissions were tested manually by creating test users and assigning them to different groups.

### Testing Approach:
1. **Create Test Users**: Create several test users and assign them to the Admins, Editors, and Viewers groups.
2. **Log In and Test**: Log in as each user and attempt to access various views in the application to ensure the permissions are enforced correctly.

## 5. Summary of Configuration

This section provides a summary of how permissions and groups are set up and used in this application:

- **Permissions**: Defined in the `Meta` class of the model.
- **Groups**: Created and managed via Django's admin interface, with specific permissions assigned.
- **Views**: Protected using the `@permission_required` decorator to enforce the defined permissions.

