from django import forms


branch_choices = (
        ('-','---SELECT---'),
        ('CSE','Computer Science & Engineering'),
        ('ECE','Electronics and Communication Engineering'),
        ('MECH','Mechanical Engineering'),
        ('MME','Metallurgy Engineering'),
        ('CHE','Chemical Engineering'),
        ('CIVIL','Civil Engineering'),
        ('EEE','Electrical and Electronics Engineering'),
        ('BIO','Biotechnology'),
    )

class AddCompaniesForm(forms.Form):

    name = forms.CharField(
        required = True,
        label = 'Name Of Company',
        max_length = 32,
        widget = forms.TextInput(
            attrs={
            "class": "form-control",
            }
        )
    )

    ctc = forms.CharField(
        required = True,
        label = 'CTC Offered',
        max_length = 32,
        widget = forms.TextInput(
            attrs={
            "class": "form-control",
            }
        )
    )

    cgpa = forms.DecimalField(
        required = True,
        label = 'CGPA cut-off',
        widget = forms.TextInput(
            attrs={
            "class": "form-control",
            }
        )
    )

    br_allowed = forms.CharField(
        required = True,
        label = 'Branches Allowed',
        max_length = 32,
        widget = forms.Select(
            choices = branch_choices,
            attrs={
            "class": "form-control",
            }
        )
    )
