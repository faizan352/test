from django import forms


class TaskDetailsForm(forms.Form):
    name = forms.CharField(min_length=4, max_length=30)
    type = forms.CharField(min_length=4, max_length=30)
    due_date = forms.DateTimeField()
    description = forms.CharField(min_length=4, max_length=30)
    status = forms.CharField(min_length=4, max_length=30)
    priority = forms.Textarea()
    assign_to = forms.CharField(min_length=4, max_length=30)
    created_by = forms.CharField(min_length=4, max_length=30)

