from django import forms
from .models import Job, Category, JobType

class JobForm(forms.ModelForm):
    IS_FEATURED_CHOICES = (
        (True, 'Yes'),
        (False, 'No'),
    )

    is_featured = forms.ChoiceField(
        choices=IS_FEATURED_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Is Featured"
    )

    job_type = forms.ModelChoiceField(
        queryset=JobType.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Select Job Type"
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Select Category"
    )
    class Meta:
        model = Job
        fields = ['job_title','job_slug','job_type', 'category', 'application_deadline', 'salary', 'job_description', 'job_requirements', 'company_name', 'company_location', 'company_website', 'is_featured', 'job_post_date']
        widgets = {
            'application_deadline': forms.DateInput(attrs={'type': 'date'}),
            'job_post_date': forms.DateInput(attrs={'type': 'date'}),
            'is_featured': forms.CheckboxInput(),
        }
    def __init__(self, *args, **kwargs):
        super(JobForm, self).__init__(*args, **kwargs)
        self.fields['application_deadline'].widget.attrs.update({
        'placeholder': 'Enter Application Deadline',
        'type': 'date'
                })
        self.fields['job_post_date'].widget.attrs.update({
        'placeholder': 'Enter Job Post Date',
        'type': 'date'
                })
        self.fields['job_title'].widget.attrs['placeholder'] = 'Enter Job Title'
        self.fields['job_slug'].widget.attrs['placeholder'] = 'Enter Job slug'
        self.fields['salary'].widget.attrs['placeholder'] = 'Enter Salary'
        self.fields['job_description'].widget.attrs['placeholder'] = ''
        self.fields['job_requirements'].widget.attrs['placeholder'] = ''
        self.fields['company_name'].widget.attrs['placeholder'] = 'Enter Company Name'
        self.fields['company_location'].widget.attrs['placeholder'] = 'Enter Company Location'
        self.fields['company_website'].widget.attrs['placeholder'] = 'www.xyz pvt.Ltd'
        self.fields['is_featured'].widget.attrs['placeholder'] = ''
        self.fields['job_post_date'].widget.attrs['placeholder'] = ''
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'