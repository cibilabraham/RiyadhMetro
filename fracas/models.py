from django.db import models
from django.forms import ModelForm, DateField, ChoiceField, CharField
from datetime import date
from fracas_site import settings
from django.contrib.admin.widgets import AdminDateWidget
import datetime
import uuid
from django.forms.models import ModelChoiceIterator, ModelMultipleChoiceField
from django.forms.widgets import MultipleHiddenInput
from django.contrib.postgres.fields import *

from django.contrib.auth.models import User,Group

# Create your models here.


class ModelArrowCharField(models.CharField):
    arrow = True
    
class CorrectiveAction(models.Model):
    defect = models.ForeignKey('Defect', on_delete=models.CASCADE)
    # root_cause = models.ForeignKey('RootCause', on_delete=models.CASCADE)
    corrective_action_id = models.AutoField(primary_key=True)
    corrective_action_owner = models.CharField(max_length=550, blank=True)
    corrective_action_description = models.TextField(blank=True)
    corrective_action_update = models.TextField(blank=True)
    corrective_action_status = models.CharField(max_length=550, blank=True)
    is_active = models.IntegerField(default=0)
    P_id = models.IntegerField(default=0)

class FailureMode(models.Model):
    mode_id = models.CharField(max_length=550, unique=True)
    mode_description = models.CharField(max_length=550, null=True, blank=True)
    asset_type = ArrayField(models.CharField(max_length=255, blank=True),default=list)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    P_id = models.IntegerField(default=0)
    is_active = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Failure Mode Identification'


    def __str__(self):
        return self.mode_id

failureTypeChoices = (
    ('software', 'Software'),
    ('hardware', 'Hardware'),
    ('random', 'Random')
)
saftyFailureChoices = (
    ('yes', 'Yes'),
    ('no', 'No')
)
class FailureData(models.Model):
    asset_type = models.CharField(max_length=550, blank=True)
    failure_id = models.CharField(max_length=600, null=True, blank=True)
    asset_config_id = models.ForeignKey('Asset', on_delete=models.CASCADE, to_field='asset_config_id', null=True, blank=True)
    event_description = models.CharField(max_length=600 , null=True)
    mode_id = models.ForeignKey('FailureMode', on_delete=models.SET_NULL, null=True, blank=True)
    mode_description = models.CharField(max_length=600, null=True, blank=True)
    date = models.DateField(null=True)
    time = models.TimeField(max_length=15, null=True)
    detection = models.CharField(max_length=600 , null=True)
    service_delay = models.CharField(max_length=600, null=True, blank=True)
    immediate_investigation = models.TextField(null=True, blank=True)
    failure_type = models.CharField(max_length=600  , default='safety', choices=failureTypeChoices)
    safety_failure = models.CharField(max_length=550, default='yes', choices=saftyFailureChoices)
    hazard_id = models.CharField(max_length=550, null=True, blank=True)
    cm_description = models.TextField(null=True, blank=True)
    replaced_asset_config_id = models.CharField(max_length=500  , null=True)
    cm_start_date = models.DateField(null=True, blank=True)
    cm_start_time = models.TimeField(max_length=15, null=True) 
    cm_end_date = models.DateField(null=True, blank=True)
    cm_end_time = models.TimeField(null=True,blank=True)
    oem_failure_reference = models.TextField(null=True, blank=True)
    defect = models.ForeignKey('Defect', on_delete=models.SET_NULL, null=True, blank=True)
    P_id = models.IntegerField(default=0)
    is_active = models.IntegerField(default=0)
    # root_cause = models.ForeignKey('RootCause', on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return ' '

    class Meta:
        verbose_name_plural = 'Failure data Collection Form'

class Asset(models.Model):
    asset_config_id = models.CharField(max_length=550, unique=True)
    asset_serial_number = models.CharField(max_length=550)
    location_id = models.TextField()
    location_description = models.TextField()
    asset_type = models.IntegerField(default=0)
    software_version = models.CharField(max_length=550)
    asset_description = models.TextField()
    software_description = models.TextField()
    asset_status = models.CharField(max_length=550)
    is_active = models.IntegerField(default=0)
    P_id = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Asset Register'

    def __str__(self):
        return self.asset_config_id

class Defect(models.Model):
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    asset_type = models.CharField(max_length=550, blank=True)
    defect_id = models.AutoField(primary_key=True)
    defect_description = models.TextField(blank=True)
    defect_open_date = models.DateField(null=True, blank=True)
    defect_closed_date = models.DateField(null=True, blank=True)
    investigation = models.TextField(blank=True)
    defect_status = models.CharField(max_length=550, blank=True)
    defect_status_remarks = models.TextField(blank=True)
    oem_defect_reference = models.TextField(blank=True)
    oem_target_date = models.DateField(null=True, blank=True)
    is_active = models.IntegerField(default=0)
    P_id = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = '(4) FRACAS Defect Identification'

    def start_date_to_string(self):
        if self.start_date is None:
            return ''
        else:
            return self.start_date.value_to_string(self.start_date, '%d-%m-%y') + '-'

    def end_date_to_string(self):
        if self.end_date is None:
            return ''
        else:
            return self.end_date.value_to_string(self.start_date ,'%d-%m-%y')

    def __str__(self):
        return (str(self.defect_id) + ': ' + str(self.defect_description))

class RootCause(models.Model):
    root_cause_id = models.AutoField(primary_key=True)
    asset_type = models.CharField(max_length=550, blank=True)
    rca_workshop_date = models.DateField(null=True, blank=True)
    root_cause_status = models.CharField(max_length=550, blank=True)
    defect = models.ForeignKey('Defect', on_delete=models.CASCADE, null=True, blank=True)
    immediate_cause = ModelArrowCharField(max_length=100, blank=True)
    leading_reasons = ModelArrowCharField(max_length=100, blank=True)
    root_cause_description = models.TextField()
    is_active = models.IntegerField(default=0)
    P_id = models.IntegerField(default=0)
    

    class Meta:
        verbose_name_plural = 'Root Cause Analysis'


class DefectDiscussion(models.Model):
    defect_discussion_id = models.AutoField(primary_key=True)
    meeting_date = models.DateField(null=True, blank=True, auto_now_add=True)
    attendees = models.ManyToManyField('UserProfile', blank=True)
    review_board = models.ForeignKey('ReviewBoard', on_delete=models.CASCADE)
    defect = models.ForeignKey('Defect', on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField(max_length=550, blank=True)

    def get_asset_type(self):
        if hasattr(self, 'review_board'):
            return self.review_board.asset_type
    
    def __str__(self):
        return ''
        


class Action(models.Model):
    action_id = models.AutoField(primary_key=True)
    action_description = models.CharField(max_length=550, blank=True)
    action_owner = models.CharField(max_length=550, blank=True)
    action_status = models.CharField(max_length=550, blank=True)
    action_due_date = models.DateField(null=True, blank=True)
    progress_log = models.TextField()
    defect_discussion_id = models.ForeignKey('DefectDiscussion', on_delete=models.CASCADE, to_field='defect_discussion_id', null=True, blank=True)
    
    def __str__(self):
        return ''


class ReviewBoard(models.Model):
    asset_type = models.CharField(max_length=550, blank=True)
    from_date = models.DateField(null=True, blank=True)
    to_date = models.DateField(null=True, blank=True)
    meeting_date = models.DateField(null=True, blank=True, auto_now_add=True)
    meeting_id = models.CharField(max_length=550, blank=True, null=True)
    meeting_status = models.CharField(max_length=550, blank=True)
    meeting_outcome = models.CharField(max_length=550, blank=True)
    is_active = models.IntegerField(default=0)
    P_id = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = '(6) FRACAS Review'

    def save(self, *args, **kwargs):
        if not self.meeting_id:
            self.meeting_id = self.id
        super(ReviewBoard, self).save(*args, **kwargs)

class EmployeeMaster(models.Model):
    employee_id =  models.CharField(max_length=550, blank=True, null=True)
    name = models.CharField(max_length=550, blank=True)
    designation = models.CharField(max_length=550, blank=True)
   
    def __str__(self):
        if self.employee_id and self.name:
            return self.employee_id + ': ' + self.name
        elif self.employee_id and not self.name:
            return self.employee_id
        elif self.name and not self.employee_id:
            return self.name
        else:
            return ''


    class Meta:
        verbose_name_plural = 'Employee Master'

class PBSMaster(models.Model):
    system = models.CharField(max_length=550, blank=True)
    subsystem = models.CharField(max_length=550, blank=True)
    project = models.ForeignKey('Product', on_delete=models.CASCADE,null=True, blank=True)
    product_id = models.CharField(max_length=550, blank=True)
    product_description = models.CharField(max_length=550, blank=True)
    asset_type = models.CharField(max_length=550, blank=True)
    asset_description = models.CharField(max_length=550, blank=True)
    MTBF = models.FloatField(default=0)
    MTBSAF = models.FloatField(default=0,blank=True)
    MTTR = models.FloatField(default=0,blank=True)
    MART = models.FloatField(default=0,blank=True)
    asset_quantity = models.IntegerField(default=0)
    is_active = models.IntegerField(default=0)
    availability_target = models.FloatField(default=0,blank=True)

    class Meta:
        verbose_name_plural = 'PBS Master'
        
    def __str__(self):
        return self.asset_type

class UserProfile(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE,null=True, blank=True)
    user_role = models.ForeignKey(Group, on_delete=models.CASCADE,null=True, blank=True,)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_active = models.IntegerField(default=0)
    is_disable = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name

class UserResetKey(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    key = models.CharField(max_length=255, db_index=True)
    # key_type = models.CharField(choices=keyChoices, max_length=20, null=True, blank=True)
    expires_on = models.DateTimeField(null=True, blank=True)
    otp_expires_on = models.DateTimeField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

class assetRegister(models.Model):
    
    class Meta:
        verbose_name_plural = 'Asset Register'
        
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    MTBF = models.FloatField(default=0)
    MTBSAF = models.FloatField(default=0)
    MTTR = models.FloatField(default=0)
    availability_target = models.FloatField(default=0)
    is_active = models.IntegerField(default=0)

    def __str__(self):
        return self.product_name

class temp_table_import_file(models.Model):
    # id = models.TextField()
    system = models.TextField()
    subsystem = models.TextField()
    subsystem_id = models.IntegerField()
    product_id = models.CharField(max_length=550, blank=True)
    product_description = models.TextField()
    asset_type = models.TextField()
    asset_description = models.TextField()
    MTBF = models.TextField()
    MTBSAF = models.TextField()
    MTTR = models.TextField()
    MART = models.TextField()
    asset_quantity = models.TextField()
    error_list = models.TextField()
    updated_by = models.TextField()

    
class temp_table_asset_register(models.Model):
    asset_config_id = models.CharField(max_length=550)
    asset_serial_number = models.CharField(max_length=550)
    location_id = models.TextField()
    location_description = models.TextField()
    asset_type = models.TextField()
    asset_type_id = models.TextField()
    software_version = models.CharField(max_length=550)
    asset_description = models.TextField()
    software_description = models.TextField()
    asset_status = models.CharField(max_length=550)
    is_active = models.IntegerField(default=0)
    P_id = models.TextField()
    error_list = models.TextField()
    updated_by = models.TextField()
    
class temp_table_FailureData(models.Model):
    failure_id = models.TextField()
    asset_type = models.TextField()
    asset_config_id = models.TextField()
    event_description = models.TextField()
    mode_id = models.TextField()
    mode_description = models.TextField()
    date = models.TextField()
    time = models.TextField()
    detection = models.TextField()
    service_delay = models.TextField()
    immediate_investigation = models.TextField()
    failure_type = models.TextField()
    safety_failure = models.TextField()
    hazard_id = models.TextField()
    cm_description = models.TextField()
    replaced_asset_config_id = models.TextField()
    cm_start_date = models.TextField()
    cm_start_time = models.TextField()
    cm_end_date = models.TextField()
    cm_end_time = models.TextField()
    oem_failure_reference = models.TextField()
    defect = models.TextField()
    P_id = models.TextField()
    is_active = models.TextField()
    updated_by = models.TextField()


class temp_table_failure_mode(models.Model):
    mode_id = models.TextField()
    mode_description = models.TextField()
    asset_type = models.TextField()
    asset_type_id = models.TextField()
    error_list = models.TextField()
    P_id = models.TextField()
    updated_by = models.TextField()

class temp_table_failure_data(models.Model):
    failure_id= models.BigIntegerField(null=True)
    asset_type= models.TextField()
    asset_config_id= models.TextField()
    asset_type_id= models.TextField()
    event_description= models.TextField()
    mode_id= models.TextField()
    date= models.TextField()
    time= models.TextField()
    detection= models.TextField()
    service_delay= models.TextField()
    immediate_investigation= models.TextField()
    failure_type= models.TextField()
    safety_failure= models.TextField()
    hazard_id= models.TextField()
    cm_description= models.TextField()
    replaced_asset_config_id= models.TextField()
    cm_start_date= models.TextField()
    cm_start_time= models.TextField()
    cm_end_date= models.TextField()
    cm_end_time= models.TextField()
    oem_failure_reference= models.TextField()
    defect= models.TextField()
    error_list = models.TextField()
    P_id = models.TextField()
    updated_by = models.TextField()
    
class history(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    P_id = models.IntegerField(default=0)
    date = models.DateField(null=True, blank=True)
    message = models.TextField()
    time = models.TimeField(max_length=15, null=True)
    function_name = models.CharField(max_length=50,null=True, blank=True)
    
   
class PBSUnit(models.Model):
    MTBFMTBSAF= models.TextField()
    MTTR = models.TextField()

class Systems(models.Model):
    project = models.ForeignKey('Product', on_delete=models.CASCADE,null=True, blank=True)
    System = models.CharField(max_length=550, blank=True)
    MTBF = models.FloatField(default=0)
    MTBSAF = models.FloatField(default=0)
    MTTR = models.FloatField(default=0)
    availability_target = models.FloatField(default=0)
    is_active = models.IntegerField(default=0)

    def __str__(self):
        return self.System
    