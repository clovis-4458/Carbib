from django.db import models
from datetime import date


class Countries(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Jobs(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('closed', 'Closed'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(default="No description provided.")
    location = models.CharField(max_length=100, default="Not specified")
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date_posted = models.DateField(auto_now_add=True)
    closing_date = models.DateField()
    responsibilities = models.TextField(default="Not specified")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} at {self.location}"


class Agents(models.Model):
    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    photo = models.ImageField(upload_to='agents_photos/')

    def __str__(self):
        return self.full_name


class Candidates(models.Model):

    # Candidate Status
    CANDIDATE_STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Approved", "Approved"),
        ("Travelled", "Travelled"),
    ]
    candidate_status = models.CharField(
        max_length=20, choices=CANDIDATE_STATUS_CHOICES, default="Pending"
    )

    # Personal Info
    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    religion = models.CharField(max_length=100)
    marital_status = models.CharField(max_length=20)
    no_of_children = models.PositiveIntegerField(default=0)
    tribe = models.CharField(max_length=100)
    clan = models.CharField(max_length=100)
    nin_number = models.CharField(max_length=20)
    passport_number = models.CharField(max_length=20, blank=True, null=True)
    working_experience = models.TextField(blank=True)
    country_worked = models.CharField(max_length=100, blank=True, null=True)

    # Place of Origin
    place_of_origin_village = models.CharField(max_length=100, blank=True, null=True)
    place_of_origin_parish = models.CharField(max_length=100, blank=True, null=True)
    place_of_origin_subcounty = models.CharField(max_length=100, blank=True, null=True)
    place_of_origin_county = models.CharField(max_length=100, blank=True, null=True)
    place_of_origin_district = models.CharField(max_length=100, blank=True, null=True)

    # Present Address
    present_address_village = models.CharField(max_length=100, blank=True, null=True)
    present_address_parish = models.CharField(max_length=100, blank=True, null=True)
    present_address_subcounty = models.CharField(max_length=100, blank=True, null=True)
    present_address_county = models.CharField(max_length=100, blank=True, null=True)
    present_address_district = models.CharField(max_length=100, blank=True, null=True)

    # Father Info
    father_name = models.CharField(max_length=100, blank=True, null=True)
    father_dob = models.DateField(blank=True, null=True)
    father_tel = models.CharField(max_length=20, blank=True, null=True)
    father_nin = models.CharField(max_length=20, blank=True, null=True)
    father_district = models.CharField(max_length=100, blank=True, null=True)
    father_tribe = models.CharField(max_length=100, blank=True, null=True)
    father_status = models.CharField(max_length=20, blank=True, null=True)

    # Mother Info
    mother_name = models.CharField(max_length=100, blank=True, null=True)
    mother_dob = models.DateField(blank=True, null=True)
    mother_tel = models.CharField(max_length=20, blank=True, null=True)
    mother_nin = models.CharField(max_length=20, blank=True, null=True)
    mother_district = models.CharField(max_length=100, blank=True, null=True)
    mother_tribe = models.CharField(max_length=100, blank=True, null=True)
    mother_status = models.CharField(max_length=20, blank=True, null=True)

    # Next of Kin
    next_of_kin_name = models.CharField(max_length=100)
    next_of_kin_relationship = models.CharField(max_length=100)
    next_of_kin_contact = models.CharField(max_length=20)
    next_of_kin_address = models.CharField(max_length=200)

    # Education
    education_level = models.CharField(max_length=200, blank=True, null=True)

    # Job Info
    job_applied = models.ForeignKey(Jobs, on_delete=models.SET_NULL, null=True, blank=True)
    job_location = models.ForeignKey(Countries, on_delete=models.SET_NULL, null=True, blank=True)
    referral_info = models.ForeignKey(Agents, on_delete=models.SET_NULL, null=True, blank=True)

    # CV & Documents
    cv = models.FileField(upload_to='cvs/', blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    passport_copy = models.ImageField(upload_to='passport_copies/', blank=True, null=True)
    full_photo = models.ImageField(upload_to='full_photos/', blank=True, null=True)
    medical_copy = models.ImageField(upload_to='medical_copies/', blank=True, null=True)
    interpol = models.ImageField(upload_to='interpol/', blank=True, null=True)

    # Automatic Age Calculation
    @property
    def age(self):
        """Automatically calculate age from date_of_birth."""
        if not self.date_of_birth:
            return None

        today = date.today()
        return (
            today.year
            - self.date_of_birth.year
            - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        )

    def __str__(self):
        job_title = self.job_applied.title if self.job_applied else "No Job"
        return f"{self.full_name} - {job_title}"
