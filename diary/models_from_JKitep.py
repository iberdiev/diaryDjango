# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AQrCode(models.Model):
    qr_code = models.CharField(unique=True, max_length=5)
    generated = models.TextField()  # This field type is a guess.
    is_used = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'a_qr_code'


class AQrCodeGen(models.Model):
    qr_code = models.CharField(unique=True, max_length=5)
    user_id = models.IntegerField()
    active = models.IntegerField()
    record_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'a_qr_code_gen'


class Azat(models.Model):
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'azat'


class BerliGlobalsearchData(models.Model):
    gscrmid = models.OneToOneField('JkitepCrmentity', models.DO_NOTHING, db_column='gscrmid', primary_key=True)
    searchlabel = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'berli_globalsearch_data'


class BerliGlobalsearchSettings(models.Model):
    gstabid = models.OneToOneField('JkitepTab', models.DO_NOTHING, db_column='gstabid', primary_key=True)
    displayfield = models.CharField(max_length=150)
    searchcolumn = models.CharField(max_length=150)
    turn_off = models.IntegerField()
    sequence = models.IntegerField()
    searchall = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'berli_globalsearch_settings'


class ComJkitepWorkflowActivatedonce(models.Model):
    workflow_id = models.IntegerField(primary_key=True)
    entity_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'com_jkitep_workflow_activatedonce'
        unique_together = (('workflow_id', 'entity_id'),)


class ComJkitepWorkflowTasktypes(models.Model):
    id = models.IntegerField()
    tasktypename = models.CharField(max_length=255)
    label = models.CharField(max_length=255, blank=True, null=True)
    classname = models.CharField(max_length=255, blank=True, null=True)
    classpath = models.CharField(max_length=255, blank=True, null=True)
    templatepath = models.CharField(max_length=255, blank=True, null=True)
    modules = models.CharField(max_length=500, blank=True, null=True)
    sourcemodule = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'com_jkitep_workflow_tasktypes'


class ComJkitepWorkflowTasktypesSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'com_jkitep_workflow_tasktypes_seq'


class ComJkitepWorkflows(models.Model):
    workflow_id = models.AutoField(primary_key=True)
    module_name = models.CharField(max_length=100, blank=True, null=True)
    summary = models.CharField(max_length=400)
    test = models.TextField(blank=True, null=True)
    execution_condition = models.IntegerField()
    defaultworkflow = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    filtersavedinnew = models.IntegerField(blank=True, null=True)
    schtypeid = models.IntegerField(blank=True, null=True)
    schdayofmonth = models.CharField(max_length=100, blank=True, null=True)
    schdayofweek = models.CharField(max_length=100, blank=True, null=True)
    schannualdates = models.CharField(max_length=100, blank=True, null=True)
    schtime = models.CharField(max_length=50, blank=True, null=True)
    nexttrigger_time = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    workflowname = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'com_jkitep_workflows'


class ComJkitepWorkflowsSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'com_jkitep_workflows_seq'


class ComJkitepWorkflowtaskQueue(models.Model):
    task_id = models.IntegerField(blank=True, null=True)
    entity_id = models.CharField(max_length=100, blank=True, null=True)
    do_after = models.IntegerField(blank=True, null=True)
    relatedinfo = models.CharField(max_length=255, blank=True, null=True)
    task_contents = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'com_jkitep_workflowtask_queue'


class ComJkitepWorkflowtasks(models.Model):
    task_id = models.AutoField(primary_key=True)
    workflow_id = models.IntegerField(blank=True, null=True)
    summary = models.CharField(max_length=400)
    task = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'com_jkitep_workflowtasks'


class ComJkitepWorkflowtasksEntitymethod(models.Model):
    workflowtasks_entitymethod_id = models.IntegerField(primary_key=True)
    module_name = models.CharField(max_length=100, blank=True, null=True)
    method_name = models.CharField(max_length=100, blank=True, null=True)
    function_path = models.CharField(max_length=400, blank=True, null=True)
    function_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'com_jkitep_workflowtasks_entitymethod'


class ComJkitepWorkflowtasksEntitymethodSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'com_jkitep_workflowtasks_entitymethod_seq'


class ComJkitepWorkflowtasksSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'com_jkitep_workflowtasks_seq'


class ComJkitepWorkflowtemplates(models.Model):
    template_id = models.AutoField(primary_key=True)
    module_name = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=400, blank=True, null=True)
    template = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'com_jkitep_workflowtemplates'


class JkitepAcademicYearPay(models.Model):
    academic_year_payid = models.AutoField(primary_key=True)
    academic_year_pay = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_academic_year_pay'


class JkitepAcademicYearPaySeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_academic_year_pay_seq'


class JkitepAccount(models.Model):
    accountid = models.OneToOneField('JkitepCrmentity', models.DO_NOTHING, db_column='accountid', primary_key=True)
    account_no = models.CharField(max_length=100)
    accountname = models.CharField(max_length=100)
    parentid = models.IntegerField(blank=True, null=True)
    account_type = models.CharField(max_length=200, blank=True, null=True)
    industry = models.CharField(max_length=200, blank=True, null=True)
    annualrevenue = models.DecimalField(max_digits=25, decimal_places=8, blank=True, null=True)
    rating = models.CharField(max_length=200, blank=True, null=True)
    ownership = models.CharField(max_length=50, blank=True, null=True)
    siccode = models.CharField(max_length=50, blank=True, null=True)
    tickersymbol = models.CharField(max_length=30, blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    otherphone = models.CharField(max_length=30, blank=True, null=True)
    email1 = models.CharField(max_length=100, blank=True, null=True)
    email2 = models.CharField(max_length=100, blank=True, null=True)
    website = models.CharField(max_length=100, blank=True, null=True)
    fax = models.CharField(max_length=30, blank=True, null=True)
    employees = models.IntegerField(blank=True, null=True)
    emailoptout = models.CharField(max_length=3, blank=True, null=True)
    notify_owner = models.CharField(max_length=3, blank=True, null=True)
    inn = models.CharField(max_length=30, blank=True, null=True)
    kpp = models.CharField(max_length=30, blank=True, null=True)
    splastsms = models.DateTimeField(blank=True, null=True)
    one_s_id = models.CharField(max_length=255, blank=True, null=True)
    isconvertedfromlead = models.CharField(max_length=3, blank=True, null=True)
    tags = models.CharField(max_length=1, blank=True, null=True)
    full_name_2 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_account'


class JkitepAccountbillads(models.Model):
    accountaddressid = models.OneToOneField(JkitepAccount, models.DO_NOTHING, db_column='accountaddressid', primary_key=True)
    bill_city = models.CharField(max_length=30, blank=True, null=True)
    bill_code = models.CharField(max_length=30, blank=True, null=True)
    bill_country = models.CharField(max_length=30, blank=True, null=True)
    bill_state = models.CharField(max_length=30, blank=True, null=True)
    bill_street = models.CharField(max_length=250, blank=True, null=True)
    bill_pobox = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_accountbillads'


class JkitepAccountrating(models.Model):
    accountratingid = models.AutoField(primary_key=True)
    rating = models.CharField(unique=True, max_length=200)
    sortorderid = models.IntegerField()
    presence = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_accountrating'


class JkitepAccountscf(models.Model):
    accountid = models.OneToOneField(JkitepAccount, models.DO_NOTHING, db_column='accountid', primary_key=True)
    vk_url = models.CharField(max_length=155, blank=True, null=True)
    tw_url = models.CharField(max_length=155, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_accountscf'


class JkitepAccountshipads(models.Model):
    accountaddressid = models.OneToOneField(JkitepAccount, models.DO_NOTHING, db_column='accountaddressid', primary_key=True)
    ship_city = models.CharField(max_length=30, blank=True, null=True)
    ship_code = models.CharField(max_length=30, blank=True, null=True)
    ship_country = models.CharField(max_length=30, blank=True, null=True)
    ship_state = models.CharField(max_length=30, blank=True, null=True)
    ship_pobox = models.CharField(max_length=30, blank=True, null=True)
    ship_street = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_accountshipads'


class JkitepAccounttype(models.Model):
    accounttypeid = models.AutoField(primary_key=True)
    accounttype = models.CharField(unique=True, max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_accounttype'


class JkitepAccounttypeSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_accounttype_seq'


class JkitepActionmapping(models.Model):
    actionid = models.IntegerField(primary_key=True)
    actionname = models.CharField(max_length=200)
    securitycheck = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_actionmapping'
        unique_together = (('actionid', 'actionname'),)


class JkitepActivity(models.Model):
    activityid = models.OneToOneField('JkitepCrmentity', models.DO_NOTHING, db_column='activityid', primary_key=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    semodule = models.CharField(max_length=20, blank=True, null=True)
    activitytype = models.CharField(max_length=200)
    date_start = models.DateField()
    due_date = models.DateField(blank=True, null=True)
    time_start = models.CharField(max_length=50, blank=True, null=True)
    time_end = models.CharField(max_length=50, blank=True, null=True)
    sendnotification = models.CharField(max_length=3)
    duration_hours = models.CharField(max_length=200, blank=True, null=True)
    duration_minutes = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=200, blank=True, null=True)
    eventstatus = models.CharField(max_length=200, blank=True, null=True)
    priority = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=150, blank=True, null=True)
    notime = models.CharField(max_length=3)
    visibility = models.CharField(max_length=50)
    recurringtype = models.CharField(max_length=200, blank=True, null=True)
    tags = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_activity'


class JkitepActivityRecurringInfo(models.Model):
    activityid = models.IntegerField()
    recurrenceid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_activity_recurring_info'


class JkitepActivityReminder(models.Model):
    activity = models.OneToOneField(JkitepActivity, models.DO_NOTHING, primary_key=True)
    reminder_time = models.IntegerField()
    reminder_sent = models.IntegerField()
    recurringid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_activity_reminder'
        unique_together = (('activity', 'recurringid'),)


class JkitepActivityReminderPopup(models.Model):
    reminderid = models.AutoField(primary_key=True)
    semodule = models.CharField(max_length=100)
    recordid = models.IntegerField()
    date_start = models.DateField()
    time_start = models.CharField(max_length=100)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_activity_reminder_popup'


class JkitepActivityView(models.Model):
    activity_viewid = models.AutoField(primary_key=True)
    activity_view = models.CharField(max_length=200)
    sortorderid = models.IntegerField()
    presence = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_activity_view'


class JkitepActivityViewSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_activity_view_seq'


class JkitepActivitycf(models.Model):
    activityid = models.OneToOneField(JkitepActivity, models.DO_NOTHING, db_column='activityid', primary_key=True)

    class Meta:
        managed = False
        db_table = 'jkitep_activitycf'


class JkitepActivityproductrel(models.Model):
    activityid = models.IntegerField(primary_key=True)
    productid = models.ForeignKey('JkitepProducts', models.DO_NOTHING, db_column='productid')

    class Meta:
        managed = False
        db_table = 'jkitep_activityproductrel'
        unique_together = (('activityid', 'productid'),)


class JkitepActivitytype(models.Model):
    activitytypeid = models.AutoField(primary_key=True)
    activitytype = models.CharField(unique=True, max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_activitytype'


class JkitepActivitytypeSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_activitytype_seq'


class JkitepAnnouncement(models.Model):
    creatorid = models.IntegerField(primary_key=True)
    announcement = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'jkitep_announcement'


class JkitepApp2Tab(models.Model):
    tabid = models.ForeignKey('JkitepTab', models.DO_NOTHING, db_column='tabid', blank=True, null=True)
    appname = models.CharField(max_length=20, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    visible = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_app2tab'


class JkitepAreastaff(models.Model):
    areastaffid = models.IntegerField(primary_key=True)
    area_staff_no = models.CharField(max_length=100, blank=True, null=True)
    firstname = models.CharField(max_length=100, blank=True, null=True)
    lastname = models.CharField(max_length=100, blank=True, null=True)
    patronymic = models.CharField(max_length=100, blank=True, null=True)
    pin_con = models.CharField(max_length=100, blank=True, null=True)
    status_users_area = models.CharField(max_length=100, blank=True, null=True)
    user_employee_id = models.CharField(max_length=100, blank=True, null=True)
    mobile_phone = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    regions_id = models.CharField(max_length=100, blank=True, null=True)
    role_name_area = models.CharField(max_length=100, blank=True, null=True)
    employees_id_user = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_areastaff'


class JkitepAreastaffUserField(models.Model):
    recordid = models.IntegerField()
    userid = models.IntegerField()
    starred = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_areastaff_user_field'


class JkitepAreastaffcf(models.Model):
    areastaffid = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'jkitep_areastaffcf'


class JkitepAssets(models.Model):
    assetsid = models.OneToOneField('JkitepCrmentity', models.DO_NOTHING, db_column='assetsid', primary_key=True)
    asset_no = models.CharField(max_length=30)
    account = models.IntegerField(blank=True, null=True)
    product = models.IntegerField()
    serialnumber = models.CharField(max_length=200, blank=True, null=True)
    datesold = models.DateField(blank=True, null=True)
    dateinservice = models.DateField(blank=True, null=True)
    assetstatus = models.CharField(max_length=200, blank=True, null=True)
    tagnumber = models.CharField(max_length=300, blank=True, null=True)
    invoiceid = models.IntegerField(blank=True, null=True)
    shippingmethod = models.CharField(max_length=200, blank=True, null=True)
    shippingtrackingnumber = models.CharField(max_length=200, blank=True, null=True)
    assetname = models.CharField(max_length=100, blank=True, null=True)
    contact = models.IntegerField(blank=True, null=True)
    tags = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_assets'


class JkitepAssetscf(models.Model):
    assetsid = models.OneToOneField(JkitepAssets, models.DO_NOTHING, db_column='assetsid', primary_key=True)

    class Meta:
        managed = False
        db_table = 'jkitep_assetscf'


class JkitepAssetstatus(models.Model):
    assetstatusid = models.AutoField(primary_key=True)
    assetstatus = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_assetstatus'


class JkitepAssetstatusSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_assetstatus_seq'


class JkitepAsterisk(models.Model):
    server = models.CharField(max_length=30, blank=True, null=True)
    port = models.CharField(max_length=30, blank=True, null=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    version = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_asterisk'


class JkitepAsteriskextensions(models.Model):
    userid = models.IntegerField(blank=True, null=True)
    asterisk_extension = models.CharField(max_length=50, blank=True, null=True)
    use_asterisk = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_asteriskextensions'


class JkitepAsteriskincomingcalls(models.Model):
    from_number = models.CharField(max_length=50, blank=True, null=True)
    from_name = models.CharField(max_length=50, blank=True, null=True)
    to_number = models.CharField(max_length=50, blank=True, null=True)
    callertype = models.CharField(max_length=30, blank=True, null=True)
    flag = models.IntegerField(blank=True, null=True)
    timer = models.IntegerField(blank=True, null=True)
    refuid = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_asteriskincomingcalls'


class JkitepAsteriskincomingevents(models.Model):
    uid = models.CharField(primary_key=True, max_length=255)
    channel = models.CharField(max_length=100, blank=True, null=True)
    from_number = models.BigIntegerField(blank=True, null=True)
    from_name = models.CharField(max_length=100, blank=True, null=True)
    to_number = models.BigIntegerField(blank=True, null=True)
    callertype = models.CharField(max_length=100, blank=True, null=True)
    timer = models.IntegerField(blank=True, null=True)
    flag = models.CharField(max_length=3, blank=True, null=True)
    pbxrecordid = models.IntegerField(blank=True, null=True)
    relcrmid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_asteriskincomingevents'


class JkitepAttachments(models.Model):
    attachmentsid = models.OneToOneField('JkitepCrmentity', models.DO_NOTHING, db_column='attachmentsid', primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    path = models.TextField(blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_attachments'


class JkitepAttachmentsfolder(models.Model):
    folderid = models.AutoField(primary_key=True)
    foldername = models.CharField(max_length=200)
    description = models.CharField(max_length=250, blank=True, null=True)
    createdby = models.IntegerField()
    sequence = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_attachmentsfolder'


class JkitepAttachmentsfolderSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_attachmentsfolder_seq'


class JkitepAuditHelp(models.Model):
    audit_helpid = models.AutoField(primary_key=True)
    audit_help = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_audit_help'


class JkitepAuditHelpSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_audit_help_seq'


class JkitepAuditTrial(models.Model):
    auditid = models.IntegerField(primary_key=True)
    userid = models.IntegerField(blank=True, null=True)
    module = models.CharField(max_length=255, blank=True, null=True)
    action = models.CharField(max_length=255, blank=True, null=True)
    recordid = models.CharField(max_length=20, blank=True, null=True)
    actiondate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_audit_trial'


class JkitepAuthor(models.Model):
    authorid = models.AutoField(primary_key=True)
    author = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_author'


class JkitepAuthorSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_author_seq'


class JkitepBenefit(models.Model):
    benefitid = models.IntegerField(primary_key=True)
    ben_no = models.CharField(max_length=100, blank=True, null=True)
    bname = models.CharField(max_length=100, blank=True, null=True)
    pedadvice = models.CharField(max_length=100, blank=True, null=True)
    discount = models.CharField(max_length=100, blank=True, null=True)
    confirmation = models.CharField(max_length=100, blank=True, null=True)
    pedadvicedoc = models.CharField(max_length=100, blank=True, null=True)
    student_id = models.CharField(max_length=100, blank=True, null=True)
    yyyy = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_benefit'


class JkitepBenefitUserField(models.Model):
    recordid = models.IntegerField()
    userid = models.IntegerField()
    starred = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_benefit_user_field'


class JkitepBenefitcf(models.Model):
    benefitid = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'jkitep_benefitcf'


class JkitepBilled(models.Model):
    billedid = models.IntegerField(primary_key=True)
    billed_no = models.CharField(max_length=100, blank=True, null=True)
    student_id = models.CharField(max_length=100)
    yyyy = models.CharField(max_length=100)
    class_id = models.CharField(max_length=100, blank=True, null=True)
    cost = models.CharField(max_length=100, blank=True, null=True)
    product_id = models.CharField(max_length=100, blank=True, null=True)
    status_billed = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_billed'


class JkitepBilledUserField(models.Model):
    recordid = models.IntegerField()
    userid = models.IntegerField()
    starred = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_billed_user_field'


class JkitepBilledcf(models.Model):
    billedid = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'jkitep_billedcf'


class JkitepBlocks(models.Model):
    blockid = models.IntegerField(primary_key=True)
    tabid = models.ForeignKey('JkitepTab', models.DO_NOTHING, db_column='tabid')
    blocklabel = models.CharField(max_length=100)
    sequence = models.IntegerField(blank=True, null=True)
    show_title = models.IntegerField(blank=True, null=True)
    visible = models.IntegerField()
    create_view = models.IntegerField()
    edit_view = models.IntegerField()
    detail_view = models.IntegerField()
    display_status = models.IntegerField()
    iscustom = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_blocks'


class JkitepBlocksSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_blocks_seq'


class JkitepBname(models.Model):
    bnameid = models.AutoField(primary_key=True)
    bname = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_bname'


class JkitepBnameSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_bname_seq'


class JkitepBookfund(models.Model):
    bookfundid = models.IntegerField(primary_key=True)
    book_fund_no = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    author = models.CharField(max_length=100, blank=True, null=True)
    publisher = models.CharField(max_length=100, blank=True, null=True)
    subject = models.CharField(max_length=100, blank=True, null=True)
    year_of_publishing = models.DateField(blank=True, null=True)
    class_num_book_fund = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_bookfund'


class JkitepBookfundUserField(models.Model):
    recordid = models.IntegerField()
    userid = models.IntegerField()
    starred = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_bookfund_user_field'


class JkitepBookfundcf(models.Model):
    bookfundid = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'jkitep_bookfundcf'


class JkitepBuildingstate(models.Model):
    buildingstateid = models.AutoField(primary_key=True)
    buildingstate = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_buildingstate'


class JkitepBuildingstateSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_buildingstate_seq'


class JkitepCalendarDefaultActivitytypes(models.Model):
    id = models.IntegerField(primary_key=True)
    module = models.CharField(max_length=50, blank=True, null=True)
    fieldname = models.CharField(max_length=50, blank=True, null=True)
    defaultcolor = models.CharField(max_length=50, blank=True, null=True)
    isdefault = models.IntegerField(blank=True, null=True)
    conditions = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_calendar_default_activitytypes'


class JkitepCalendarDefaultActivitytypesSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_calendar_default_activitytypes_seq'


class JkitepCalendarUserActivitytypes(models.Model):
    id = models.IntegerField(primary_key=True)
    defaultid = models.IntegerField(blank=True, null=True)
    userid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    visible = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_calendar_user_activitytypes'


class JkitepCalendarUserActivitytypesSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_calendar_user_activitytypes_seq'


class JkitepCalendarsharedtype(models.Model):
    calendarsharedtypeid = models.AutoField(primary_key=True)
    calendarsharedtype = models.CharField(max_length=200)
    sortorderid = models.IntegerField(blank=True, null=True)
    presence = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_calendarsharedtype'


class JkitepCalendarsharedtypeSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_calendarsharedtype_seq'


class JkitepCallduration(models.Model):
    calldurationid = models.AutoField(primary_key=True)
    callduration = models.CharField(max_length=200)
    sortorderid = models.IntegerField(blank=True, null=True)
    presence = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_callduration'


class JkitepCalldurationSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_callduration_seq'


class JkitepCampaign(models.Model):
    campaign_no = models.CharField(max_length=100)
    campaignname = models.CharField(max_length=255, blank=True, null=True)
    campaigntype = models.CharField(max_length=200, blank=True, null=True)
    campaignstatus = models.CharField(max_length=200, blank=True, null=True)
    expectedrevenue = models.DecimalField(max_digits=25, decimal_places=8, blank=True, null=True)
    budgetcost = models.DecimalField(max_digits=25, decimal_places=8, blank=True, null=True)
    actualcost = models.DecimalField(max_digits=25, decimal_places=8, blank=True, null=True)
    expectedresponse = models.CharField(max_length=200, blank=True, null=True)
    numsent = models.DecimalField(max_digits=11, decimal_places=0, blank=True, null=True)
    product_id = models.IntegerField(blank=True, null=True)
    sponsor = models.CharField(max_length=255, blank=True, null=True)
    targetaudience = models.CharField(max_length=255, blank=True, null=True)
    targetsize = models.IntegerField(blank=True, null=True)
    expectedresponsecount = models.IntegerField(blank=True, null=True)
    expectedsalescount = models.IntegerField(blank=True, null=True)
    expectedroi = models.DecimalField(max_digits=25, decimal_places=8, blank=True, null=True)
    actualresponsecount = models.IntegerField(blank=True, null=True)
    actualsalescount = models.IntegerField(blank=True, null=True)
    actualroi = models.DecimalField(max_digits=25, decimal_places=8, blank=True, null=True)
    campaignid = models.OneToOneField('JkitepCrmentity', models.DO_NOTHING, db_column='campaignid', primary_key=True)
    closingdate = models.DateField(blank=True, null=True)
    tags = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_campaign'


class JkitepCampaignaccountrel(models.Model):
    campaignid = models.IntegerField(blank=True, null=True)
    accountid = models.IntegerField(blank=True, null=True)
    campaignrelstatusid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_campaignaccountrel'


class JkitepCampaigncontrel(models.Model):
    campaignid = models.IntegerField(primary_key=True)
    contactid = models.ForeignKey('JkitepContactdetails', models.DO_NOTHING, db_column='contactid')
    campaignrelstatusid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_campaigncontrel'
        unique_together = (('campaignid', 'contactid', 'campaignrelstatusid'),)


class JkitepCampaignleadrel(models.Model):
    campaignid = models.IntegerField(primary_key=True)
    leadid = models.ForeignKey('JkitepLeaddetails', models.DO_NOTHING, db_column='leadid')
    campaignrelstatusid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_campaignleadrel'
        unique_together = (('campaignid', 'leadid', 'campaignrelstatusid'),)


class JkitepCampaignrelstatus(models.Model):
    campaignrelstatusid = models.IntegerField(blank=True, null=True)
    campaignrelstatus = models.CharField(max_length=256, blank=True, null=True)
    sortorderid = models.IntegerField(blank=True, null=True)
    presence = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_campaignrelstatus'


class JkitepCampaignrelstatusSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_campaignrelstatus_seq'


class JkitepCampaignscf(models.Model):
    campaignid = models.OneToOneField(JkitepCampaign, models.DO_NOTHING, db_column='campaignid', primary_key=True)

    class Meta:
        managed = False
        db_table = 'jkitep_campaignscf'


class JkitepCampaignstatus(models.Model):
    campaignstatusid = models.AutoField(primary_key=True)
    campaignstatus = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_campaignstatus'


class JkitepCampaignstatusSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_campaignstatus_seq'


class JkitepCampaigntype(models.Model):
    campaigntypeid = models.AutoField(primary_key=True)
    campaigntype = models.CharField(unique=True, max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_campaigntype'


class JkitepCampaigntypeSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_campaigntype_seq'


class JkitepCarrier(models.Model):
    carrierid = models.AutoField(primary_key=True)
    carrier = models.CharField(unique=True, max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_carrier'


class JkitepCarrierSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_carrier_seq'


class JkitepClassName(models.Model):
    class_nameid = models.AutoField(primary_key=True)
    class_name = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_class_name'


class JkitepClassNameSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_class_name_seq'


class JkitepClassNum(models.Model):
    class_numid = models.AutoField(primary_key=True)
    class_num = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_class_num'


class JkitepClassNumBookFund(models.Model):
    class_num_book_fundid = models.AutoField(primary_key=True)
    class_num_book_fund = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_class_num_book_fund'


class JkitepClassNumBookFundSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_class_num_book_fund_seq'


class JkitepClassNumSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_class_num_seq'


class JkitepClassNumSer(models.Model):
    class_num_serid = models.AutoField(primary_key=True)
    class_num_ser = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_class_num_ser'


class JkitepClassNumSerSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_class_num_ser_seq'


class JkitepClasses(models.Model):
    classesid = models.IntegerField(primary_key=True)
    classes_no = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    class_num = models.CharField(max_length=200, blank=True, null=True)
    class_name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_classes'


class JkitepClassesUserField(models.Model):
    recordid = models.IntegerField()
    userid = models.IntegerField()
    starred = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_classes_user_field'


class JkitepClassescf(models.Model):
    classesid = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'jkitep_classescf'


class JkitepCntactivityrel(models.Model):
    contactid = models.OneToOneField('JkitepContactdetails', models.DO_NOTHING, db_column='contactid', primary_key=True)
    activityid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_cntactivityrel'
        unique_together = (('contactid', 'activityid'),)


class JkitepContactaddress(models.Model):
    contactaddressid = models.OneToOneField('JkitepContactdetails', models.DO_NOTHING, db_column='contactaddressid', primary_key=True)
    mailingcity = models.CharField(max_length=40, blank=True, null=True)
    mailingstreet = models.CharField(max_length=250, blank=True, null=True)
    mailingcountry = models.CharField(max_length=40, blank=True, null=True)
    othercountry = models.CharField(max_length=30, blank=True, null=True)
    mailingstate = models.CharField(max_length=30, blank=True, null=True)
    mailingpobox = models.CharField(max_length=30, blank=True, null=True)
    othercity = models.CharField(max_length=40, blank=True, null=True)
    otherstate = models.CharField(max_length=50, blank=True, null=True)
    mailingzip = models.CharField(max_length=30, blank=True, null=True)
    otherzip = models.CharField(max_length=30, blank=True, null=True)
    otherstreet = models.CharField(max_length=250, blank=True, null=True)
    otherpobox = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_contactaddress'


class JkitepContactdetails(models.Model):
    contactid = models.OneToOneField('JkitepCrmentity', models.DO_NOTHING, db_column='contactid', primary_key=True)
    contact_no = models.CharField(max_length=100)
    accountid = models.IntegerField(blank=True, null=True)
    salutation = models.CharField(max_length=200, blank=True, null=True)
    lastname = models.CharField(max_length=80)
    firstname = models.CharField(max_length=40, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    mobile = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    department = models.CharField(max_length=30, blank=True, null=True)
    fax = models.CharField(max_length=50, blank=True, null=True)
    reportsto = models.CharField(max_length=30, blank=True, null=True)
    training = models.CharField(max_length=50, blank=True, null=True)
    usertype = models.CharField(max_length=50, blank=True, null=True)
    contacttype = models.CharField(max_length=50, blank=True, null=True)
    otheremail = models.CharField(max_length=100, blank=True, null=True)
    secondaryemail = models.CharField(max_length=100, blank=True, null=True)
    donotcall = models.CharField(max_length=3, blank=True, null=True)
    emailoptout = models.CharField(max_length=3, blank=True, null=True)
    imagename = models.CharField(max_length=150, blank=True, null=True)
    reference = models.CharField(max_length=3, blank=True, null=True)
    notify_owner = models.CharField(max_length=3, blank=True, null=True)
    splastsms = models.DateTimeField(blank=True, null=True)
    isconvertedfromlead = models.CharField(max_length=3, blank=True, null=True)
    tags = models.CharField(max_length=1, blank=True, null=True)
    patronymic = models.CharField(max_length=100, blank=True, null=True)
    pin_con = models.CharField(max_length=100, blank=True, null=True)
    class_id = models.CharField(max_length=100, blank=True, null=True)
    school_id = models.CharField(max_length=100, blank=True, null=True)
    balance = models.DecimalField(max_digits=27, decimal_places=8, blank=True, null=True)
    gender = models.CharField(max_length=50, blank=True, null=True)
    benefit = models.CharField(max_length=100, blank=True, null=True)
    startbalance = models.CharField(max_length=100, blank=True, null=True)
    bdate = models.DateField(blank=True, null=True)
    school_class_id = models.CharField(max_length=100, blank=True, null=True)
    balance_sum = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_contactdetails'


class JkitepContactscf(models.Model):
    contactid = models.OneToOneField(JkitepContactdetails, models.DO_NOTHING, db_column='contactid', primary_key=True)
    vk_url = models.CharField(max_length=155, blank=True, null=True)
    tw_url = models.CharField(max_length=155, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_contactscf'


class JkitepContactsubdetails(models.Model):
    contactsubscriptionid = models.OneToOneField(JkitepContactdetails, models.DO_NOTHING, db_column='contactsubscriptionid', primary_key=True)
    homephone = models.CharField(max_length=50, blank=True, null=True)
    otherphone = models.CharField(max_length=50, blank=True, null=True)
    assistant = models.CharField(max_length=30, blank=True, null=True)
    assistantphone = models.CharField(max_length=50, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    laststayintouchrequest = models.IntegerField(blank=True, null=True)
    laststayintouchsavedate = models.IntegerField(blank=True, null=True)
    leadsource = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_contactsubdetails'


class JkitepContpotentialrel(models.Model):
    contactid = models.IntegerField(primary_key=True)
    potentialid = models.ForeignKey('JkitepPotential', models.DO_NOTHING, db_column='potentialid')

    class Meta:
        managed = False
        db_table = 'jkitep_contpotentialrel'
        unique_together = (('contactid', 'potentialid'),)


class JkitepContractPriority(models.Model):
    contract_priorityid = models.AutoField(primary_key=True)
    contract_priority = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_contract_priority'


class JkitepContractPrioritySeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_contract_priority_seq'


class JkitepContractStatus(models.Model):
    contract_statusid = models.AutoField(primary_key=True)
    contract_status = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_contract_status'


class JkitepContractStatusSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_contract_status_seq'


class JkitepContractType(models.Model):
    contract_typeid = models.AutoField(primary_key=True)
    contract_type = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_contract_type'


class JkitepContractTypeSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_contract_type_seq'


class JkitepConvertleadmapping(models.Model):
    cfmid = models.AutoField(primary_key=True)
    leadfid = models.IntegerField()
    accountfid = models.IntegerField(blank=True, null=True)
    contactfid = models.IntegerField(blank=True, null=True)
    potentialfid = models.IntegerField(blank=True, null=True)
    editable = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_convertleadmapping'


class JkitepConvertpotentialmapping(models.Model):
    cfmid = models.AutoField(primary_key=True)
    potentialfid = models.IntegerField()
    projectfid = models.IntegerField(blank=True, null=True)
    editable = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_convertpotentialmapping'


class JkitepCrmentity(models.Model):
    crmid = models.IntegerField(primary_key=True)
    smcreatorid = models.IntegerField()
    smownerid = models.IntegerField()
    modifiedby = models.IntegerField()
    setype = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    createdtime = models.DateTimeField()
    modifiedtime = models.DateTimeField()
    viewedtime = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    version = models.IntegerField()
    presence = models.IntegerField(blank=True, null=True)
    deleted = models.IntegerField()
    smgroupid = models.IntegerField(blank=True, null=True)
    source = models.CharField(max_length=100, blank=True, null=True)
    label = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_crmentity'


class JkitepCrmentitySeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_crmentity_seq'


class JkitepCrmentityUserField(models.Model):
    recordid = models.ForeignKey(JkitepCrmentity, models.DO_NOTHING, db_column='recordid')
    userid = models.IntegerField()
    starred = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_crmentity_user_field'


class JkitepCrmentityrel(models.Model):
    crmid = models.IntegerField()
    module = models.CharField(max_length=100)
    relcrmid = models.IntegerField()
    relmodule = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'jkitep_crmentityrel'


class JkitepCrmsetup(models.Model):
    userid = models.IntegerField(blank=True, null=True)
    setup_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_crmsetup'


class JkitepCronTask(models.Model):
    name = models.CharField(unique=True, max_length=100, blank=True, null=True)
    handler_file = models.CharField(unique=True, max_length=100, blank=True, null=True)
    frequency = models.IntegerField(blank=True, null=True)
    laststart = models.PositiveIntegerField(blank=True, null=True)
    lastend = models.PositiveIntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    module = models.CharField(max_length=100, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_cron_task'


class JkitepCurrencies(models.Model):
    currencyid = models.AutoField(primary_key=True)
    currency_name = models.CharField(max_length=200, blank=True, null=True)
    currency_code = models.CharField(max_length=50, blank=True, null=True)
    currency_symbol = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_currencies'


class JkitepCurrenciesSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_currencies_seq'


class JkitepCurrency(models.Model):
    currencyid = models.AutoField(primary_key=True)
    currency = models.CharField(unique=True, max_length=200)
    sortorderid = models.IntegerField()
    presence = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_currency'


class JkitepCurrencyDecimalSeparator(models.Model):
    currency_decimal_separatorid = models.AutoField(primary_key=True)
    currency_decimal_separator = models.CharField(max_length=2)
    sortorderid = models.IntegerField()
    presence = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_currency_decimal_separator'


class JkitepCurrencyDecimalSeparatorSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_currency_decimal_separator_seq'


class JkitepCurrencyGroupingPattern(models.Model):
    currency_grouping_patternid = models.AutoField(primary_key=True)
    currency_grouping_pattern = models.CharField(max_length=200)
    sortorderid = models.IntegerField()
    presence = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_currency_grouping_pattern'


class JkitepCurrencyGroupingPatternSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_currency_grouping_pattern_seq'


class JkitepCurrencyGroupingSeparator(models.Model):
    currency_grouping_separatorid = models.AutoField(primary_key=True)
    currency_grouping_separator = models.CharField(max_length=2)
    sortorderid = models.IntegerField()
    presence = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_currency_grouping_separator'


class JkitepCurrencyGroupingSeparatorSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_currency_grouping_separator_seq'


class JkitepCurrencyInfo(models.Model):
    currency_name = models.CharField(max_length=100, blank=True, null=True)
    currency_code = models.CharField(max_length=100, blank=True, null=True)
    currency_symbol = models.CharField(max_length=30, blank=True, null=True)
    conversion_rate = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)
    currency_status = models.CharField(max_length=25, blank=True, null=True)
    defaultid = models.CharField(max_length=10)
    deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_currency_info'


class JkitepCurrencyInfoSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_currency_info_seq'


class JkitepCurrencySymbolPlacement(models.Model):
    currency_symbol_placementid = models.AutoField(primary_key=True)
    currency_symbol_placement = models.CharField(max_length=30)
    sortorderid = models.IntegerField()
    presence = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_currency_symbol_placement'


class JkitepCurrencySymbolPlacementSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_currency_symbol_placement_seq'


class JkitepCustomaction(models.Model):
    cvid = models.ForeignKey('JkitepCustomview', models.DO_NOTHING, db_column='cvid')
    subject = models.CharField(max_length=250)
    module = models.CharField(max_length=50)
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_customaction'


class JkitepCustomerdetails(models.Model):
    customerid = models.OneToOneField(JkitepContactdetails, models.DO_NOTHING, db_column='customerid', primary_key=True)
    portal = models.CharField(max_length=3, blank=True, null=True)
    support_start_date = models.DateField(blank=True, null=True)
    support_end_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_customerdetails'


class JkitepCustomerportalFields(models.Model):
    tabid = models.IntegerField(primary_key=True)
    fieldinfo = models.TextField(blank=True, null=True)
    records_visible = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_customerportal_fields'


class JkitepCustomerportalPrefs(models.Model):
    tabid = models.IntegerField(primary_key=True)
    prefkey = models.CharField(max_length=100)
    prefvalue = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_customerportal_prefs'
        unique_together = (('tabid', 'prefkey'),)


class JkitepCustomerportalRelatedmoduleinfo(models.Model):
    tabid = models.IntegerField(primary_key=True)
    relatedmodules = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_customerportal_relatedmoduleinfo'


class JkitepCustomerportalSettings(models.Model):
    id = models.IntegerField(blank=True, null=True)
    url = models.CharField(max_length=250, blank=True, null=True)
    default_assignee = models.IntegerField(blank=True, null=True)
    support_notification = models.IntegerField(blank=True, null=True)
    announcement = models.TextField(blank=True, null=True)
    shortcuts = models.TextField(blank=True, null=True)
    widgets = models.TextField(blank=True, null=True)
    charts = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_customerportal_settings'


class JkitepCustomerportalTabs(models.Model):
    tabid = models.IntegerField(primary_key=True)
    visible = models.IntegerField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    createrecord = models.IntegerField()
    editrecord = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_customerportal_tabs'


class JkitepCustomview(models.Model):
    cvid = models.IntegerField(primary_key=True)
    viewname = models.CharField(max_length=100)
    setdefault = models.IntegerField(blank=True, null=True)
    setmetrics = models.IntegerField(blank=True, null=True)
    entitytype = models.ForeignKey('JkitepTab', models.DO_NOTHING, db_column='entitytype')
    status = models.IntegerField(blank=True, null=True)
    userid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_customview'


class JkitepCustomviewSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_customview_seq'


class JkitepCv2Group(models.Model):
    cvid = models.ForeignKey(JkitepCustomview, models.DO_NOTHING, db_column='cvid')
    groupid = models.ForeignKey('JkitepGroups', models.DO_NOTHING, db_column='groupid')

    class Meta:
        managed = False
        db_table = 'jkitep_cv2group'


class JkitepCv2Role(models.Model):
    cvid = models.ForeignKey(JkitepCustomview, models.DO_NOTHING, db_column='cvid')
    roleid = models.ForeignKey('JkitepRole', models.DO_NOTHING, db_column='roleid')

    class Meta:
        managed = False
        db_table = 'jkitep_cv2role'


class JkitepCv2Rs(models.Model):
    cvid = models.ForeignKey(JkitepCustomview, models.DO_NOTHING, db_column='cvid')
    rsid = models.ForeignKey('JkitepRole', models.DO_NOTHING, db_column='rsid')

    class Meta:
        managed = False
        db_table = 'jkitep_cv2rs'


class JkitepCv2Users(models.Model):
    cvid = models.ForeignKey(JkitepCustomview, models.DO_NOTHING, db_column='cvid')
    userid = models.ForeignKey('JkitepUsers', models.DO_NOTHING, db_column='userid')

    class Meta:
        managed = False
        db_table = 'jkitep_cv2users'


class JkitepCvadvfilter(models.Model):
    cvid = models.OneToOneField(JkitepCustomview, models.DO_NOTHING, db_column='cvid', primary_key=True)
    columnindex = models.IntegerField()
    columnname = models.CharField(max_length=250, blank=True, null=True)
    comparator = models.CharField(max_length=20, blank=True, null=True)
    value = models.CharField(max_length=512, blank=True, null=True)
    groupid = models.IntegerField(blank=True, null=True)
    column_condition = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_cvadvfilter'
        unique_together = (('cvid', 'columnindex'),)


class JkitepCvadvfilterGrouping(models.Model):
    groupid = models.IntegerField(primary_key=True)
    cvid = models.IntegerField()
    group_condition = models.CharField(max_length=255, blank=True, null=True)
    condition_expression = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_cvadvfilter_grouping'
        unique_together = (('groupid', 'cvid'),)


class JkitepCvcolumnlist(models.Model):
    cvid = models.OneToOneField(JkitepCustomview, models.DO_NOTHING, db_column='cvid', primary_key=True)
    columnindex = models.IntegerField()
    columnname = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_cvcolumnlist'
        unique_together = (('cvid', 'columnindex'),)


class JkitepCvstdfilter(models.Model):
    cvid = models.ForeignKey(JkitepCustomview, models.DO_NOTHING, db_column='cvid')
    columnname = models.CharField(max_length=250, blank=True, null=True)
    stdfilter = models.CharField(max_length=250, blank=True, null=True)
    startdate = models.DateField(blank=True, null=True)
    enddate = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_cvstdfilter'


class JkitepDashboardTabs(models.Model):
    tabname = models.CharField(max_length=50, blank=True, null=True)
    isdefault = models.IntegerField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    appname = models.CharField(max_length=20, blank=True, null=True)
    modulename = models.CharField(max_length=50, blank=True, null=True)
    userid = models.ForeignKey('JkitepUsers', models.DO_NOTHING, db_column='userid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_dashboard_tabs'
        unique_together = (('tabname', 'userid'),)


class JkitepDatashareGrp2Grp(models.Model):
    shareid = models.IntegerField(primary_key=True)
    share_groupid = models.IntegerField(blank=True, null=True)
    to_groupid = models.ForeignKey('JkitepGroups', models.DO_NOTHING, db_column='to_groupid', blank=True, null=True)
    permission = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_datashare_grp2grp'


class JkitepDatashareGrp2Role(models.Model):
    shareid = models.IntegerField(primary_key=True)
    share_groupid = models.IntegerField(blank=True, null=True)
    to_roleid = models.ForeignKey('JkitepRole', models.DO_NOTHING, db_column='to_roleid', blank=True, null=True)
    permission = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_datashare_grp2role'


class JkitepDatashareGrp2Rs(models.Model):
    shareid = models.IntegerField(primary_key=True)
    share_groupid = models.IntegerField(blank=True, null=True)
    to_roleandsubid = models.ForeignKey('JkitepRole', models.DO_NOTHING, db_column='to_roleandsubid', blank=True, null=True)
    permission = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_datashare_grp2rs'


class JkitepDatashareModuleRel(models.Model):
    shareid = models.IntegerField(primary_key=True)
    tabid = models.ForeignKey('JkitepTab', models.DO_NOTHING, db_column='tabid')
    relationtype = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_datashare_module_rel'


class JkitepDatashareModuleRelSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_datashare_module_rel_seq'


class JkitepDatashareRelatedmodulePermission(models.Model):
    shareid = models.IntegerField(primary_key=True)
    datashare_relatedmodule_id = models.IntegerField()
    permission = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_datashare_relatedmodule_permission'
        unique_together = (('shareid', 'datashare_relatedmodule_id'),)


class JkitepDatashareRelatedmodules(models.Model):
    datashare_relatedmodule_id = models.IntegerField(primary_key=True)
    tabid = models.ForeignKey('JkitepTab', models.DO_NOTHING, db_column='tabid', blank=True, null=True)
    relatedto_tabid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_datashare_relatedmodules'


class JkitepDatashareRelatedmodulesSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_datashare_relatedmodules_seq'


class JkitepDatashareRole2Group(models.Model):
    shareid = models.IntegerField(primary_key=True)
    share_roleid = models.ForeignKey('JkitepRole', models.DO_NOTHING, db_column='share_roleid', blank=True, null=True)
    to_groupid = models.IntegerField(blank=True, null=True)
    permission = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_datashare_role2group'


class JkitepDatashareRole2Role(models.Model):
    shareid = models.IntegerField(primary_key=True)
    share_roleid = models.CharField(max_length=255, blank=True, null=True)
    to_roleid = models.ForeignKey('JkitepRole', models.DO_NOTHING, db_column='to_roleid', blank=True, null=True)
    permission = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_datashare_role2role'


class JkitepDatashareRole2Rs(models.Model):
    shareid = models.IntegerField(primary_key=True)
    share_roleid = models.CharField(max_length=255, blank=True, null=True)
    to_roleandsubid = models.ForeignKey('JkitepRole', models.DO_NOTHING, db_column='to_roleandsubid', blank=True, null=True)
    permission = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_datashare_role2rs'


class JkitepDatashareRs2Grp(models.Model):
    shareid = models.IntegerField(primary_key=True)
    share_roleandsubid = models.ForeignKey('JkitepRole', models.DO_NOTHING, db_column='share_roleandsubid', blank=True, null=True)
    to_groupid = models.IntegerField(blank=True, null=True)
    permission = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_datashare_rs2grp'


class JkitepDatashareRs2Role(models.Model):
    shareid = models.IntegerField(primary_key=True)
    share_roleandsubid = models.CharField(max_length=255, blank=True, null=True)
    to_roleid = models.ForeignKey('JkitepRole', models.DO_NOTHING, db_column='to_roleid', blank=True, null=True)
    permission = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_datashare_rs2role'


class JkitepDatashareRs2Rs(models.Model):
    shareid = models.IntegerField(primary_key=True)
    share_roleandsubid = models.CharField(max_length=255, blank=True, null=True)
    to_roleandsubid = models.ForeignKey('JkitepRole', models.DO_NOTHING, db_column='to_roleandsubid', blank=True, null=True)
    permission = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_datashare_rs2rs'


class JkitepDateFormat(models.Model):
    date_formatid = models.AutoField(primary_key=True)
    date_format = models.CharField(max_length=200)
    sortorderid = models.IntegerField()
    presence = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_date_format'


class JkitepDateFormatSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_date_format_seq'


class JkitepDayoftheweek(models.Model):
    dayoftheweekid = models.AutoField(primary_key=True)
    dayoftheweek = models.CharField(max_length=200)
    sortorderid = models.IntegerField(blank=True, null=True)
    presence = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_dayoftheweek'


class JkitepDayoftheweekSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_dayoftheweek_seq'


class JkitepDefOrgField(models.Model):
    tabid = models.IntegerField(blank=True, null=True)
    fieldid = models.IntegerField(primary_key=True)
    visible = models.IntegerField(blank=True, null=True)
    readonly = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_def_org_field'


class JkitepDefOrgShare(models.Model):
    ruleid = models.AutoField(primary_key=True)
    tabid = models.IntegerField()
    permission = models.ForeignKey('JkitepOrgShareActionMapping', models.DO_NOTHING, db_column='permission', blank=True, null=True)
    editstatus = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_def_org_share'


class JkitepDefOrgShareSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_def_org_share_seq'


class JkitepDefaultRecordView(models.Model):
    default_record_viewid = models.AutoField(primary_key=True)
    default_record_view = models.CharField(max_length=200)
    sortorderid = models.IntegerField(blank=True, null=True)
    presence = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_default_record_view'


class JkitepDefaultRecordViewSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_default_record_view_seq'


class JkitepDefaultactivitytype(models.Model):
    defaultactivitytypeid = models.AutoField(primary_key=True)
    defaultactivitytype = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_defaultactivitytype'


class JkitepDefaultactivitytypeSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_defaultactivitytype_seq'


class JkitepDefaultcalendarview(models.Model):
    defaultcalendarviewid = models.AutoField(primary_key=True)
    defaultcalendarview = models.CharField(max_length=200)
    sortorderid = models.IntegerField(blank=True, null=True)
    presence = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_defaultcalendarview'


class JkitepDefaultcalendarviewSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_defaultcalendarview_seq'


class JkitepDefaultcv(models.Model):
    tabid = models.OneToOneField('JkitepTab', models.DO_NOTHING, db_column='tabid', primary_key=True)
    defaultviewname = models.CharField(max_length=50)
    query = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_defaultcv'


class JkitepDefaulteventstatus(models.Model):
    defaulteventstatusid = models.AutoField(primary_key=True)
    defaulteventstatus = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_defaulteventstatus'


class JkitepDefaulteventstatusSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_defaulteventstatus_seq'


class JkitepDiscount(models.Model):
    discountid = models.AutoField(primary_key=True)
    discount = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_discount'


class JkitepDiscountSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_discount_seq'


class JkitepDistrictcityemployees(models.Model):
    districtcityemployeesid = models.IntegerField(primary_key=True)
    district_city_employees_no = models.CharField(max_length=100, blank=True, null=True)
    firstname = models.CharField(max_length=100, blank=True, null=True)
    status_users_emp = models.CharField(max_length=100, blank=True, null=True)
    user_employee_id = models.CharField(max_length=100, blank=True, null=True)
    role_name_emp = models.CharField(max_length=100, blank=True, null=True)
    region_id = models.CharField(max_length=100, blank=True, null=True)
    pin_con = models.CharField(max_length=100, blank=True, null=True)
    lastname = models.CharField(max_length=100, blank=True, null=True)
    patronymic = models.CharField(max_length=100, blank=True, null=True)
    mobile_phone = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    employee_id = models.CharField(max_length=100, blank=True, null=True)
    employees_id_user = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_districtcityemployees'


class JkitepDistrictcityemployeesUserField(models.Model):
    recordid = models.IntegerField()
    userid = models.IntegerField()
    starred = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_districtcityemployees_user_field'


class JkitepDistrictcityemployeescf(models.Model):
    districtcityemployeesid = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'jkitep_districtcityemployeescf'


class JkitepDotype(models.Model):
    dotypeid = models.AutoField(primary_key=True)
    dotype = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_dotype'


class JkitepDotypeSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_dotype_seq'


class JkitepDurationMinutes(models.Model):
    minutesid = models.AutoField(primary_key=True)
    duration_minutes = models.CharField(max_length=200)
    sortorderid = models.IntegerField()
    presence = models.IntegerField()
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_duration_minutes'


class JkitepDurationMinutesSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_duration_minutes_seq'


class JkitepDurationhrs(models.Model):
    hrsid = models.AutoField(primary_key=True)
    hrs = models.CharField(max_length=50, blank=True, null=True)
    sortorderid = models.IntegerField()
    presence = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_durationhrs'


class JkitepDurationmins(models.Model):
    minsid = models.AutoField(primary_key=True)
    mins = models.CharField(max_length=50, blank=True, null=True)
    sortorderid = models.IntegerField()
    presence = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_durationmins'


class JkitepEmailAccess(models.Model):
    crmid = models.IntegerField(blank=True, null=True)
    mailid = models.IntegerField(blank=True, null=True)
    accessdate = models.DateField(blank=True, null=True)
    accesstime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_email_access'


class JkitepEmailTrack(models.Model):
    crmid = models.IntegerField(blank=True, null=True)
    mailid = models.IntegerField(blank=True, null=True)
    access_count = models.IntegerField(blank=True, null=True)
    click_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_email_track'
        unique_together = (('crmid', 'mailid'),)


class JkitepEmaildetails(models.Model):
    emailid = models.IntegerField(primary_key=True)
    from_email = models.CharField(max_length=50)
    to_email = models.TextField(blank=True, null=True)
    cc_email = models.TextField(blank=True, null=True)
    bcc_email = models.TextField(blank=True, null=True)
    assigned_user_email = models.CharField(max_length=50)
    idlists = models.TextField(blank=True, null=True)
    email_flag = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'jkitep_emaildetails'


class JkitepEmailsRecipientprefs(models.Model):
    tabid = models.IntegerField()
    prefs = models.CharField(max_length=255, blank=True, null=True)
    userid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_emails_recipientprefs'


class JkitepEmailslookup(models.Model):
    crmid = models.ForeignKey(JkitepCrmentity, models.DO_NOTHING, db_column='crmid', blank=True, null=True)
    setype = models.CharField(max_length=100, blank=True, null=True)
    value = models.CharField(max_length=100, blank=True, null=True)
    fieldid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_emailslookup'
        unique_together = (('crmid', 'setype', 'fieldid'),)


class JkitepEmailtemplates(models.Model):
    foldername = models.CharField(max_length=100, blank=True, null=True)
    templatename = models.CharField(max_length=100, blank=True, null=True)
    templatepath = models.CharField(max_length=100, blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    deleted = models.IntegerField()
    templateid = models.AutoField(primary_key=True)
    systemtemplate = models.IntegerField()
    module = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_emailtemplates'


class JkitepEmailtemplatesSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_emailtemplates_seq'


class JkitepEntityname(models.Model):
    tabid = models.OneToOneField('JkitepTab', models.DO_NOTHING, db_column='tabid', primary_key=True)
    modulename = models.CharField(max_length=100, blank=True, null=True)
    tablename = models.CharField(max_length=100)
    fieldname = models.CharField(max_length=150)
    entityidfield = models.CharField(max_length=150)
    entityidcolumn = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'jkitep_entityname'


class JkitepEventhandlerModule(models.Model):
    eventhandler_module_id = models.AutoField(primary_key=True)
    module_name = models.CharField(max_length=100, blank=True, null=True)
    handler_class = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_eventhandler_module'


class JkitepEventhandlerModuleSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_eventhandler_module_seq'


class JkitepEventhandlers(models.Model):
    eventhandler_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=100)
    handler_path = models.CharField(max_length=400)
    handler_class = models.CharField(max_length=100)
    cond = models.TextField(blank=True, null=True)
    is_active = models.IntegerField()
    dependent_on = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_eventhandlers'
        unique_together = (('eventhandler_id', 'event_name', 'handler_class'),)


class JkitepEventhandlersSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_eventhandlers_seq'


class JkitepEventstatus(models.Model):
    eventstatusid = models.AutoField(primary_key=True)
    eventstatus = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_eventstatus'


class JkitepEventstatusSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_eventstatus_seq'


class JkitepExpectedresponse(models.Model):
    expectedresponseid = models.AutoField(primary_key=True)
    expectedresponse = models.CharField(unique=True, max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_expectedresponse'


class JkitepExpectedresponseSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_expectedresponse_seq'


class JkitepExtnstoreUsers(models.Model):
    username = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=75, blank=True, null=True)
    instanceurl = models.CharField(max_length=255, blank=True, null=True)
    createdon = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_extnstore_users'


class JkitepFaq(models.Model):
    id = models.OneToOneField(JkitepCrmentity, models.DO_NOTHING, db_column='id', primary_key=True)
    faq_no = models.CharField(max_length=100)
    product_id = models.CharField(max_length=100, blank=True, null=True)
    question = models.TextField(blank=True, null=True)
    answer = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    tags = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_faq'


class JkitepFaqcategories(models.Model):
    faqcategories_id = models.AutoField(primary_key=True)
    faqcategories = models.CharField(max_length=200, blank=True, null=True)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_faqcategories'


class JkitepFaqcategoriesSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_faqcategories_seq'


class JkitepFaqcf(models.Model):
    faqid = models.OneToOneField(JkitepFaq, models.DO_NOTHING, db_column='faqid', primary_key=True)

    class Meta:
        managed = False
        db_table = 'jkitep_faqcf'


class JkitepFaqcomments(models.Model):
    commentid = models.AutoField(primary_key=True)
    faqid = models.ForeignKey(JkitepFaq, models.DO_NOTHING, db_column='faqid', blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    createdtime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'jkitep_faqcomments'


class JkitepFaqstatus(models.Model):
    faqstatus_id = models.AutoField(primary_key=True)
    faqstatus = models.CharField(max_length=200, blank=True, null=True)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_faqstatus'


class JkitepFaqstatusSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_faqstatus_seq'


class JkitepFeedback(models.Model):
    userid = models.IntegerField(blank=True, null=True)
    dontshow = models.CharField(max_length=19, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_feedback'


class JkitepField(models.Model):
    tabid = models.ForeignKey('JkitepTab', models.DO_NOTHING, db_column='tabid')
    fieldid = models.AutoField(primary_key=True)
    columnname = models.CharField(max_length=63, blank=True, null=True)
    tablename = models.CharField(max_length=100, blank=True, null=True)
    generatedtype = models.IntegerField()
    uitype = models.CharField(max_length=30)
    fieldname = models.CharField(max_length=50)
    fieldlabel = models.CharField(max_length=50)
    readonly = models.IntegerField()
    presence = models.IntegerField()
    defaultvalue = models.TextField(blank=True, null=True)
    maximumlength = models.IntegerField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    block = models.IntegerField(blank=True, null=True)
    displaytype = models.IntegerField(blank=True, null=True)
    typeofdata = models.CharField(max_length=100, blank=True, null=True)
    quickcreate = models.IntegerField()
    quickcreatesequence = models.IntegerField(blank=True, null=True)
    info_type = models.CharField(max_length=20, blank=True, null=True)
    masseditable = models.IntegerField()
    helpinfo = models.TextField(blank=True, null=True)
    summaryfield = models.IntegerField()
    headerfield = models.IntegerField(blank=True, null=True)
    isunique = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_field'


class JkitepFieldSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_field_seq'


class JkitepFieldmodulerel(models.Model):
    fieldid = models.IntegerField()
    module = models.CharField(max_length=100)
    relmodule = models.CharField(max_length=100)
    status = models.CharField(max_length=10, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_fieldmodulerel'


class JkitepFreetaggedObjects(models.Model):
    tag_id = models.IntegerField(primary_key=True)
    tagger_id = models.IntegerField()
    object_id = models.IntegerField()
    tagged_on = models.DateTimeField()
    module = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_freetagged_objects'
        unique_together = (('tag_id', 'tagger_id', 'object_id'),)


class JkitepFreetags(models.Model):
    id = models.IntegerField(primary_key=True)
    tag = models.CharField(max_length=50)
    raw_tag = models.CharField(max_length=50)
    visibility = models.CharField(max_length=100)
    owner = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_freetags'


class JkitepFreetagsSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_freetags_seq'


class JkitepGender(models.Model):
    genderid = models.AutoField(primary_key=True)
    gender = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_gender'


class JkitepGenderSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_gender_seq'


class JkitepGlacct(models.Model):
    glacctid = models.AutoField(primary_key=True)
    glacct = models.CharField(unique=True, max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_glacct'


class JkitepGlacctSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_glacct_seq'


class JkitepGoogleEventCalendarMapping(models.Model):
    event_id = models.CharField(max_length=255, blank=True, null=True)
    calendar_id = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_google_event_calendar_mapping'


class JkitepGoogleOauth2(models.Model):
    service = models.CharField(max_length=20, blank=True, null=True)
    access_token = models.CharField(max_length=500, blank=True, null=True)
    refresh_token = models.CharField(max_length=500, blank=True, null=True)
    userid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_google_oauth2'


class JkitepGoogleSyncFieldmapping(models.Model):
    jkitep_field = models.CharField(max_length=255, blank=True, null=True)
    google_field = models.CharField(max_length=255, blank=True, null=True)
    google_field_type = models.CharField(max_length=255, blank=True, null=True)
    google_custom_label = models.CharField(max_length=255, blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_google_sync_fieldmapping'


class JkitepGoogleSyncLocalization(models.Model):
    id = models.IntegerField(primary_key=True)
    field_name = models.CharField(max_length=150)
    original_field_type = models.CharField(max_length=150, blank=True, null=True)
    russian_field_type = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_google_sync_localization'


class JkitepGoogleSyncSettings(models.Model):
    user = models.IntegerField(blank=True, null=True)
    module = models.CharField(max_length=50, blank=True, null=True)
    clientgroup = models.CharField(max_length=255, blank=True, null=True)
    direction = models.CharField(max_length=50, blank=True, null=True)
    enabled = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_google_sync_settings'


class JkitepGroup2Grouprel(models.Model):
    groupid = models.OneToOneField('JkitepGroups', models.DO_NOTHING, db_column='groupid', primary_key=True)
    containsgroupid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_group2grouprel'
        unique_together = (('groupid', 'containsgroupid'),)


class JkitepGroup2Role(models.Model):
    groupid = models.IntegerField(primary_key=True)
    roleid = models.ForeignKey('JkitepRole', models.DO_NOTHING, db_column='roleid')

    class Meta:
        managed = False
        db_table = 'jkitep_group2role'
        unique_together = (('groupid', 'roleid'),)


class JkitepGroup2Rs(models.Model):
    groupid = models.IntegerField(primary_key=True)
    roleandsubid = models.ForeignKey('JkitepRole', models.DO_NOTHING, db_column='roleandsubid')

    class Meta:
        managed = False
        db_table = 'jkitep_group2rs'
        unique_together = (('groupid', 'roleandsubid'),)


class JkitepGroups(models.Model):
    groupid = models.IntegerField(primary_key=True)
    groupname = models.CharField(unique=True, max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_groups'


class JkitepHelps(models.Model):
    helpsid = models.IntegerField(primary_key=True)
    help_no = models.CharField(max_length=100, blank=True, null=True)
    hname = models.CharField(max_length=100, blank=True, null=True)
    htheme = models.CharField(max_length=100, blank=True, null=True)
    lang_helps = models.CharField(max_length=100, blank=True, null=True)
    video_help = models.CharField(max_length=100, blank=True, null=True)
    audit_help = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_helps'


class JkitepHelpsUserField(models.Model):
    recordid = models.IntegerField()
    userid = models.IntegerField()
    starred = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_helps_user_field'


class JkitepHelpscf(models.Model):
    helpsid = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'jkitep_helpscf'


class JkitepHomeLayout(models.Model):
    userid = models.IntegerField(primary_key=True)
    layout = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_home_layout'


class JkitepHomedashbd(models.Model):
    stuffid = models.OneToOneField('JkitepHomestuff', models.DO_NOTHING, db_column='stuffid', primary_key=True)
    dashbdname = models.CharField(max_length=100, blank=True, null=True)
    dashbdtype = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_homedashbd'


class JkitepHomedefault(models.Model):
    stuffid = models.OneToOneField('JkitepHomestuff', models.DO_NOTHING, db_column='stuffid', primary_key=True)
    hometype = models.CharField(max_length=30)
    maxentries = models.IntegerField(blank=True, null=True)
    setype = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_homedefault'


class JkitepHomemodule(models.Model):
    stuffid = models.OneToOneField('JkitepHomestuff', models.DO_NOTHING, db_column='stuffid', primary_key=True)
    modulename = models.CharField(max_length=100, blank=True, null=True)
    maxentries = models.IntegerField()
    customviewid = models.IntegerField()
    setype = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'jkitep_homemodule'


class JkitepHomemoduleflds(models.Model):
    stuffid = models.ForeignKey(JkitepHomemodule, models.DO_NOTHING, db_column='stuffid', blank=True, null=True)
    fieldname = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_homemoduleflds'


class JkitepHomereportchart(models.Model):
    stuffid = models.IntegerField(primary_key=True)
    reportid = models.IntegerField(blank=True, null=True)
    reportcharttype = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_homereportchart'


class JkitepHomerss(models.Model):
    stuffid = models.OneToOneField('JkitepHomestuff', models.DO_NOTHING, db_column='stuffid', primary_key=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    maxentries = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_homerss'


class JkitepHomestuff(models.Model):
    stuffid = models.IntegerField(primary_key=True)
    stuffsequence = models.IntegerField()
    stufftype = models.CharField(max_length=100, blank=True, null=True)
    userid = models.ForeignKey('JkitepUsers', models.DO_NOTHING, db_column='userid')
    visible = models.IntegerField()
    stufftitle = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_homestuff'


class JkitepHomestuffSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_homestuff_seq'


class JkitepHourFormat(models.Model):
    hour_formatid = models.AutoField(primary_key=True)
    hour_format = models.CharField(max_length=200)
    sortorderid = models.IntegerField(blank=True, null=True)
    presence = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_hour_format'


class JkitepHourFormatSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_hour_format_seq'


class JkitepHtheme(models.Model):
    hthemeid = models.AutoField(primary_key=True)
    htheme = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_htheme'


class JkitepHthemeSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_htheme_seq'


class JkitepImportLocks(models.Model):
    jkitep_import_lock_id = models.IntegerField(primary_key=True)
    userid = models.IntegerField()
    tabid = models.IntegerField()
    importid = models.IntegerField()
    locked_since = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_import_locks'


class JkitepImportMaps(models.Model):
    name = models.CharField(max_length=36)
    module = models.CharField(max_length=36)
    content = models.TextField(blank=True, null=True)
    has_header = models.IntegerField()
    deleted = models.IntegerField()
    date_entered = models.DateTimeField()
    date_modified = models.DateTimeField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    is_published = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'jkitep_import_maps'


class JkitepImportQueue(models.Model):
    importid = models.IntegerField(primary_key=True)
    userid = models.IntegerField()
    tabid = models.IntegerField()
    field_mapping = models.TextField(blank=True, null=True)
    default_values = models.TextField(blank=True, null=True)
    merge_type = models.IntegerField(blank=True, null=True)
    merge_fields = models.TextField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    lineitem_currency_id = models.IntegerField(blank=True, null=True)
    paging = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_import_queue'


class JkitepIndustry(models.Model):
    industryid = models.AutoField(primary_key=True)
    industry = models.CharField(unique=True, max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_industry'


class JkitepIndustrySeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_industry_seq'


class JkitepIntspeed(models.Model):
    intspeedid = models.AutoField(primary_key=True)
    intspeed = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_intspeed'


class JkitepIntspeedSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_intspeed_seq'


class JkitepInttype(models.Model):
    inttypeid = models.AutoField(primary_key=True)
    inttype = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_inttype'


class JkitepInttypeSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_inttype_seq'


class JkitepInventoryTandc(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=30)
    tandc = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_inventory_tandc'


class JkitepInventoryTandcSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_inventory_tandc_seq'


class JkitepInventorycharges(models.Model):
    chargeid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    format = models.CharField(max_length=10, blank=True, null=True)
    type = models.CharField(max_length=10, blank=True, null=True)
    value = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)
    regions = models.TextField(blank=True, null=True)
    istaxable = models.IntegerField()
    taxes = models.CharField(max_length=1024, blank=True, null=True)
    deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_inventorycharges'


class JkitepInventorychargesrel(models.Model):
    recordid = models.IntegerField()
    charges = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_inventorychargesrel'


class JkitepInventorynotification(models.Model):
    notificationid = models.AutoField(primary_key=True)
    notificationname = models.CharField(max_length=200, blank=True, null=True)
    notificationsubject = models.CharField(max_length=200, blank=True, null=True)
    notificationbody = models.TextField(blank=True, null=True)
    label = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_inventorynotification'


class JkitepInventorynotificationSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_inventorynotification_seq'


class JkitepInventoryproductrel(models.Model):
    id = models.ForeignKey(JkitepCrmentity, models.DO_NOTHING, db_column='id', blank=True, null=True)
    productid = models.IntegerField(blank=True, null=True)
    sequence_no = models.IntegerField(blank=True, null=True)
    quantity = models.DecimalField(max_digits=25, decimal_places=3, blank=True, null=True)
    listprice = models.DecimalField(max_digits=27, decimal_places=8, blank=True, null=True)
    discount_percent = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    discount_amount = models.DecimalField(max_digits=27, decimal_places=8, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    incrementondel = models.IntegerField()
    lineitem_id = models.AutoField(primary_key=True)
    tax1 = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    tax2 = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    tax3 = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    image = models.CharField(max_length=2, blank=True, null=True)
    purchase_cost = models.DecimalField(max_digits=27, decimal_places=8, blank=True, null=True)
    margin = models.DecimalField(max_digits=27, decimal_places=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_inventoryproductrel'


class JkitepInventoryproductrelSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_inventoryproductrel_seq'


class JkitepInventoryshippingrel(models.Model):
    id = models.IntegerField(blank=True, null=True)
    shtax1 = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    shtax2 = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    shtax3 = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_inventoryshippingrel'


class JkitepInventorysubproductrel(models.Model):
    id = models.IntegerField()
    sequence_no = models.IntegerField()
    productid = models.IntegerField()
    quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_inventorysubproductrel'


class JkitepInventorytaxinfo(models.Model):
    taxid = models.IntegerField(primary_key=True)
    taxname = models.CharField(max_length=50, blank=True, null=True)
    taxlabel = models.CharField(max_length=50, blank=True, null=True)
    percentage = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    method = models.CharField(max_length=10, blank=True, null=True)
    type = models.CharField(max_length=10, blank=True, null=True)
    compoundon = models.CharField(max_length=400, blank=True, null=True)
    regions = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_inventorytaxinfo'


class JkitepInventorytaxinfoSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_inventorytaxinfo_seq'


class JkitepInvitees(models.Model):
    activityid = models.IntegerField(primary_key=True)
    inviteeid = models.IntegerField()
    status = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_invitees'
        unique_together = (('activityid', 'inviteeid'),)


class JkitepInvoice(models.Model):
    invoiceid = models.OneToOneField(JkitepCrmentity, models.DO_NOTHING, db_column='invoiceid', primary_key=True)
    subject = models.CharField(max_length=100, blank=True, null=True)
    salesorderid = models.ForeignKey('JkitepSalesorder', models.DO_NOTHING, db_column='salesorderid', blank=True, null=True)
    customerno = models.CharField(max_length=100, blank=True, null=True)
    contactid = models.IntegerField(blank=True, null=True)
    notes = models.CharField(max_length=100, blank=True, null=True)
    invoicedate = models.DateField(blank=True, null=True)
    duedate = models.DateField(blank=True, null=True)
    invoiceterms = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    adjustment = models.DecimalField(max_digits=25, decimal_places=8, blank=True, null=True)
    salescommission = models.DecimalField(max_digits=25, decimal_places=3, blank=True, null=True)
    exciseduty = models.DecimalField(max_digits=25, decimal_places=3, blank=True, null=True)
    subtotal = models.DecimalField(max_digits=25, decimal_places=8, blank=True, null=True)
    total = models.DecimalField(max_digits=25, decimal_places=8, blank=True, null=True)
    taxtype = models.CharField(max_length=25, blank=True, null=True)
    discount_percent = models.DecimalField(max_digits=25, decimal_places=3, blank=True, null=True)
    discount_amount = models.DecimalField(max_digits=25, decimal_places=8, blank=True, null=True)
    s_h_amount = models.DecimalField(max_digits=25, decimal_places=8, blank=True, null=True)
    shipping = models.CharField(max_length=100, blank=True, null=True)
    accountid = models.IntegerField(blank=True, null=True)
    terms_conditions = models.TextField(blank=True, null=True)
    purchaseorder = models.CharField(max_length=200, blank=True, null=True)
    invoicestatus = models.CharField(max_length=200, blank=True, null=True)
    invoice_no = models.CharField(max_length=100, blank=True, null=True)
    currency_id = models.IntegerField()
    conversion_rate = models.DecimalField(max_digits=10, decimal_places=3)
    compound_taxes_info = models.TextField(blank=True, null=True)
    sp_act_id = models.IntegerField(blank=True, null=True)
    pre_tax_total = models.DecimalField(max_digits=25, decimal_places=8, blank=True, null=True)
    received = models.DecimalField(max_digits=25, decimal_places=8, blank=True, null=True)
    balance = models.DecimalField(max_digits=25, decimal_places=8, blank=True, null=True)
    s_h_percent = models.DecimalField(max_digits=25, decimal_places=8, blank=True, null=True)
    spcompany = models.CharField(max_length=200, blank=True, null=True)
    potential_id = models.CharField(max_length=100, blank=True, null=True)
    tags = models.CharField(max_length=1, blank=True, null=True)
    region_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_invoice'


class JkitepInvoiceRecurringInfo(models.Model):
    salesorderid = models.OneToOneField('JkitepSalesorder', models.DO_NOTHING, db_column='salesorderid', primary_key=True)
    recurring_frequency = models.CharField(max_length=200, blank=True, null=True)
    start_period = models.DateField(blank=True, null=True)
    end_period = models.DateField(blank=True, null=True)
    last_recurring_date = models.DateField(blank=True, null=True)
    payment_duration = models.CharField(max_length=200, blank=True, null=True)
    invoice_status = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_invoice_recurring_info'


class JkitepInvoicebillads(models.Model):
    invoicebilladdressid = models.OneToOneField(JkitepInvoice, models.DO_NOTHING, db_column='invoicebilladdressid', primary_key=True)
    bill_city = models.CharField(max_length=30, blank=True, null=True)
    bill_code = models.CharField(max_length=30, blank=True, null=True)
    bill_country = models.CharField(max_length=30, blank=True, null=True)
    bill_state = models.CharField(max_length=30, blank=True, null=True)
    bill_street = models.CharField(max_length=250, blank=True, null=True)
    bill_pobox = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_invoicebillads'


class JkitepInvoicecf(models.Model):
    invoiceid = models.OneToOneField(JkitepInvoice, models.DO_NOTHING, db_column='invoiceid', primary_key=True)

    class Meta:
        managed = False
        db_table = 'jkitep_invoicecf'


class JkitepInvoiceshipads(models.Model):
    invoiceshipaddressid = models.OneToOneField(JkitepInvoice, models.DO_NOTHING, db_column='invoiceshipaddressid', primary_key=True)
    ship_city = models.CharField(max_length=30, blank=True, null=True)
    ship_code = models.CharField(max_length=30, blank=True, null=True)
    ship_country = models.CharField(max_length=30, blank=True, null=True)
    ship_state = models.CharField(max_length=30, blank=True, null=True)
    ship_street = models.CharField(max_length=250, blank=True, null=True)
    ship_pobox = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_invoiceshipads'


class JkitepInvoicestatus(models.Model):
    invoicestatusid = models.AutoField(primary_key=True)
    invoicestatus = models.CharField(unique=True, max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_invoicestatus'


class JkitepInvoicestatusSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_invoicestatus_seq'


class JkitepInvoicestatushistory(models.Model):
    historyid = models.AutoField(primary_key=True)
    invoiceid = models.ForeignKey(JkitepInvoice, models.DO_NOTHING, db_column='invoiceid')
    accountname = models.CharField(max_length=100, blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    invoicestatus = models.CharField(max_length=200, blank=True, null=True)
    lastmodified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_invoicestatushistory'


class JkitepLangHelps(models.Model):
    lang_helpsid = models.AutoField(primary_key=True)
    lang_helps = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_lang_helps'


class JkitepLangHelpsSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_lang_helps_seq'


class JkitepLangInstrucClass(models.Model):
    lang_instruc_classid = models.AutoField(primary_key=True)
    lang_instruc_class = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_lang_instruc_class'


class JkitepLangInstrucClassSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_lang_instruc_class_seq'


class JkitepLanguage(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    prefix = models.CharField(max_length=10, blank=True, null=True)
    label = models.CharField(max_length=30, blank=True, null=True)
    lastupdated = models.DateTimeField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    isdefault = models.IntegerField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_language'


class JkitepLanguageInstruction(models.Model):
    language_instructionid = models.AutoField(primary_key=True)
    language_instruction = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_language_instruction'


class JkitepLanguageInstructionSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_language_instruction_seq'


class JkitepLanguageSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_language_seq'


class JkitepLawtype(models.Model):
    lawtypeid = models.AutoField(primary_key=True)
    lawtype = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_lawtype'


class JkitepLawtypeSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_lawtype_seq'


class JkitepLeadView(models.Model):
    lead_viewid = models.AutoField(primary_key=True)
    lead_view = models.CharField(max_length=200)
    sortorderid = models.IntegerField()
    presence = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_lead_view'


class JkitepLeadViewSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_lead_view_seq'


class JkitepLeadaddress(models.Model):
    leadaddressid = models.OneToOneField('JkitepLeaddetails', models.DO_NOTHING, db_column='leadaddressid', primary_key=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    code = models.CharField(max_length=30, blank=True, null=True)
    state = models.CharField(max_length=30, blank=True, null=True)
    pobox = models.CharField(max_length=30, blank=True, null=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    mobile = models.CharField(max_length=50, blank=True, null=True)
    fax = models.CharField(max_length=50, blank=True, null=True)
    lane = models.CharField(max_length=250, blank=True, null=True)
    leadaddresstype = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_leadaddress'


class JkitepLeaddetails(models.Model):
    leadid = models.OneToOneField(JkitepCrmentity, models.DO_NOTHING, db_column='leadid', primary_key=True)
    lead_no = models.CharField(max_length=100)
    email = models.CharField(max_length=100, blank=True, null=True)
    interest = models.CharField(max_length=50, blank=True, null=True)
    firstname = models.CharField(max_length=40, blank=True, null=True)
    salutation = models.CharField(max_length=200, blank=True, null=True)
    lastname = models.CharField(max_length=80)
    company = models.CharField(max_length=100)
    annualrevenue = models.DecimalField(max_digits=25, decimal_places=8, blank=True, null=True)
    industry = models.CharField(max_length=200, blank=True, null=True)
    campaign = models.CharField(max_length=30, blank=True, null=True)
    rating = models.CharField(max_length=200, blank=True, null=True)
    leadstatus = models.CharField(max_length=200, blank=True, null=True)
    leadsource = models.CharField(max_length=200, blank=True, null=True)
    converted = models.IntegerField(blank=True, null=True)
    designation = models.CharField(max_length=50, blank=True, null=True)
    licencekeystatus = models.CharField(max_length=50, blank=True, null=True)
    space = models.CharField(max_length=250, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    priority = models.CharField(max_length=50, blank=True, null=True)
    demorequest = models.CharField(max_length=50, blank=True, null=True)
    partnercontact = models.CharField(max_length=50, blank=True, null=True)
    productversion = models.CharField(max_length=20, blank=True, null=True)
    product = models.CharField(max_length=50, blank=True, null=True)
    maildate = models.DateField(blank=True, null=True)
    nextstepdate = models.DateField(blank=True, null=True)
    fundingsituation = models.CharField(max_length=50, blank=True, null=True)
    purpose = models.CharField(max_length=50, blank=True, null=True)
    evaluationstatus = models.CharField(max_length=50, blank=True, null=True)
    transferdate = models.DateField(blank=True, null=True)
    revenuetype = models.CharField(max_length=50, blank=True, null=True)
    noofemployees = models.IntegerField(blank=True, null=True)
    secondaryemail = models.CharField(max_length=100, blank=True, null=True)
    assignleadchk = models.IntegerField(blank=True, null=True)
    splastsms = models.DateTimeField(blank=True, null=True)
    emailoptout = models.CharField(max_length=3, blank=True, null=True)
    tags = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_leaddetails'


class JkitepLeadscf(models.Model):
    leadid = models.OneToOneField(JkitepLeaddetails, models.DO_NOTHING, db_column='leadid', primary_key=True)
    vk_url = models.CharField(max_length=155, blank=True, null=True)
    tw_url = models.CharField(max_length=155, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_leadscf'


class JkitepLeadsource(models.Model):
    leadsourceid = models.AutoField(primary_key=True)
    leadsource = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_leadsource'


class JkitepLeadsourceSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_leadsource_seq'


class JkitepLeadstage(models.Model):
    leadstageid = models.AutoField(primary_key=True)
    stage = models.CharField(unique=True, max_length=200)
    sortorderid = models.IntegerField()
    presence = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_leadstage'


class JkitepLeadstatus(models.Model):
    leadstatusid = models.AutoField(primary_key=True)
    leadstatus = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_leadstatus'


class JkitepLeadstatusSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_leadstatus_seq'


class JkitepLeadsubdetails(models.Model):
    leadsubscriptionid = models.OneToOneField(JkitepLeaddetails, models.DO_NOTHING, db_column='leadsubscriptionid', primary_key=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    callornot = models.IntegerField(blank=True, null=True)
    readornot = models.IntegerField(blank=True, null=True)
    empct = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_leadsubdetails'


class JkitepLinks(models.Model):
    linkid = models.IntegerField(primary_key=True)
    tabid = models.IntegerField(blank=True, null=True)
    linktype = models.CharField(max_length=50, blank=True, null=True)
    linklabel = models.CharField(max_length=50, blank=True, null=True)
    linkurl = models.CharField(max_length=255, blank=True, null=True)
    linkicon = models.CharField(max_length=100, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    handler_path = models.CharField(max_length=128, blank=True, null=True)
    handler_class = models.CharField(max_length=50, blank=True, null=True)
    handler = models.CharField(max_length=50, blank=True, null=True)
    parent_link = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_links'


class JkitepLinksSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_links_seq'


class JkitepLoginhistory(models.Model):
    login_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_ip = models.CharField(max_length=25)
    logout_time = models.DateTimeField()
    login_time = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_loginhistory'


class JkitepMailAccounts(models.Model):
    account_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    display_name = models.CharField(max_length=50, blank=True, null=True)
    mail_id = models.CharField(max_length=50, blank=True, null=True)
    account_name = models.CharField(max_length=50, blank=True, null=True)
    mail_protocol = models.CharField(max_length=20, blank=True, null=True)
    mail_username = models.CharField(max_length=50)
    mail_password = models.TextField(blank=True, null=True)
    mail_servername = models.CharField(max_length=50, blank=True, null=True)
    box_refresh = models.IntegerField(blank=True, null=True)
    mails_per_page = models.IntegerField(blank=True, null=True)
    ssltype = models.CharField(max_length=50, blank=True, null=True)
    sslmeth = models.CharField(max_length=50, blank=True, null=True)
    int_mailer = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    set_default = models.IntegerField(blank=True, null=True)
    sent_folder = models.CharField(max_length=50, blank=True, null=True)
    trash_folder = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_mail_accounts'


class JkitepMailerQueue(models.Model):
    id = models.IntegerField(primary_key=True)
    fromname = models.CharField(max_length=100, blank=True, null=True)
    fromemail = models.CharField(max_length=100, blank=True, null=True)
    mailer = models.CharField(max_length=10, blank=True, null=True)
    content_type = models.CharField(max_length=15, blank=True, null=True)
    subject = models.CharField(max_length=999, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    relcrmid = models.IntegerField(blank=True, null=True)
    failed = models.IntegerField()
    failreason = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_mailer_queue'


class JkitepMailerQueueattachments(models.Model):
    id = models.IntegerField(blank=True, null=True)
    path = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    encoding = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_mailer_queueattachments'


class JkitepMailerQueueinfo(models.Model):
    id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_mailer_queueinfo'


class JkitepMailmanagerMailattachments(models.Model):
    userid = models.IntegerField(blank=True, null=True)
    muid = models.IntegerField(blank=True, null=True)
    aname = models.CharField(max_length=100, blank=True, null=True)
    lastsavedtime = models.IntegerField(blank=True, null=True)
    attachid = models.IntegerField()
    path = models.CharField(max_length=200)
    cid = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_mailmanager_mailattachments'


class JkitepMailmanagerMailrecord(models.Model):
    userid = models.IntegerField(blank=True, null=True)
    mfrom = models.CharField(max_length=255, blank=True, null=True)
    mto = models.CharField(max_length=255, blank=True, null=True)
    mcc = models.CharField(max_length=500, blank=True, null=True)
    mbcc = models.CharField(max_length=500, blank=True, null=True)
    mdate = models.CharField(max_length=20, blank=True, null=True)
    msubject = models.CharField(max_length=500, blank=True, null=True)
    mbody = models.TextField(blank=True, null=True)
    mcharset = models.CharField(max_length=10, blank=True, null=True)
    misbodyhtml = models.IntegerField(blank=True, null=True)
    mplainmessage = models.IntegerField(blank=True, null=True)
    mhtmlmessage = models.IntegerField(blank=True, null=True)
    muniqueid = models.CharField(max_length=500, blank=True, null=True)
    mbodyparsed = models.IntegerField(blank=True, null=True)
    muid = models.IntegerField(blank=True, null=True)
    lastsavedtime = models.IntegerField(blank=True, null=True)
    folder = models.CharField(max_length=250, blank=True, null=True)
    mfolder = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_mailmanager_mailrecord'


class JkitepMailmanagerMailrel(models.Model):
    mailuid = models.CharField(max_length=999, blank=True, null=True)
    crmid = models.IntegerField(blank=True, null=True)
    emailid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_mailmanager_mailrel'


class JkitepMailscanner(models.Model):
    scannerid = models.AutoField(primary_key=True)
    scannername = models.CharField(max_length=30, blank=True, null=True)
    server = models.CharField(max_length=100, blank=True, null=True)
    protocol = models.CharField(max_length=10, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    ssltype = models.CharField(max_length=10, blank=True, null=True)
    sslmethod = models.CharField(max_length=30, blank=True, null=True)
    connecturl = models.CharField(max_length=255, blank=True, null=True)
    searchfor = models.CharField(max_length=10, blank=True, null=True)
    markas = models.CharField(max_length=10, blank=True, null=True)
    isvalid = models.IntegerField(blank=True, null=True)
    scanfrom = models.CharField(max_length=10, blank=True, null=True)
    time_zone = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_mailscanner'


class JkitepMailscannerActions(models.Model):
    actionid = models.AutoField(primary_key=True)
    scannerid = models.IntegerField(blank=True, null=True)
    actiontype = models.CharField(max_length=10, blank=True, null=True)
    module = models.CharField(max_length=30, blank=True, null=True)
    lookup = models.CharField(max_length=30, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_mailscanner_actions'


class JkitepMailscannerFolders(models.Model):
    folderid = models.AutoField(primary_key=True)
    scannerid = models.IntegerField(blank=True, null=True)
    foldername = models.CharField(max_length=255, blank=True, null=True)
    lastscan = models.CharField(max_length=30, blank=True, null=True)
    rescan = models.IntegerField(blank=True, null=True)
    enabled = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_mailscanner_folders'


class JkitepMailscannerIds(models.Model):
    scannerid = models.IntegerField(blank=True, null=True)
    messageid = models.CharField(max_length=512, blank=True, null=True)
    crmid = models.IntegerField(blank=True, null=True)
    refids = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_mailscanner_ids'


class JkitepMailscannerRuleactions(models.Model):
    ruleid = models.IntegerField(blank=True, null=True)
    actionid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_mailscanner_ruleactions'


class JkitepMailscannerRules(models.Model):
    ruleid = models.AutoField(primary_key=True)
    scannerid = models.IntegerField(blank=True, null=True)
    fromaddress = models.CharField(max_length=255, blank=True, null=True)
    toaddress = models.CharField(max_length=255, blank=True, null=True)
    subjectop = models.CharField(max_length=20, blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    bodyop = models.CharField(max_length=20, blank=True, null=True)
    body = models.CharField(max_length=255, blank=True, null=True)
    matchusing = models.CharField(max_length=5, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    assigned_to = models.IntegerField(blank=True, null=True)
    cc = models.CharField(max_length=255, blank=True, null=True)
    bcc = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_mailscanner_rules'


class JkitepManufacturer(models.Model):
    manufacturerid = models.AutoField(primary_key=True)
    manufacturer = models.CharField(unique=True, max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_manufacturer'


class JkitepManufacturerSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_manufacturer_seq'


class JkitepMobileAlerts(models.Model):
    handler_path = models.CharField(max_length=500, blank=True, null=True)
    handler_class = models.CharField(max_length=50, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_mobile_alerts'


class JkitepModcomments(models.Model):
    modcommentsid = models.ForeignKey(JkitepCrmentity, models.DO_NOTHING, db_column='modcommentsid', blank=True, null=True)
    commentcontent = models.TextField(blank=True, null=True)
    related_to = models.IntegerField(blank=True, null=True)
    parent_comments = models.IntegerField(blank=True, null=True)
    customer = models.IntegerField(blank=True, null=True)
    userid = models.IntegerField(blank=True, null=True)
    reasontoedit = models.CharField(max_length=100, blank=True, null=True)
    is_private = models.IntegerField(blank=True, null=True)
    filename = models.CharField(max_length=255, blank=True, null=True)
    related_email_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_modcomments'


class JkitepModcommentscf(models.Model):
    modcommentsid = models.OneToOneField(JkitepModcomments, models.DO_NOTHING, db_column='modcommentsid', primary_key=True)

    class Meta:
        managed = False
        db_table = 'jkitep_modcommentscf'


class JkitepModentityNum(models.Model):
    num_id = models.IntegerField(primary_key=True)
    semodule = models.CharField(max_length=100, blank=True, null=True)
    prefix = models.CharField(max_length=50)
    start_id = models.CharField(max_length=50)
    cur_id = models.CharField(max_length=50)
    active = models.CharField(max_length=2)
    spcompany = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_modentity_num'


class JkitepModentityNumSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_modentity_num_seq'


class JkitepModtrackerBasic(models.Model):
    id = models.IntegerField(primary_key=True)
    crmid = models.IntegerField(blank=True, null=True)
    module = models.CharField(max_length=50, blank=True, null=True)
    whodid = models.IntegerField(blank=True, null=True)
    changedon = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_modtracker_basic'


class JkitepModtrackerBasicSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_modtracker_basic_seq'


class JkitepModtrackerDetail(models.Model):
    id = models.IntegerField(blank=True, null=True)
    fieldname = models.CharField(max_length=100, blank=True, null=True)
    prevalue = models.TextField(blank=True, null=True)
    postvalue = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_modtracker_detail'


class JkitepModtrackerRelations(models.Model):
    id = models.IntegerField(primary_key=True)
    targetmodule = models.CharField(max_length=100)
    targetid = models.IntegerField()
    changedon = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_modtracker_relations'


class JkitepModtrackerTabs(models.Model):
    tabid = models.IntegerField(primary_key=True)
    visible = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_modtracker_tabs'


class JkitepModuleDashboardWidgets(models.Model):
    linkid = models.IntegerField(blank=True, null=True)
    userid = models.IntegerField(blank=True, null=True)
    filterid = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    position = models.CharField(max_length=50, blank=True, null=True)
    reportid = models.IntegerField(blank=True, null=True)
    dashboardtabid = models.ForeignKey(JkitepDashboardTabs, models.DO_NOTHING, db_column='dashboardtabid', blank=True, null=True)
    size = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_module_dashboard_widgets'


class JkitepNoOfCurrencyDecimals(models.Model):
    no_of_currency_decimalsid = models.AutoField(primary_key=True)
    no_of_currency_decimals = models.CharField(max_length=200)
    sortorderid = models.IntegerField(blank=True, null=True)
    presence = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_no_of_currency_decimals'


class JkitepNoOfCurrencyDecimalsSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_no_of_currency_decimals_seq'


class JkitepNotebookContents(models.Model):
    userid = models.IntegerField()
    notebookid = models.IntegerField()
    contents = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_notebook_contents'


class JkitepNotes(models.Model):
    notesid = models.OneToOneField(JkitepCrmentity, models.DO_NOTHING, db_column='notesid', primary_key=True)
    note_no = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    filename = models.CharField(max_length=200, blank=True, null=True)
    notecontent = models.TextField(blank=True, null=True)
    folderid = models.IntegerField()
    filetype = models.CharField(max_length=50, blank=True, null=True)
    filelocationtype = models.CharField(max_length=5, blank=True, null=True)
    filedownloadcount = models.IntegerField(blank=True, null=True)
    filestatus = models.IntegerField(blank=True, null=True)
    filesize = models.IntegerField()
    fileversion = models.CharField(max_length=50, blank=True, null=True)
    tags = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_notes'


class JkitepNotescf(models.Model):
    notesid = models.OneToOneField(JkitepNotes, models.DO_NOTHING, db_column='notesid', primary_key=True)

    class Meta:
        managed = False
        db_table = 'jkitep_notescf'


class JkitepNotificationscheduler(models.Model):
    schedulednotificationid = models.AutoField(primary_key=True)
    schedulednotificationname = models.CharField(unique=True, max_length=200, blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    notificationsubject = models.CharField(max_length=200, blank=True, null=True)
    notificationbody = models.TextField(blank=True, null=True)
    label = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_notificationscheduler'


class JkitepNotificationschedulerSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_notificationscheduler_seq'


class JkitepOmsu(models.Model):
    omsuid = models.AutoField(primary_key=True)
    omsu = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_omsu'


class JkitepOmsuSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_omsu_seq'


class JkitepOpportunityType(models.Model):
    opptypeid = models.AutoField(primary_key=True)
    opportunity_type = models.CharField(unique=True, max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_opportunity_type'


class JkitepOpportunityTypeSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_opportunity_type_seq'


class JkitepOpportunitystage(models.Model):
    potstageid = models.AutoField(primary_key=True)
    stage = models.CharField(unique=True, max_length=200)
    sortorderid = models.IntegerField()
    presence = models.IntegerField()
    probability = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_opportunitystage'


class JkitepOrgShareAction2Tab(models.Model):
    share_action_id = models.IntegerField(primary_key=True)
    tabid = models.ForeignKey('JkitepTab', models.DO_NOTHING, db_column='tabid')

    class Meta:
        managed = False
        db_table = 'jkitep_org_share_action2tab'
        unique_together = (('share_action_id', 'tabid'),)


class JkitepOrgShareActionMapping(models.Model):
    share_action_id = models.IntegerField(primary_key=True)
    share_action_name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_org_share_action_mapping'


class JkitepOrganizationdetails(models.Model):
    organization_id = models.IntegerField(primary_key=True)
    organizationname = models.CharField(max_length=60, blank=True, null=True)
    address = models.CharField(max_length=150, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    code = models.CharField(max_length=30, blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    fax = models.CharField(max_length=30, blank=True, null=True)
    website = models.CharField(max_length=100, blank=True, null=True)
    logoname = models.CharField(max_length=50, blank=True, null=True)
    logo = models.TextField(blank=True, null=True)
    vatid = models.CharField(max_length=100, blank=True, null=True)
    inn = models.CharField(max_length=30, blank=True, null=True)
    kpp = models.CharField(max_length=30, blank=True, null=True)
    bankaccount = models.CharField(max_length=1024, blank=True, null=True)
    bankname = models.CharField(max_length=1024, blank=True, null=True)
    bankid = models.CharField(max_length=30, blank=True, null=True)
    corraccount = models.CharField(max_length=100, blank=True, null=True)
    director = models.CharField(max_length=100, blank=True, null=True)
    bookkeeper = models.CharField(max_length=100, blank=True, null=True)
    entrepreneur = models.CharField(max_length=100, blank=True, null=True)
    entrepreneurreg = models.CharField(max_length=100, blank=True, null=True)
    okpo = models.CharField(max_length=100, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_organizationdetails'


class JkitepOrganizationdetailsSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_organizationdetails_seq'


class JkitepOthereventduration(models.Model):
    othereventdurationid = models.AutoField(primary_key=True)
    othereventduration = models.CharField(max_length=200)
    sortorderid = models.IntegerField(blank=True, null=True)
    presence = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_othereventduration'


class JkitepOthereventdurationSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_othereventduration_seq'


class JkitepParenttab(models.Model):
    parenttabid = models.IntegerField(primary_key=True)
    parenttab_label = models.CharField(max_length=100)
    sequence = models.IntegerField()
    visible = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_parenttab'


class JkitepParenttabrel(models.Model):
    parenttabid = models.ForeignKey(JkitepParenttab, models.DO_NOTHING, db_column='parenttabid')
    tabid = models.ForeignKey('JkitepTab', models.DO_NOTHING, db_column='tabid')
    sequence = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_parenttabrel'


class JkitepParts(models.Model):
    partsid = models.IntegerField(primary_key=True)
    part_no = models.CharField(max_length=100, blank=True, null=True)
    partname = models.CharField(max_length=100, blank=True, null=True)
    textbook_id = models.CharField(max_length=100, blank=True, null=True)
    purchaseorder_id = models.CharField(max_length=100, blank=True, null=True)
    isbn_textbook = models.CharField(max_length=100, blank=True, null=True)
    bar_code = models.IntegerField(blank=True, null=True)
    rent_start = models.DateField(blank=True, null=True)
    rent_end = models.DateField(blank=True, null=True)
    count = models.CharField(max_length=100, blank=True, null=True)
    price = models.CharField(max_length=100, blank=True, null=True)
    rent_price = models.CharField(max_length=100, blank=True, null=True)
    rec_price = models.CharField(max_length=100, blank=True, null=True)
    year_publish_part = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_parts'


class JkitepPartsUserField(models.Model):
    recordid = models.IntegerField()
    userid = models.IntegerField()
    starred = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_parts_user_field'


class JkitepPartscf(models.Model):
    partsid = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'jkitep_partscf'


class JkitepPayType(models.Model):
    pay_typeid = models.AutoField(primary_key=True)
    pay_type = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_pay_type'


class JkitepPayTypeSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_pay_type_seq'


class JkitepPaymentDuration(models.Model):
    payment_duration_id = models.IntegerField(blank=True, null=True)
    payment_duration = models.CharField(max_length=200, blank=True, null=True)
    sortorderid = models.IntegerField(blank=True, null=True)
    presence = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_payment_duration'


class JkitepPaymentDurationSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_payment_duration_seq'


class JkitepPbxmanager(models.Model):
    pbxmanagerid = models.OneToOneField(JkitepCrmentity, models.DO_NOTHING, db_column='pbxmanagerid', primary_key=True)
    direction = models.CharField(max_length=10, blank=True, null=True)
    callstatus = models.CharField(max_length=20, blank=True, null=True)
    starttime = models.DateTimeField(blank=True, null=True)
    endtime = models.DateTimeField(blank=True, null=True)
    totalduration = models.IntegerField(blank=True, null=True)
    billduration = models.IntegerField(blank=True, null=True)
    recordingurl = models.CharField(max_length=200, blank=True, null=True)
    sourceuuid = models.CharField(max_length=100, blank=True, null=True)
    gateway = models.CharField(max_length=20, blank=True, null=True)
    customer = models.CharField(max_length=100, blank=True, null=True)
    user = models.CharField(max_length=100, blank=True, null=True)
    customernumber = models.CharField(max_length=100, blank=True, null=True)
    customertype = models.CharField(max_length=100, blank=True, null=True)
    incominglinename = models.CharField(max_length=100, blank=True, null=True)
    sp_is_local_cached = models.IntegerField(blank=True, null=True)
    sp_recordingurl = models.CharField(max_length=255, blank=True, null=True)
    sp_is_recorded = models.CharField(max_length=255, blank=True, null=True)
    sp_recorded_call_id = models.CharField(max_length=255, blank=True, null=True)
    sp_voip_provider = models.CharField(max_length=255, blank=True, null=True)
    sp_call_status_code = models.CharField(max_length=255, blank=True, null=True)
    sp_called_from_number = models.CharField(max_length=255, blank=True, null=True)
    sp_called_to_number = models.CharField(max_length=255, blank=True, null=True)
    tags = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_pbxmanager'


class JkitepPbxmanagerGateway(models.Model):
    gateway = models.CharField(max_length=20, blank=True, null=True)
    parameters = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_pbxmanager_gateway'


class JkitepPbxmanagerPhonelookup(models.Model):
    crmid = models.ForeignKey(JkitepCrmentity, models.DO_NOTHING, db_column='crmid', blank=True, null=True)
    setype = models.CharField(max_length=30, blank=True, null=True)
    fnumber = models.CharField(max_length=100, blank=True, null=True)
    rnumber = models.CharField(max_length=100, blank=True, null=True)
    fieldname = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_pbxmanager_phonelookup'
        unique_together = (('crmid', 'setype', 'fieldname'),)


class JkitepPbxmanagercf(models.Model):
    pbxmanagerid = models.OneToOneField(JkitepPbxmanager, models.DO_NOTHING, db_column='pbxmanagerid', primary_key=True)

    class Meta:
        managed = False
        db_table = 'jkitep_pbxmanagercf'


class JkitepPedadvice(models.Model):
    pedadviceid = models.AutoField(primary_key=True)
    pedadvice = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_pedadvice'


class JkitepPedadviceSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_pedadvice_seq'


class JkitepPicklist(models.Model):
    picklistid = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=200)

    class Meta:
        managed = False
        db_table = 'jkitep_picklist'


class JkitepPicklistDependency(models.Model):
    id = models.IntegerField(primary_key=True)
    tabid = models.IntegerField()
    sourcefield = models.CharField(max_length=255, blank=True, null=True)
    targetfield = models.CharField(max_length=255, blank=True, null=True)
    sourcevalue = models.CharField(max_length=100, blank=True, null=True)
    targetvalues = models.TextField(blank=True, null=True)
    criteria = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_picklist_dependency'


class JkitepPicklistDependencySeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_picklist_dependency_seq'


class JkitepPicklistSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_picklist_seq'


class JkitepPicklistTransitions(models.Model):
    fieldname = models.CharField(primary_key=True, max_length=255)
    module = models.CharField(max_length=100)
    transition_data = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'jkitep_picklist_transitions'


class JkitepPicklistvaluesSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_picklistvalues_seq'


class JkitepPobillads(models.Model):
    pobilladdressid = models.OneToOneField('JkitepPurchaseorder', models.DO_NOTHING, db_column='pobilladdressid', primary_key=True)
    bill_city = models.CharField(max_length=30, blank=True, null=True)
    bill_code = models.CharField(max_length=30, blank=True, null=True)
    bill_country = models.CharField(max_length=30, blank=True, null=True)
    bill_state = models.CharField(max_length=30, blank=True, null=True)
    bill_street = models.CharField(max_length=250, blank=True, null=True)
    bill_pobox = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_pobillads'


class JkitepPortal(models.Model):
    portalid = models.IntegerField(primary_key=True)
    portalname = models.CharField(max_length=200)
    portalurl = models.CharField(max_length=255)
    sequence = models.IntegerField()
    setdefault = models.IntegerField()
    createdtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_portal'


class JkitepPortalSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_portal_seq'


class JkitepPortalinfo(models.Model):
    id = models.OneToOneField(JkitepContactdetails, models.DO_NOTHING, db_column='id', primary_key=True)
    user_name = models.CharField(max_length=50, blank=True, null=True)
    user_password = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=5, blank=True, null=True)
    cryptmode = models.CharField(max_length=20, blank=True, null=True)
    last_login_time = models.DateTimeField(blank=True, null=True)
    login_time = models.DateTimeField(blank=True, null=True)
    logout_time = models.DateTimeField(blank=True, null=True)
    isactive = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_portalinfo'


class JkitepPoshipads(models.Model):
    poshipaddressid = models.OneToOneField('JkitepPurchaseorder', models.DO_NOTHING, db_column='poshipaddressid', primary_key=True)
    ship_city = models.CharField(max_length=30, blank=True, null=True)
    ship_code = models.CharField(max_length=30, blank=True, null=True)
    ship_country = models.CharField(max_length=30, blank=True, null=True)
    ship_state = models.CharField(max_length=30, blank=True, null=True)
    ship_street = models.CharField(max_length=250, blank=True, null=True)
    ship_pobox = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_poshipads'


class JkitepPositionSchoolStaff(models.Model):
    position_school_staffid = models.AutoField(primary_key=True)
    position_school_staff = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_position_school_staff'


class JkitepPositionSchoolStaffSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_position_school_staff_seq'


class JkitepPositionUserEmployee(models.Model):
    position_user_employeeid = models.AutoField(primary_key=True)
    position_user_employee = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_position_user_employee'


class JkitepPositionUserEmployeeSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_position_user_employee_seq'


class JkitepPostatus(models.Model):
    postatusid = models.AutoField(primary_key=True)
    postatus = models.CharField(unique=True, max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_postatus'


class JkitepPostatusSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_postatus_seq'


class JkitepPostatushistory(models.Model):
    historyid = models.AutoField(primary_key=True)
    purchaseorderid = models.ForeignKey('JkitepPurchaseorder', models.DO_NOTHING, db_column='purchaseorderid')
    vendorname = models.CharField(max_length=100, blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    postatus = models.CharField(max_length=200, blank=True, null=True)
    lastmodified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_postatushistory'


class JkitepPostatushistorySeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_postatushistory_seq'


class JkitepPotential(models.Model):
    potentialid = models.OneToOneField(JkitepCrmentity, models.DO_NOTHING, db_column='potentialid', primary_key=True)
    potential_no = models.CharField(max_length=100)
    related_to = models.IntegerField(blank=True, null=True)
    potentialname = models.CharField(max_length=120)
    amount = models.DecimalField(max_digits=25, decimal_places=8, blank=True, null=True)
    currency = models.CharField(max_length=20, blank=True, null=True)
    closingdate = models.DateField(blank=True, null=True)
    typeofrevenue = models.CharField(max_length=50, blank=True, null=True)
    nextstep = models.CharField(max_length=100, blank=True, null=True)
    private = models.IntegerField(blank=True, null=True)
    probability = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    campaignid = models.IntegerField(blank=True, null=True)
    sales_stage = models.CharField(max_length=200, blank=True, null=True)
    potentialtype = models.CharField(max_length=200, blank=True, null=True)
    leadsource = models.CharField(max_length=200, blank=True, null=True)
    productid = models.IntegerField(blank=True, null=True)
    productversion = models.CharField(max_length=50, blank=True, null=True)
    quotationref = models.CharField(max_length=50, blank=True, null=True)
    partnercontact = models.CharField(max_length=50, blank=True, null=True)
    remarks = models.CharField(max_length=50, blank=True, null=True)
    runtimefee = models.IntegerField(blank=True, null=True)
    followupdate = models.DateField(blank=True, null=True)
    evaluationstatus = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    forecastcategory = models.IntegerField(blank=True, null=True)
    outcomeanalysis = models.IntegerField(blank=True, null=True)
    forecast_amount = models.DecimalField(max_digits=25, decimal_places=8, blank=True, null=True)
    isconvertedfromlead = models.CharField(max_length=3, blank=True, null=True)
    contact_id = models.IntegerField(blank=True, null=True)
    spcompany = models.CharField(max_length=200, blank=True, null=True)
    tags = models.CharField(max_length=1, blank=True, null=True)
    converted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_potential'


class JkitepPotentialscf(models.Model):
    potentialid = models.OneToOneField(JkitepPotential, models.DO_NOTHING, db_column='potentialid', primary_key=True)

    class Meta:
        managed = False
        db_table = 'jkitep_potentialscf'


class JkitepPotstagehistory(models.Model):
    historyid = models.AutoField(primary_key=True)
    potentialid = models.ForeignKey(JkitepPotential, models.DO_NOTHING, db_column='potentialid')
    amount = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    stage = models.CharField(max_length=100, blank=True, null=True)
    probability = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    expectedrevenue = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    closedate = models.DateField(blank=True, null=True)
    lastmodified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_potstagehistory'


class JkitepPricebook(models.Model):
    pricebookid = models.OneToOneField(JkitepCrmentity, models.DO_NOTHING, db_column='pricebookid', primary_key=True)
    pricebook_no = models.CharField(max_length=100)
    bookname = models.CharField(max_length=100, blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    currency_id = models.IntegerField()
    one_s_id = models.CharField(max_length=255, blank=True, null=True)
    tags = models.CharField(max_length=1, blank=True, null=True)
    school_id = models.CharField(max_length=100, blank=True, null=True)
    quantity = models.CharField(max_length=100, blank=True, null=True)
    quote_id = models.CharField(max_length=100, blank=True, null=True)
    purchaseorder_id = models.CharField(max_length=100, blank=True, null=True)
    so_id = models.CharField(max_length=100, blank=True, null=True)
    is_delivered = models.CharField(max_length=20, blank=True, null=True)
    is_accepted_school = models.CharField(max_length=20, blank=True, null=True)
    is_accepted_area = models.CharField(max_length=20, blank=True, null=True)
    region_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_pricebook'


class JkitepPricebookcf(models.Model):
    pricebookid = models.OneToOneField(JkitepPricebook, models.DO_NOTHING, db_column='pricebookid', primary_key=True)

    class Meta:
        managed = False
        db_table = 'jkitep_pricebookcf'


class JkitepPricebookproductrel(models.Model):
    pricebookid = models.OneToOneField(JkitepPricebook, models.DO_NOTHING, db_column='pricebookid', primary_key=True)
    productid = models.IntegerField()
    listprice = models.DecimalField(max_digits=27, decimal_places=8, blank=True, null=True)
    usedcurrency = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_pricebookproductrel'
        unique_together = (('pricebookid', 'productid'),)


class JkitepPriority(models.Model):
    priorityid = models.AutoField(primary_key=True)
    priority = models.CharField(unique=True, max_length=200)
    sortorderid = models.IntegerField()
    presence = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_priority'


class JkitepProductcategory(models.Model):
    productcategoryid = models.AutoField(primary_key=True)
    productcategory = models.CharField(unique=True, max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_productcategory'


class JkitepProductcategorySeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_productcategory_seq'


class JkitepProductcf(models.Model):
    productid = models.OneToOneField('JkitepProducts', models.DO_NOTHING, db_column='productid', primary_key=True)

    class Meta:
        managed = False
        db_table = 'jkitep_productcf'


class JkitepProductcurrencyrel(models.Model):
    productid = models.IntegerField()
    currencyid = models.IntegerField()
    converted_price = models.DecimalField(max_digits=28, decimal_places=8, blank=True, null=True)
    actual_price = models.DecimalField(max_digits=28, decimal_places=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_productcurrencyrel'


class JkitepProducts(models.Model):
    productid = models.OneToOneField(JkitepCrmentity, models.DO_NOTHING, db_column='productid', primary_key=True)
    product_no = models.CharField(max_length=100)
    productname = models.CharField(max_length=100, blank=True, null=True)
    productcode = models.CharField(max_length=40, blank=True, null=True)
    productcategory = models.CharField(max_length=200, blank=True, null=True)
    manufacturer = models.CharField(max_length=200, blank=True, null=True)
    qty_per_unit = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    unit_price = models.DecimalField(max_digits=25, decimal_places=8, blank=True, null=True)
    weight = models.DecimalField(max_digits=11, decimal_places=3, blank=True, null=True)
    pack_size = models.IntegerField(blank=True, null=True)
    sales_start_date = models.DateField(blank=True, null=True)
    sales_end_date = models.DateField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)
    cost_factor = models.IntegerField(blank=True, null=True)
    commissionrate = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    commissionmethod = models.CharField(max_length=50, blank=True, null=True)
    discontinued = models.IntegerField()
    usageunit = models.CharField(max_length=200, blank=True, null=True)
    reorderlevel = models.IntegerField(blank=True, null=True)
    website = models.CharField(max_length=100, blank=True, null=True)
    taxclass = models.CharField(max_length=200, blank=True, null=True)
    mfr_part_no = models.CharField(max_length=200, blank=True, null=True)
    vendor_part_no = models.CharField(max_length=200, blank=True, null=True)
    serialno = models.CharField(max_length=200, blank=True, null=True)
    qtyinstock = models.DecimalField(max_digits=25, decimal_places=3, blank=True, null=True)
    productsheet = models.CharField(max_length=200, blank=True, null=True)
    qtyindemand = models.IntegerField(blank=True, null=True)
    glacct = models.CharField(max_length=200, blank=True, null=True)
    vendor_id = models.IntegerField(blank=True, null=True)
    imagename = models.TextField(blank=True, null=True)
    currency_id = models.IntegerField()
    is_subproducts_viewable = models.IntegerField(blank=True, null=True)
    manuf_country = models.CharField(max_length=100, blank=True, null=True)
    customs_id = models.CharField(max_length=100, blank=True, null=True)
    manuf_country_code = models.CharField(max_length=100, blank=True, null=True)
    unit_code = models.CharField(max_length=100, blank=True, null=True)
    one_s_id = models.CharField(max_length=255, blank=True, null=True)
    purchase_cost = models.DecimalField(max_digits=27, decimal_places=8, blank=True, null=True)
    tags = models.CharField(max_length=1, blank=True, null=True)
    sp_product_international_code = models.CharField(max_length=255, blank=True, null=True)
    textbook_id = models.CharField(max_length=100, blank=True, null=True)
    bar_code = models.IntegerField(blank=True, null=True)
    qr_code = models.CharField(max_length=100, blank=True, null=True)
    rent_start = models.DateField(blank=True, null=True)
    rent_end = models.DateField(blank=True, null=True)
    school_id = models.CharField(max_length=100, blank=True, null=True)
    student_id = models.CharField(max_length=100, blank=True, null=True)
    own_textbook = models.CharField(max_length=20, blank=True, null=True)
    textbook_state = models.CharField(max_length=200, blank=True, null=True)
    isbn_textbook = models.CharField(max_length=100, blank=True, null=True)
    part = models.CharField(max_length=100, blank=True, null=True)
    is_busy = models.CharField(max_length=20, blank=True, null=True)
    region_id = models.CharField(max_length=100, blank=True, null=True)
    is_own = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_products'


class JkitepProducttaxrel(models.Model):
    productid = models.ForeignKey(JkitepCrmentity, models.DO_NOTHING, db_column='productid')
    taxid = models.IntegerField()
    taxpercentage = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    regions = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_producttaxrel'


class JkitepProfile(models.Model):
    profileid = models.AutoField(primary_key=True)
    profilename = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    directly_related_to_role = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_profile'


class JkitepProfile2Field(models.Model):
    profileid = models.IntegerField(primary_key=True)
    tabid = models.IntegerField(blank=True, null=True)
    fieldid = models.IntegerField()
    visible = models.IntegerField(blank=True, null=True)
    readonly = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_profile2field'
        unique_together = (('profileid', 'fieldid'),)


class JkitepProfile2Globalpermissions(models.Model):
    profileid = models.OneToOneField(JkitepProfile, models.DO_NOTHING, db_column='profileid', primary_key=True)
    globalactionid = models.IntegerField()
    globalactionpermission = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_profile2globalpermissions'
        unique_together = (('profileid', 'globalactionid'),)


class JkitepProfile2Standardpermissions(models.Model):
    profileid = models.IntegerField(primary_key=True)
    tabid = models.IntegerField()
    operation = models.IntegerField()
    permissions = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_profile2standardpermissions'
        unique_together = (('profileid', 'tabid', 'operation'),)


class JkitepProfile2Tab(models.Model):
    profileid = models.IntegerField(blank=True, null=True)
    tabid = models.IntegerField(blank=True, null=True)
    permissions = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_profile2tab'


class JkitepProfile2Utility(models.Model):
    profileid = models.IntegerField(primary_key=True)
    tabid = models.IntegerField()
    activityid = models.IntegerField()
    permission = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_profile2utility'
        unique_together = (('profileid', 'tabid', 'activityid'),)


class JkitepProfileSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_profile_seq'


class JkitepProgress(models.Model):
    progressid = models.AutoField(primary_key=True)
    progress = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_progress'


class JkitepProgressSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_progress_seq'


class JkitepProject(models.Model):
    projectid = models.OneToOneField(JkitepCrmentity, models.DO_NOTHING, db_column='projectid', primary_key=True)
    projectname = models.CharField(max_length=255, blank=True, null=True)
    project_no = models.CharField(max_length=100, blank=True, null=True)
    startdate = models.DateField(blank=True, null=True)
    targetenddate = models.DateField(blank=True, null=True)
    actualenddate = models.DateField(blank=True, null=True)
    targetbudget = models.CharField(max_length=255, blank=True, null=True)
    projecturl = models.CharField(max_length=255, blank=True, null=True)
    projectstatus = models.CharField(max_length=100, blank=True, null=True)
    projectpriority = models.CharField(max_length=100, blank=True, null=True)
    projecttype = models.CharField(max_length=100, blank=True, null=True)
    progress = models.CharField(max_length=100, blank=True, null=True)
    linktoaccountscontacts = models.CharField(max_length=100, blank=True, null=True)
    tags = models.CharField(max_length=1, blank=True, null=True)
    isconvertedfrompotential = models.IntegerField()
    potentialid = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_project'


class JkitepProjectcf(models.Model):
    projectid = models.OneToOneField(JkitepProject, models.DO_NOTHING, db_column='projectid', primary_key=True)

    class Meta:
        managed = False
        db_table = 'jkitep_projectcf'


class JkitepProjectmilestone(models.Model):
    projectmilestoneid = models.OneToOneField(JkitepCrmentity, models.DO_NOTHING, db_column='projectmilestoneid', primary_key=True)
    projectmilestonename = models.CharField(max_length=255, blank=True, null=True)
    projectmilestone_no = models.CharField(max_length=100, blank=True, null=True)
    projectmilestonedate = models.CharField(max_length=255, blank=True, null=True)
    projectid = models.CharField(max_length=100, blank=True, null=True)
    projectmilestonetype = models.CharField(max_length=100, blank=True, null=True)
    tags = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_projectmilestone'


class JkitepProjectmilestonecf(models.Model):
    projectmilestoneid = models.OneToOneField(JkitepProjectmilestone, models.DO_NOTHING, db_column='projectmilestoneid', primary_key=True)

    class Meta:
        managed = False
        db_table = 'jkitep_projectmilestonecf'


class JkitepProjectmilestonetype(models.Model):
    projectmilestonetypeid = models.AutoField(primary_key=True)
    projectmilestonetype = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_projectmilestonetype'


class JkitepProjectmilestonetypeSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_projectmilestonetype_seq'


class JkitepProjectpriority(models.Model):
    projectpriorityid = models.AutoField(primary_key=True)
    projectpriority = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_projectpriority'


class JkitepProjectprioritySeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_projectpriority_seq'


class JkitepProjectstatus(models.Model):
    projectstatusid = models.AutoField(primary_key=True)
    projectstatus = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_projectstatus'


class JkitepProjectstatusSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_projectstatus_seq'


class JkitepProjecttask(models.Model):
    projecttaskid = models.OneToOneField(JkitepCrmentity, models.DO_NOTHING, db_column='projecttaskid', primary_key=True)
    projecttaskname = models.CharField(max_length=255, blank=True, null=True)
    projecttask_no = models.CharField(max_length=100, blank=True, null=True)
    projecttasktype = models.CharField(max_length=100, blank=True, null=True)
    projecttaskpriority = models.CharField(max_length=100, blank=True, null=True)
    projecttaskprogress = models.CharField(max_length=100, blank=True, null=True)
    projecttaskhours = models.CharField(max_length=255, blank=True, null=True)
    startdate = models.DateField(blank=True, null=True)
    enddate = models.DateField(blank=True, null=True)
    projectid = models.CharField(max_length=100, blank=True, null=True)
    projecttasknumber = models.IntegerField(blank=True, null=True)
    tags = models.CharField(max_length=1, blank=True, null=True)
    projecttaskstatus = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_projecttask'


class JkitepProjecttaskStatusColor(models.Model):
    status = models.CharField(unique=True, max_length=255, blank=True, null=True)
    defaultcolor = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_projecttask_status_color'


class JkitepProjecttaskcf(models.Model):
    projecttaskid = models.OneToOneField(JkitepProjecttask, models.DO_NOTHING, db_column='projecttaskid', primary_key=True)

    class Meta:
        managed = False
        db_table = 'jkitep_projecttaskcf'


class JkitepProjecttaskpriority(models.Model):
    projecttaskpriorityid = models.AutoField(primary_key=True)
    projecttaskpriority = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_projecttaskpriority'


class JkitepProjecttaskprioritySeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_projecttaskpriority_seq'


class JkitepProjecttaskprogress(models.Model):
    projecttaskprogressid = models.AutoField(primary_key=True)
    projecttaskprogress = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_projecttaskprogress'


class JkitepProjecttaskprogressSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_projecttaskprogress_seq'


class JkitepProjecttaskstatus(models.Model):
    projecttaskstatusid = models.AutoField(primary_key=True)
    projecttaskstatus = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_projecttaskstatus'


class JkitepProjecttaskstatusSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_projecttaskstatus_seq'


class JkitepProjecttasktype(models.Model):
    projecttasktypeid = models.AutoField(primary_key=True)
    projecttasktype = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_projecttasktype'


class JkitepProjecttasktypeSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_projecttasktype_seq'


class JkitepProjecttype(models.Model):
    projecttypeid = models.AutoField(primary_key=True)
    projecttype = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_projecttype'


class JkitepProjecttypeSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_projecttype_seq'


class JkitepPublishyear(models.Model):
    publishyearid = models.AutoField(primary_key=True)
    publishyear = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_publishyear'


class JkitepPublishyearSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_publishyear_seq'


class JkitepPurchaseorder(models.Model):
    purchaseorderid = models.OneToOneField(JkitepCrmentity, models.DO_NOTHING, db_column='purchaseorderid', primary_key=True)
    subject = models.CharField(max_length=100, blank=True, null=True)
    quoteid = models.IntegerField(blank=True, null=True)
    vendorid = models.ForeignKey('JkitepVendor', models.DO_NOTHING, db_column='vendorid', blank=True, null=True)
    requisition_no = models.CharField(max_length=100, blank=True, null=True)
    purchaseorder_no = models.CharField(max_length=100, blank=True, null=True)
    tracking_no = models.CharField(max_length=100, blank=True, null=True)
    contactid = models.IntegerField(blank=True, null=True)
    duedate = models.DateField(blank=True, null=True)
    carrier = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    adjustment = models.DecimalField(max_digits=25, decimal_places=8, blank=True, null=True)
    salescommission = models.DecimalField(max_digits=25, decimal_places=3, blank=True, null=True)
    exciseduty = models.DecimalField(max_digits=25, decimal_places=3, blank=True, null=True)
    total = models.DecimalField(max_digits=25, decimal_places=8, blank=True, null=True)
    subtotal = models.DecimalField(max_digits=25, decimal_places=8, blank=True, null=True)
    taxtype = models.CharField(max_length=25, blank=True, null=True)
    discount_percent = models.DecimalField(max_digits=25, decimal_places=3, blank=True, null=True)
    discount_amount = models.DecimalField(max_digits=25, decimal_places=8, blank=True, null=True)
    s_h_amount = models.DecimalField(max_digits=25, decimal_places=8, blank=True, null=True)
    terms_conditions = models.TextField(blank=True, null=True)
    postatus = models.CharField(max_length=200, blank=True, null=True)
    currency_id = models.IntegerField()
    conversion_rate = models.DecimalField(max_digits=10, decimal_places=3)
    compound_taxes_info = models.TextField(blank=True, null=True)
    pre_tax_total = models.DecimalField(max_digits=25, decimal_places=8, blank=True, null=True)
    paid = models.DecimalField(max_digits=25, decimal_places=8, blank=True, null=True)
    balance = models.DecimalField(max_digits=25, decimal_places=8, blank=True, null=True)
    s_h_percent = models.IntegerField(blank=True, null=True)
    spcompany = models.CharField(max_length=200, blank=True, null=True)
    tags = models.CharField(max_length=1, blank=True, null=True)
    region_id = models.IntegerField(blank=True, null=True)
    status_region_pur = models.CharField(max_length=700, blank=True, null=True)
    status_jk_pur = models.CharField(max_length=700, blank=True, null=True)
    region_pur_id = models.CharField(max_length=100, blank=True, null=True)
    tender_status = models.CharField(max_length=700, blank=True, null=True)
    part_id = models.CharField(max_length=100, blank=True, null=True)
    supplier_status_pur = models.CharField(max_length=100, blank=True, null=True)
    isbn = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_purchaseorder'


class JkitepPurchaseordercf(models.Model):
    purchaseorderid = models.OneToOneField(JkitepPurchaseorder, models.DO_NOTHING, db_column='purchaseorderid', primary_key=True)

    class Meta:
        managed = False
        db_table = 'jkitep_purchaseordercf'


class JkitepQueryLog(models.Model):
    query = models.CharField(unique=True, max_length=50)
    result = models.TextField()
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'jkitep_query_log'


class JkitepQuoteAcaYear(models.Model):
    quote_aca_yearid = models.AutoField(primary_key=True)
    quote_aca_year = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_quote_aca_year'


class JkitepQuoteAcaYearSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_quote_aca_year_seq'


class JkitepQuoteStageJk(models.Model):
    quote_stage_jkid = models.AutoField(primary_key=True)
    quote_stage_jk = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_quote_stage_jk'


class JkitepQuoteStageJkSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_quote_stage_jk_seq'


class JkitepQuoteStageRegion(models.Model):
    quote_stage_regionid = models.AutoField(primary_key=True)
    quote_stage_region = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_quote_stage_region'


class JkitepQuoteStageRegionSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_quote_stage_region_seq'


class JkitepQuoteStageSchool(models.Model):
    quote_stage_schoolid = models.AutoField(primary_key=True)
    quote_stage_school = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_quote_stage_school'


class JkitepQuoteStageSchoolSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_quote_stage_school_seq'


class JkitepQuotes(models.Model):
    quoteid = models.OneToOneField(JkitepCrmentity, models.DO_NOTHING, db_column='quoteid', primary_key=True)
    subject = models.CharField(max_length=100, blank=True, null=True)
    potentialid = models.ForeignKey(JkitepPotential, models.DO_NOTHING, db_column='potentialid', blank=True, null=True)
    quotestage = models.CharField(max_length=200, blank=True, null=True)
    validtill = models.DateField(blank=True, null=True)
    contactid = models.IntegerField(blank=True, null=True)
    quote_no = models.CharField(max_length=100, blank=True, null=True)
    subtotal = models.DecimalField(max_digits=25, decimal_places=8, blank=True, null=True)
    carrier = models.CharField(max_length=200, blank=True, null=True)
    shipping = models.CharField(max_length=100, blank=True, null=True)
    inventorymanager = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    adjustment = models.DecimalField(max_digits=25, decimal_places=8, blank=True, null=True)
    total = models.DecimalField(max_digits=25, decimal_places=8, blank=True, null=True)
    taxtype = models.CharField(max_length=25, blank=True, null=True)
    discount_percent = models.DecimalField(max_digits=25, decimal_places=3, blank=True, null=True)
    discount_amount = models.DecimalField(max_digits=25, decimal_places=8, blank=True, null=True)
    s_h_amount = models.DecimalField(max_digits=25, decimal_places=8, blank=True, null=True)
    accountid = models.IntegerField(blank=True, null=True)
    terms_conditions = models.TextField(blank=True, null=True)
    currency_id = models.IntegerField()
    conversion_rate = models.DecimalField(max_digits=10, decimal_places=3)
    compound_taxes_info = models.TextField(blank=True, null=True)
    pre_tax_total = models.DecimalField(max_digits=25, decimal_places=8, blank=True, null=True)
    s_h_percent = models.IntegerField(blank=True, null=True)
    spcompany = models.CharField(max_length=200, blank=True, null=True)
    tags = models.CharField(max_length=1, blank=True, null=True)
    school_id = models.CharField(max_length=100, blank=True, null=True)
    region_id = models.IntegerField(blank=True, null=True)
    region_quotes_id = models.CharField(max_length=100, blank=True, null=True)
    salesorder_id = models.CharField(max_length=100, blank=True, null=True)
    quote_stage_school = models.CharField(max_length=200, blank=True, null=True)
    quote_stage_region = models.CharField(max_length=200, blank=True, null=True)
    quote_aca_year = models.CharField(max_length=300, blank=True, null=True)
    is_used_balance = models.CharField(max_length=20, blank=True, null=True)
    quote_stage_jk = models.CharField(max_length=200, blank=True, null=True)
    purchase_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_quotes'


class JkitepQuotesbillads(models.Model):
    quotebilladdressid = models.OneToOneField(JkitepQuotes, models.DO_NOTHING, db_column='quotebilladdressid', primary_key=True)
    bill_city = models.CharField(max_length=30, blank=True, null=True)
    bill_code = models.CharField(max_length=30, blank=True, null=True)
    bill_country = models.CharField(max_length=30, blank=True, null=True)
    bill_state = models.CharField(max_length=30, blank=True, null=True)
    bill_street = models.CharField(max_length=250, blank=True, null=True)
    bill_pobox = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_quotesbillads'


class JkitepQuotescf(models.Model):
    quoteid = models.OneToOneField(JkitepQuotes, models.DO_NOTHING, db_column='quoteid', primary_key=True)

    class Meta:
        managed = False
        db_table = 'jkitep_quotescf'


class JkitepQuotesshipads(models.Model):
    quoteshipaddressid = models.OneToOneField(JkitepQuotes, models.DO_NOTHING, db_column='quoteshipaddressid', primary_key=True)
    ship_city = models.CharField(max_length=30, blank=True, null=True)
    ship_code = models.CharField(max_length=30, blank=True, null=True)
    ship_country = models.CharField(max_length=30, blank=True, null=True)
    ship_state = models.CharField(max_length=30, blank=True, null=True)
    ship_street = models.CharField(max_length=250, blank=True, null=True)
    ship_pobox = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_quotesshipads'


class JkitepQuotestage(models.Model):
    quotestageid = models.AutoField(primary_key=True)
    quotestage = models.CharField(unique=True, max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_quotestage'


class JkitepQuotestageSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_quotestage_seq'


class JkitepQuotestagehistory(models.Model):
    historyid = models.AutoField(primary_key=True)
    quoteid = models.ForeignKey(JkitepQuotes, models.DO_NOTHING, db_column='quoteid')
    accountname = models.CharField(max_length=100, blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    quotestage = models.CharField(max_length=200, blank=True, null=True)
    lastmodified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_quotestagehistory'


class JkitepQuotestagehistorySeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_quotestagehistory_seq'


class JkitepRating(models.Model):
    rating_id = models.AutoField(primary_key=True)
    rating = models.CharField(max_length=200, blank=True, null=True)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_rating'


class JkitepRatingSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_rating_seq'


class JkitepReasontrn(models.Model):
    reasontrnid = models.AutoField(primary_key=True)
    reasontrn = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_reasontrn'


class JkitepReasontrnSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_reasontrn_seq'


class JkitepRecurringFrequency(models.Model):
    recurring_frequency_id = models.IntegerField(blank=True, null=True)
    recurring_frequency = models.CharField(max_length=200, blank=True, null=True)
    sortorderid = models.IntegerField(blank=True, null=True)
    presence = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_recurring_frequency'


class JkitepRecurringFrequencySeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_recurring_frequency_seq'


class JkitepRecurringevents(models.Model):
    recurringid = models.AutoField(primary_key=True)
    activityid = models.ForeignKey(JkitepActivity, models.DO_NOTHING, db_column='activityid')
    recurringdate = models.DateField(blank=True, null=True)
    recurringtype = models.CharField(max_length=30, blank=True, null=True)
    recurringfreq = models.IntegerField(blank=True, null=True)
    recurringinfo = models.CharField(max_length=50, blank=True, null=True)
    recurringenddate = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_recurringevents'


class JkitepRecurringtype(models.Model):
    recurringeventid = models.AutoField(primary_key=True)
    recurringtype = models.CharField(unique=True, max_length=200)
    sortorderid = models.IntegerField()
    presence = models.IntegerField()
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_recurringtype'


class JkitepRecurringtypeSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_recurringtype_seq'


class JkitepRegion(models.Model):
    regionid = models.IntegerField(primary_key=True)
    region_no = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    email_reg = models.CharField(max_length=100, blank=True, null=True)
    email_heaad = models.CharField(max_length=100, blank=True, null=True)
    fuul_name_head = models.CharField(max_length=100, blank=True, null=True)
    full_name_reg = models.CharField(max_length=100, blank=True, null=True)
    mobile_head = models.CharField(max_length=100, blank=True, null=True)
    mobile = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    fax = models.CharField(max_length=100, blank=True, null=True)
    balance = models.DecimalField(max_digits=27, decimal_places=8, blank=True, null=True)
    region_id_name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    iscity = models.CharField(max_length=100, blank=True, null=True)
    code = models.CharField(max_length=100, blank=True, null=True)
    balance_sum = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_region'


class JkitepRegionSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_region_seq'


class JkitepRegionUserField(models.Model):
    recordid = models.IntegerField()
    userid = models.IntegerField()
    starred = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_region_user_field'


class JkitepRegioncf(models.Model):
    regionid = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'jkitep_regioncf'


class JkitepRegions(models.Model):
    regionsid = models.IntegerField(primary_key=True)
    region_no = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_regions'


class JkitepRegionsUserField(models.Model):
    recordid = models.IntegerField()
    userid = models.IntegerField()
    starred = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_regions_user_field'


class JkitepRegionscf(models.Model):
    regionsid = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'jkitep_regionscf'


class JkitepRelatedlists(models.Model):
    relation_id = models.IntegerField(primary_key=True)
    tabid = models.IntegerField(blank=True, null=True)
    related_tabid = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    label = models.CharField(max_length=100, blank=True, null=True)
    presence = models.IntegerField()
    actions = models.CharField(max_length=50)
    relationfieldid = models.IntegerField(blank=True, null=True)
    source = models.CharField(max_length=25, blank=True, null=True)
    relationtype = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_relatedlists'


class JkitepRelatedlistsRb(models.Model):
    entityid = models.IntegerField(blank=True, null=True)
    action = models.CharField(max_length=50, blank=True, null=True)
    rel_table = models.CharField(max_length=200, blank=True, null=True)
    rel_column = models.CharField(max_length=200, blank=True, null=True)
    ref_column = models.CharField(max_length=200, blank=True, null=True)
    related_crm_ids = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_relatedlists_rb'


class JkitepRelatedlistsSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_relatedlists_seq'


class JkitepRelcriteria(models.Model):
    queryid = models.OneToOneField('JkitepSelectquery', models.DO_NOTHING, db_column='queryid', primary_key=True)
    columnindex = models.IntegerField()
    columnname = models.CharField(max_length=250, blank=True, null=True)
    comparator = models.CharField(max_length=20, blank=True, null=True)
    value = models.CharField(max_length=512, blank=True, null=True)
    groupid = models.IntegerField(blank=True, null=True)
    column_condition = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_relcriteria'
        unique_together = (('queryid', 'columnindex'),)


class JkitepRelcriteriaGrouping(models.Model):
    groupid = models.IntegerField(primary_key=True)
    queryid = models.IntegerField()
    group_condition = models.CharField(max_length=256, blank=True, null=True)
    condition_expression = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_relcriteria_grouping'
        unique_together = (('groupid', 'queryid'),)


class JkitepReminderInterval(models.Model):
    reminder_intervalid = models.AutoField(primary_key=True)
    reminder_interval = models.CharField(max_length=200)
    sortorderid = models.IntegerField()
    presence = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_reminder_interval'


class JkitepReminderIntervalSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_reminder_interval_seq'


class JkitepReport(models.Model):
    reportid = models.IntegerField(primary_key=True)
    folderid = models.IntegerField()
    reportname = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    reporttype = models.CharField(max_length=50, blank=True, null=True)
    queryid = models.ForeignKey('JkitepSelectquery', models.DO_NOTHING, db_column='queryid')
    state = models.CharField(max_length=50, blank=True, null=True)
    customizable = models.IntegerField(blank=True, null=True)
    category = models.IntegerField(blank=True, null=True)
    owner = models.IntegerField(blank=True, null=True)
    sharingtype = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_report'


class JkitepReportSharegroups(models.Model):
    reportid = models.ForeignKey(JkitepReport, models.DO_NOTHING, db_column='reportid')
    groupid = models.ForeignKey(JkitepGroups, models.DO_NOTHING, db_column='groupid')

    class Meta:
        managed = False
        db_table = 'jkitep_report_sharegroups'


class JkitepReportSharerole(models.Model):
    reportid = models.ForeignKey(JkitepReport, models.DO_NOTHING, db_column='reportid')
    roleid = models.ForeignKey('JkitepRole', models.DO_NOTHING, db_column='roleid')

    class Meta:
        managed = False
        db_table = 'jkitep_report_sharerole'


class JkitepReportSharers(models.Model):
    reportid = models.ForeignKey(JkitepReport, models.DO_NOTHING, db_column='reportid')
    rsid = models.ForeignKey('JkitepRole', models.DO_NOTHING, db_column='rsid')

    class Meta:
        managed = False
        db_table = 'jkitep_report_sharers'


class JkitepReportShareusers(models.Model):
    reportid = models.ForeignKey(JkitepReport, models.DO_NOTHING, db_column='reportid')
    userid = models.ForeignKey('JkitepUsers', models.DO_NOTHING, db_column='userid')

    class Meta:
        managed = False
        db_table = 'jkitep_report_shareusers'


class JkitepReportdatefilter(models.Model):
    datefilterid = models.OneToOneField(JkitepReport, models.DO_NOTHING, db_column='datefilterid', primary_key=True)
    datecolumnname = models.CharField(max_length=250, blank=True, null=True)
    datefilter = models.CharField(max_length=250, blank=True, null=True)
    startdate = models.DateField(blank=True, null=True)
    enddate = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_reportdatefilter'


class JkitepReportfilters(models.Model):
    filterid = models.IntegerField()
    name = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'jkitep_reportfilters'


class JkitepReportfolder(models.Model):
    folderid = models.AutoField(primary_key=True)
    foldername = models.CharField(max_length=100)
    description = models.CharField(max_length=250, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_reportfolder'


class JkitepReportgroupbycolumn(models.Model):
    reportid = models.ForeignKey(JkitepReport, models.DO_NOTHING, db_column='reportid', blank=True, null=True)
    sortid = models.IntegerField(blank=True, null=True)
    sortcolname = models.CharField(max_length=250, blank=True, null=True)
    dategroupbycriteria = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_reportgroupbycolumn'


class JkitepReportmodules(models.Model):
    reportmodulesid = models.OneToOneField(JkitepReport, models.DO_NOTHING, db_column='reportmodulesid', primary_key=True)
    primarymodule = models.CharField(max_length=100, blank=True, null=True)
    secondarymodules = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_reportmodules'


class JkitepReportsharing(models.Model):
    reportid = models.IntegerField()
    shareid = models.IntegerField()
    setype = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'jkitep_reportsharing'


class JkitepReportsortcol(models.Model):
    sortcolid = models.IntegerField(primary_key=True)
    reportid = models.ForeignKey(JkitepReport, models.DO_NOTHING, db_column='reportid')
    columnname = models.CharField(max_length=250, blank=True, null=True)
    sortorder = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_reportsortcol'
        unique_together = (('sortcolid', 'reportid'),)


class JkitepReportsummary(models.Model):
    reportsummaryid = models.OneToOneField(JkitepReport, models.DO_NOTHING, db_column='reportsummaryid', primary_key=True)
    summarytype = models.IntegerField()
    columnname = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'jkitep_reportsummary'
        unique_together = (('reportsummaryid', 'summarytype', 'columnname'),)


class JkitepReporttype(models.Model):
    reportid = models.OneToOneField(JkitepReport, models.DO_NOTHING, db_column='reportid', primary_key=True)
    data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_reporttype'


class JkitepRole(models.Model):
    roleid = models.CharField(primary_key=True, max_length=255)
    rolename = models.CharField(max_length=200, blank=True, null=True)
    parentrole = models.CharField(max_length=255, blank=True, null=True)
    depth = models.IntegerField(blank=True, null=True)
    allowassignedrecordsto = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_role'


class JkitepRole2Picklist(models.Model):
    roleid = models.OneToOneField(JkitepRole, models.DO_NOTHING, db_column='roleid', primary_key=True)
    picklistvalueid = models.IntegerField()
    picklistid = models.ForeignKey(JkitepPicklist, models.DO_NOTHING, db_column='picklistid')
    sortid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_role2picklist'
        unique_together = (('roleid', 'picklistvalueid', 'picklistid'),)


class JkitepRole2Profile(models.Model):
    roleid = models.CharField(primary_key=True, max_length=255)
    profileid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_role2profile'
        unique_together = (('roleid', 'profileid'),)


class JkitepRoleName(models.Model):
    role_nameid = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_role_name'


class JkitepRoleNameArea(models.Model):
    role_name_areaid = models.AutoField(primary_key=True)
    role_name_area = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_role_name_area'


class JkitepRoleNameEmp(models.Model):
    role_name_empid = models.AutoField(primary_key=True)
    role_name_emp = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_role_name_emp'


class JkitepRoleSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_role_seq'


class JkitepRollupcommentsSettings(models.Model):
    rollupid = models.AutoField(primary_key=True)
    userid = models.IntegerField()
    tabid = models.IntegerField()
    rollup_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_rollupcomments_settings'


class JkitepRowheight(models.Model):
    rowheightid = models.AutoField(primary_key=True)
    rowheight = models.CharField(max_length=200)
    sortorderid = models.IntegerField(blank=True, null=True)
    presence = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_rowheight'


class JkitepRowheightSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_rowheight_seq'


class JkitepRss(models.Model):
    rssid = models.IntegerField(primary_key=True)
    rssurl = models.CharField(max_length=200)
    rsstitle = models.CharField(max_length=200, blank=True, null=True)
    rsstype = models.IntegerField(blank=True, null=True)
    starred = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_rss'


class JkitepSalesStage(models.Model):
    sales_stage_id = models.AutoField(primary_key=True)
    sales_stage = models.CharField(max_length=200, blank=True, null=True)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_sales_stage'


class JkitepSalesStageSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_sales_stage_seq'


class JkitepSalesmanactivityrel(models.Model):
    smid = models.OneToOneField('JkitepUsers', models.DO_NOTHING, db_column='smid', primary_key=True)
    activityid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_salesmanactivityrel'
        unique_together = (('smid', 'activityid'),)


class JkitepSalesmanattachmentsrel(models.Model):
    smid = models.IntegerField(primary_key=True)
    attachmentsid = models.ForeignKey(JkitepAttachments, models.DO_NOTHING, db_column='attachmentsid')

    class Meta:
        managed = False
        db_table = 'jkitep_salesmanattachmentsrel'
        unique_together = (('smid', 'attachmentsid'),)


class JkitepSalesmanticketrel(models.Model):
    smid = models.OneToOneField('JkitepUsers', models.DO_NOTHING, db_column='smid', primary_key=True)
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_salesmanticketrel'
        unique_together = (('smid', 'id'),)


class JkitepSalesorder(models.Model):
    salesorderid = models.OneToOneField(JkitepCrmentity, models.DO_NOTHING, db_column='salesorderid', primary_key=True)
    subject = models.CharField(max_length=100, blank=True, null=True)
    potentialid = models.IntegerField(blank=True, null=True)
    customerno = models.CharField(max_length=100, blank=True, null=True)
    salesorder_no = models.CharField(max_length=100, blank=True, null=True)
    quoteid = models.IntegerField(blank=True, null=True)
    vendorterms = models.CharField(max_length=100, blank=True, null=True)
    contactid = models.IntegerField(blank=True, null=True)
    vendorid = models.ForeignKey('JkitepVendor', models.DO_NOTHING, db_column='vendorid', blank=True, null=True)
    duedate = models.DateField(blank=True, null=True)
    carrier = models.CharField(max_length=200, blank=True, null=True)
    pending = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    adjustment = models.DecimalField(max_digits=25, decimal_places=8, blank=True, null=True)
    salescommission = models.DecimalField(max_digits=25, decimal_places=3, blank=True, null=True)
    exciseduty = models.DecimalField(max_digits=25, decimal_places=3, blank=True, null=True)
    total = models.DecimalField(max_digits=25, decimal_places=8, blank=True, null=True)
    subtotal = models.DecimalField(max_digits=25, decimal_places=8, blank=True, null=True)
    taxtype = models.CharField(max_length=25, blank=True, null=True)
    discount_percent = models.DecimalField(max_digits=25, decimal_places=3, blank=True, null=True)
    discount_amount = models.DecimalField(max_digits=25, decimal_places=8, blank=True, null=True)
    s_h_amount = models.DecimalField(max_digits=25, decimal_places=8, blank=True, null=True)
    accountid = models.IntegerField(blank=True, null=True)
    terms_conditions = models.TextField(blank=True, null=True)
    purchaseorder = models.CharField(max_length=200, blank=True, null=True)
    sostatus = models.CharField(max_length=200, blank=True, null=True)
    currency_id = models.IntegerField()
    conversion_rate = models.DecimalField(max_digits=10, decimal_places=3)
    enable_recurring = models.IntegerField(blank=True, null=True)
    compound_taxes_info = models.TextField(blank=True, null=True)
    one_s_id = models.CharField(max_length=255, blank=True, null=True)
    fromsite = models.IntegerField(blank=True, null=True)
    pre_tax_total = models.DecimalField(max_digits=25, decimal_places=8, blank=True, null=True)
    s_h_percent = models.IntegerField(blank=True, null=True)
    spcompany = models.CharField(max_length=200, blank=True, null=True)
    tags = models.CharField(max_length=1, blank=True, null=True)
    region_id = models.IntegerField(blank=True, null=True)
    region_salesorder_id = models.CharField(max_length=100, blank=True, null=True)
    status_jk_so = models.CharField(max_length=700, blank=True, null=True)
    status_region_so = models.CharField(max_length=700, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_salesorder'


class JkitepSalesordercf(models.Model):
    salesorderid = models.OneToOneField(JkitepSalesorder, models.DO_NOTHING, db_column='salesorderid', primary_key=True)

    class Meta:
        managed = False
        db_table = 'jkitep_salesordercf'


class JkitepSalutationtype(models.Model):
    salutationid = models.AutoField(primary_key=True)
    salutationtype = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_salutationtype'


class JkitepSalutationtypeSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_salutationtype_seq'


class JkitepScheduledReports(models.Model):
    reportid = models.IntegerField(primary_key=True)
    recipients = models.TextField(blank=True, null=True)
    schedule = models.TextField(blank=True, null=True)
    format = models.CharField(max_length=10, blank=True, null=True)
    next_trigger_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'jkitep_scheduled_reports'


class JkitepSchedulereports(models.Model):
    reportid = models.IntegerField(blank=True, null=True)
    scheduleid = models.IntegerField(blank=True, null=True)
    recipients = models.TextField(blank=True, null=True)
    schdate = models.CharField(max_length=20, blank=True, null=True)
    schtime = models.TimeField(blank=True, null=True)
    schdayoftheweek = models.CharField(max_length=100, blank=True, null=True)
    schdayofthemonth = models.CharField(max_length=100, blank=True, null=True)
    schannualdates = models.CharField(max_length=500, blank=True, null=True)
    specificemails = models.CharField(max_length=500, blank=True, null=True)
    next_trigger_time = models.DateTimeField()
    fileformat = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_schedulereports'


class JkitepSchoolNumber(models.Model):
    school_numberid = models.AutoField(primary_key=True)
    school_number = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_school_number'


class JkitepSchoolNumberSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_school_number_seq'


class JkitepSchoolclasses(models.Model):
    schoolclassesid = models.IntegerField(primary_key=True)
    school_classes_no = models.CharField(max_length=100, blank=True, null=True)
    class_id = models.CharField(max_length=100, blank=True, null=True)
    school_id = models.CharField(max_length=100, blank=True, null=True)
    startbalance = models.CharField(max_length=100, blank=True, null=True)
    lang_instruc_class = models.CharField(max_length=200, blank=True, null=True)
    yyyy = models.CharField(max_length=100, blank=True, null=True)
    balance_sum = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_schoolclasses'


class JkitepSchoolclassesUserField(models.Model):
    recordid = models.IntegerField()
    userid = models.IntegerField()
    starred = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_schoolclasses_user_field'


class JkitepSchoolclassescf(models.Model):
    schoolclassesid = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'jkitep_schoolclassescf'


class JkitepSchools(models.Model):
    schoolsid = models.IntegerField(primary_key=True)
    schools_no = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    school_code = models.CharField(max_length=100, blank=True, null=True)
    found_school = models.DateField(blank=True, null=True)
    fax = models.CharField(max_length=100, blank=True, null=True)
    work_phone = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    region_id = models.CharField(max_length=100, blank=True, null=True)
    balance = models.DecimalField(max_digits=27, decimal_places=8, blank=True, null=True)
    school_number = models.CharField(max_length=400, blank=True, null=True)
    type_school = models.CharField(max_length=200, blank=True, null=True)
    type_ownership = models.CharField(max_length=200, blank=True, null=True)
    language_instruction = models.CharField(max_length=200, blank=True, null=True)
    school_address = models.CharField(max_length=200, blank=True, null=True)
    school_named = models.CharField(max_length=100, blank=True, null=True)
    region_school_id = models.CharField(max_length=100, blank=True, null=True)
    omsu = models.CharField(max_length=100, blank=True, null=True)
    bdate = models.DateField(blank=True, null=True)
    startbalance = models.CharField(max_length=100, blank=True, null=True)
    okpo = models.CharField(max_length=100, blank=True, null=True)
    fioadding = models.CharField(max_length=100, blank=True, null=True)
    posadding = models.CharField(max_length=100, blank=True, null=True)
    workingcount = models.IntegerField(blank=True, null=True)
    staffplancount = models.IntegerField(blank=True, null=True)
    stafffactcount = models.IntegerField(blank=True, null=True)
    staffwomcount = models.IntegerField(blank=True, null=True)
    staff5count = models.IntegerField(blank=True, null=True)
    staff1115count = models.IntegerField(blank=True, null=True)
    staff15count = models.IntegerField(blank=True, null=True)
    staffcer5tcount = models.IntegerField(blank=True, null=True)
    staffcert1count = models.IntegerField(blank=True, null=True)
    staffhiedcount = models.IntegerField(blank=True, null=True)
    staffneedcount = models.IntegerField(blank=True, null=True)
    staffmedcount = models.IntegerField(blank=True, null=True)
    mobadding = models.CharField(max_length=100, blank=True, null=True)
    mailadding = models.CharField(max_length=100, blank=True, null=True)
    staff510count = models.IntegerField(blank=True, null=True)
    totalsquare = models.CharField(max_length=100, blank=True, null=True)
    edusquare = models.CharField(max_length=100, blank=True, null=True)
    othsquare = models.CharField(max_length=100, blank=True, null=True)
    rentsquare = models.CharField(max_length=100, blank=True, null=True)
    buildingstate = models.CharField(max_length=100, blank=True, null=True)
    usestate = models.CharField(max_length=100, blank=True, null=True)
    sewerage = models.CharField(max_length=20, blank=True, null=True)
    hotwater = models.CharField(max_length=20, blank=True, null=True)
    toilets = models.CharField(max_length=20, blank=True, null=True)
    drinkwater = models.CharField(max_length=20, blank=True, null=True)
    washbasins = models.CharField(max_length=20, blank=True, null=True)
    spectoilet = models.CharField(max_length=20, blank=True, null=True)
    lifts = models.CharField(max_length=20, blank=True, null=True)
    classeson1 = models.CharField(max_length=20, blank=True, null=True)
    medpersons = models.CharField(max_length=20, blank=True, null=True)
    specedupers = models.CharField(max_length=20, blank=True, null=True)
    elecliblary = models.CharField(max_length=20, blank=True, null=True)
    compcount = models.IntegerField(blank=True, null=True)
    workcompcount = models.IntegerField(blank=True, null=True)
    intcompcount = models.IntegerField(blank=True, null=True)
    projector = models.CharField(max_length=20, blank=True, null=True)
    copierprinter = models.CharField(max_length=20, blank=True, null=True)
    inttype = models.CharField(max_length=100, blank=True, null=True)
    intspeed = models.CharField(max_length=100, blank=True, null=True)
    intmanagem = models.CharField(max_length=20, blank=True, null=True)
    intinallclas = models.CharField(max_length=20, blank=True, null=True)
    availeverywifi = models.CharField(max_length=20, blank=True, null=True)
    inttv = models.CharField(max_length=20, blank=True, null=True)
    physicslab = models.CharField(max_length=20, blank=True, null=True)
    chemistrylab = models.CharField(max_length=20, blank=True, null=True)
    biologylab = models.CharField(max_length=20, blank=True, null=True)
    hotfood = models.CharField(max_length=20, blank=True, null=True)
    booklibraryc = models.IntegerField(blank=True, null=True)
    tbooklibraryc = models.IntegerField(blank=True, null=True)
    pandus = models.CharField(max_length=20, blank=True, null=True)
    balance_sum = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_schools'


class JkitepSchoolsUserField(models.Model):
    recordid = models.IntegerField()
    userid = models.IntegerField()
    starred = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_schools_user_field'


class JkitepSchoolscf(models.Model):
    schoolsid = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'jkitep_schoolscf'


class JkitepSchoolstaff(models.Model):
    schoolstaffid = models.IntegerField(primary_key=True)
    school_staff_no = models.CharField(max_length=100, blank=True, null=True)
    firstname = models.CharField(max_length=100, blank=True, null=True)
    lastname = models.CharField(max_length=100, blank=True, null=True)
    patronymic = models.CharField(max_length=100, blank=True, null=True)
    pin_con = models.CharField(max_length=100, blank=True, null=True)
    mobile_phone = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    position_school_staff = models.CharField(max_length=300, blank=True, null=True)
    school_id = models.CharField(max_length=100, blank=True, null=True)
    role_name = models.CharField(max_length=100, blank=True, null=True)
    user_employee_id = models.CharField(max_length=100, blank=True, null=True)
    status_users = models.CharField(max_length=100, blank=True, null=True)
    class_id = models.CharField(max_length=100, blank=True, null=True)
    balance = models.CharField(max_length=100, blank=True, null=True)
    employees_id_user = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_schoolstaff'


class JkitepSchoolstaffUserField(models.Model):
    recordid = models.IntegerField()
    userid = models.IntegerField()
    starred = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_schoolstaff_user_field'


class JkitepSchoolstaffcf(models.Model):
    schoolstaffid = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'jkitep_schoolstaffcf'


class JkitepSeactivityrel(models.Model):
    crmid = models.OneToOneField(JkitepCrmentity, models.DO_NOTHING, db_column='crmid', primary_key=True)
    activityid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_seactivityrel'
        unique_together = (('crmid', 'activityid'),)


class JkitepSeactivityrelSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_seactivityrel_seq'


class JkitepSeattachmentsrel(models.Model):
    crmid = models.OneToOneField(JkitepCrmentity, models.DO_NOTHING, db_column='crmid', primary_key=True)
    attachmentsid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_seattachmentsrel'
        unique_together = (('crmid', 'attachmentsid'),)


class JkitepSelectcolumn(models.Model):
    queryid = models.OneToOneField('JkitepSelectquery', models.DO_NOTHING, db_column='queryid', primary_key=True)
    columnindex = models.IntegerField()
    columnname = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_selectcolumn'
        unique_together = (('queryid', 'columnindex'),)


class JkitepSelectquery(models.Model):
    queryid = models.IntegerField(primary_key=True)
    startindex = models.IntegerField(blank=True, null=True)
    numofobjects = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_selectquery'


class JkitepSelectquerySeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_selectquery_seq'


class JkitepSenotesrel(models.Model):
    crmid = models.OneToOneField(JkitepCrmentity, models.DO_NOTHING, db_column='crmid', primary_key=True)
    notesid = models.ForeignKey(JkitepNotes, models.DO_NOTHING, db_column='notesid')

    class Meta:
        managed = False
        db_table = 'jkitep_senotesrel'
        unique_together = (('crmid', 'notesid'),)


class JkitepSeproductsrel(models.Model):
    crmid = models.IntegerField(primary_key=True)
    productid = models.ForeignKey(JkitepProducts, models.DO_NOTHING, db_column='productid')
    setype = models.CharField(max_length=30)
    quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_seproductsrel'
        unique_together = (('crmid', 'productid'),)


class JkitepService(models.Model):
    serviceid = models.OneToOneField(JkitepCrmentity, models.DO_NOTHING, db_column='serviceid', primary_key=True)
    service_no = models.CharField(max_length=100)
    servicename = models.CharField(max_length=50)
    servicecategory = models.CharField(max_length=200, blank=True, null=True)
    qty_per_unit = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    unit_price = models.DecimalField(max_digits=25, decimal_places=8, blank=True, null=True)
    sales_start_date = models.DateField(blank=True, null=True)
    sales_end_date = models.DateField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)
    discontinued = models.IntegerField()
    service_usageunit = models.CharField(max_length=200, blank=True, null=True)
    website = models.CharField(max_length=100, blank=True, null=True)
    taxclass = models.CharField(max_length=200, blank=True, null=True)
    currency_id = models.IntegerField()
    commissionrate = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    unit_code = models.CharField(max_length=100, blank=True, null=True)
    one_s_id = models.CharField(max_length=255, blank=True, null=True)
    purchase_cost = models.DecimalField(max_digits=27, decimal_places=8, blank=True, null=True)
    tags = models.CharField(max_length=1, blank=True, null=True)
    subject_ser = models.CharField(max_length=100, blank=True, null=True)
    publisher = models.CharField(max_length=100, blank=True, null=True)
    class_num_ser = models.CharField(max_length=200, blank=True, null=True)
    textbook_lang = models.CharField(max_length=200, blank=True, null=True)
    text_book_name = models.CharField(max_length=700, blank=True, null=True)
    author = models.CharField(max_length=700, blank=True, null=True)
    rent_price = models.CharField(max_length=100, blank=True, null=True)
    textbook_author_id = models.CharField(max_length=100, blank=True, null=True)
    fondimage = models.CharField(max_length=255, blank=True, null=True)
    rec_price = models.CharField(max_length=100, blank=True, null=True)
    publishyear = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_service'


class JkitepServiceUsageunit(models.Model):
    service_usageunitid = models.AutoField(primary_key=True)
    service_usageunit = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_service_usageunit'


class JkitepServiceUsageunitSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_service_usageunit_seq'


class JkitepServicecategory(models.Model):
    servicecategoryid = models.AutoField(primary_key=True)
    servicecategory = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_servicecategory'


class JkitepServicecategorySeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_servicecategory_seq'


class JkitepServicecf(models.Model):
    serviceid = models.OneToOneField(JkitepService, models.DO_NOTHING, db_column='serviceid', primary_key=True)

    class Meta:
        managed = False
        db_table = 'jkitep_servicecf'


class JkitepServicecontracts(models.Model):
    servicecontractsid = models.ForeignKey(JkitepCrmentity, models.DO_NOTHING, db_column='servicecontractsid', blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    sc_related_to = models.IntegerField(blank=True, null=True)
    tracking_unit = models.CharField(max_length=100, blank=True, null=True)
    total_units = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    used_units = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    subject = models.CharField(max_length=100, blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    planned_duration = models.CharField(max_length=256, blank=True, null=True)
    actual_duration = models.CharField(max_length=256, blank=True, null=True)
    contract_status = models.CharField(max_length=200, blank=True, null=True)
    priority = models.CharField(max_length=200, blank=True, null=True)
    contract_type = models.CharField(max_length=200, blank=True, null=True)
    progress = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    contract_no = models.CharField(max_length=100, blank=True, null=True)
    tags = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_servicecontracts'


class JkitepServicecontractscf(models.Model):
    servicecontractsid = models.OneToOneField(JkitepServicecontracts, models.DO_NOTHING, db_column='servicecontractsid', primary_key=True)

    class Meta:
        managed = False
        db_table = 'jkitep_servicecontractscf'


class JkitepSeticketsrel(models.Model):
    crmid = models.IntegerField(primary_key=True)
    ticketid = models.ForeignKey('JkitepTroubletickets', models.DO_NOTHING, db_column='ticketid')

    class Meta:
        managed = False
        db_table = 'jkitep_seticketsrel'
        unique_together = (('crmid', 'ticketid'),)


class JkitepSettingsBlocks(models.Model):
    blockid = models.IntegerField(primary_key=True)
    label = models.CharField(max_length=250, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_settings_blocks'


class JkitepSettingsBlocksSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_settings_blocks_seq'


class JkitepSettingsField(models.Model):
    fieldid = models.IntegerField(primary_key=True)
    blockid = models.ForeignKey(JkitepSettingsBlocks, models.DO_NOTHING, db_column='blockid', blank=True, null=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    iconpath = models.CharField(max_length=300, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    linkto = models.TextField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    pinned = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_settings_field'


class JkitepSettingsFieldSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_settings_field_seq'


class JkitepSharedcalendar(models.Model):
    userid = models.IntegerField(primary_key=True)
    sharedid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_sharedcalendar'
        unique_together = (('userid', 'sharedid'),)


class JkitepShareduserinfo(models.Model):
    userid = models.IntegerField()
    shareduserid = models.IntegerField()
    color = models.CharField(max_length=50, blank=True, null=True)
    visible = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_shareduserinfo'


class JkitepShippingtaxinfo(models.Model):
    taxid = models.IntegerField(primary_key=True)
    taxname = models.CharField(max_length=50, blank=True, null=True)
    taxlabel = models.CharField(max_length=50, blank=True, null=True)
    percentage = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    method = models.CharField(max_length=10, blank=True, null=True)
    type = models.CharField(max_length=10, blank=True, null=True)
    compoundon = models.CharField(max_length=400, blank=True, null=True)
    regions = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_shippingtaxinfo'


class JkitepShippingtaxinfoSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_shippingtaxinfo_seq'


class JkitepShorturls(models.Model):
    uid = models.CharField(max_length=50, blank=True, null=True)
    handler_path = models.CharField(max_length=400, blank=True, null=True)
    handler_class = models.CharField(max_length=100, blank=True, null=True)
    handler_function = models.CharField(max_length=100, blank=True, null=True)
    handler_data = models.CharField(max_length=255, blank=True, null=True)
    onetime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_shorturls'


class JkitepSmsnotifier(models.Model):
    smsnotifierid = models.OneToOneField(JkitepCrmentity, models.DO_NOTHING, db_column='smsnotifierid', primary_key=True)
    message = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_smsnotifier'


class JkitepSmsnotifierServers(models.Model):
    password = models.CharField(max_length=255, blank=True, null=True)
    isactive = models.IntegerField(blank=True, null=True)
    providertype = models.CharField(max_length=50, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    parameters = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_smsnotifier_servers'


class JkitepSmsnotifierStatus(models.Model):
    smsnotifierid = models.IntegerField(blank=True, null=True)
    tonumber = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    smsmessageid = models.CharField(max_length=50, blank=True, null=True)
    needlookup = models.IntegerField(blank=True, null=True)
    statusid = models.AutoField(primary_key=True)
    statusmessage = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_smsnotifier_status'


class JkitepSmsnotifiercf(models.Model):
    smsnotifierid = models.OneToOneField(JkitepSmsnotifier, models.DO_NOTHING, db_column='smsnotifierid', primary_key=True)

    class Meta:
        managed = False
        db_table = 'jkitep_smsnotifiercf'


class JkitepSoapservice(models.Model):
    id = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=25, blank=True, null=True)
    sessionid = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_soapservice'


class JkitepSobillads(models.Model):
    sobilladdressid = models.OneToOneField(JkitepSalesorder, models.DO_NOTHING, db_column='sobilladdressid', primary_key=True)
    bill_city = models.CharField(max_length=30, blank=True, null=True)
    bill_code = models.CharField(max_length=30, blank=True, null=True)
    bill_country = models.CharField(max_length=30, blank=True, null=True)
    bill_state = models.CharField(max_length=30, blank=True, null=True)
    bill_street = models.CharField(max_length=250, blank=True, null=True)
    bill_pobox = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_sobillads'


class JkitepSoshipads(models.Model):
    soshipaddressid = models.OneToOneField(JkitepSalesorder, models.DO_NOTHING, db_column='soshipaddressid', primary_key=True)
    ship_city = models.CharField(max_length=30, blank=True, null=True)
    ship_code = models.CharField(max_length=30, blank=True, null=True)
    ship_country = models.CharField(max_length=30, blank=True, null=True)
    ship_state = models.CharField(max_length=30, blank=True, null=True)
    ship_street = models.CharField(max_length=250, blank=True, null=True)
    ship_pobox = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_soshipads'


class JkitepSostatus(models.Model):
    sostatusid = models.AutoField(primary_key=True)
    sostatus = models.CharField(unique=True, max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_sostatus'


class JkitepSostatusSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_sostatus_seq'


class JkitepSostatushistory(models.Model):
    historyid = models.AutoField(primary_key=True)
    salesorderid = models.ForeignKey(JkitepSalesorder, models.DO_NOTHING, db_column='salesorderid')
    accountname = models.CharField(max_length=100, blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    sostatus = models.CharField(max_length=200, blank=True, null=True)
    lastmodified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_sostatushistory'


class JkitepSostatushistorySeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_sostatushistory_seq'


class JkitepSpAct(models.Model):
    actid = models.OneToOneField(JkitepCrmentity, models.DO_NOTHING, db_column='actid', primary_key=True)
    salesorderid = models.IntegerField(blank=True, null=True)
    contactid = models.IntegerField(blank=True, null=True)
    actdate = models.DateField(blank=True, null=True)
    adjustment = models.DecimalField(max_digits=25, decimal_places=8, blank=True, null=True)
    subtotal = models.DecimalField(max_digits=25, decimal_places=8, blank=True, null=True)
    total = models.DecimalField(max_digits=25, decimal_places=8, blank=True, null=True)
    taxtype = models.CharField(max_length=25, blank=True, null=True)
    discount_percent = models.DecimalField(max_digits=25, decimal_places=8, blank=True, null=True)
    discount_amount = models.DecimalField(max_digits=25, decimal_places=8, blank=True, null=True)
    s_h_amount = models.DecimalField(max_digits=25, decimal_places=8, blank=True, null=True)
    shipping = models.CharField(max_length=100, blank=True, null=True)
    accountid = models.IntegerField(blank=True, null=True)
    sp_actstatus = models.CharField(max_length=200, blank=True, null=True)
    act_no = models.CharField(max_length=100, blank=True, null=True)
    currency_id = models.IntegerField()
    conversion_rate = models.DecimalField(max_digits=10, decimal_places=3)
    spcompany = models.CharField(max_length=200, blank=True, null=True)
    pre_tax_total = models.DecimalField(max_digits=25, decimal_places=8, blank=True, null=True)
    s_h_percent = models.IntegerField(blank=True, null=True)
    compound_taxes_info = models.TextField(blank=True, null=True)
    region_id = models.IntegerField(blank=True, null=True)
    tags = models.CharField(max_length=1, blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_sp_act'


class JkitepSpActbillads(models.Model):
    actbilladdressid = models.OneToOneField(JkitepSpAct, models.DO_NOTHING, db_column='actbilladdressid', primary_key=True)
    bill_city = models.CharField(max_length=30, blank=True, null=True)
    bill_code = models.CharField(max_length=30, blank=True, null=True)
    bill_country = models.CharField(max_length=30, blank=True, null=True)
    bill_state = models.CharField(max_length=30, blank=True, null=True)
    bill_street = models.CharField(max_length=250, blank=True, null=True)
    bill_pobox = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_sp_actbillads'


class JkitepSpActcf(models.Model):
    actid = models.OneToOneField(JkitepSpAct, models.DO_NOTHING, db_column='actid', primary_key=True)

    class Meta:
        managed = False
        db_table = 'jkitep_sp_actcf'


class JkitepSpActshipads(models.Model):
    actshipaddressid = models.OneToOneField(JkitepSpAct, models.DO_NOTHING, db_column='actshipaddressid', primary_key=True)
    ship_city = models.CharField(max_length=30, blank=True, null=True)
    ship_code = models.CharField(max_length=30, blank=True, null=True)
    ship_country = models.CharField(max_length=30, blank=True, null=True)
    ship_state = models.CharField(max_length=30, blank=True, null=True)
    ship_street = models.CharField(max_length=250, blank=True, null=True)
    ship_pobox = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_sp_actshipads'


class JkitepSpActstatus(models.Model):
    sp_actstatusid = models.AutoField(primary_key=True)
    sp_actstatus = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_sp_actstatus'


class JkitepSpActstatusSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_sp_actstatus_seq'


class JkitepSpActstatushistory(models.Model):
    historyid = models.AutoField(primary_key=True)
    actid = models.ForeignKey(JkitepSpAct, models.DO_NOTHING, db_column='actid')
    accountname = models.CharField(max_length=100, blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    sp_actstatus = models.CharField(max_length=200, blank=True, null=True)
    lastmodified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_sp_actstatushistory'


class JkitepSpBlocksConfiguration(models.Model):
    sp_blocks_configuration_id = models.IntegerField(blank=True, null=True)
    module_name = models.CharField(max_length=255, blank=True, null=True)
    field_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_sp_blocks_configuration'


class JkitepSpBlocksConfiguration2Blocks(models.Model):
    sp_blocks_configuration_id = models.IntegerField(blank=True, null=True)
    block_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_sp_blocks_configuration2blocks'


class JkitepSpBlocksConfiguration2Values(models.Model):
    sp_blocks_configuration_id = models.IntegerField(blank=True, null=True)
    field_value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_sp_blocks_configuration2values'


class JkitepSpBlocksConfigurationSeq(models.Model):
    id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_sp_blocks_configuration_seq'


class JkitepSpConsignment(models.Model):
    consignmentid = models.OneToOneField(JkitepCrmentity, models.DO_NOTHING, db_column='consignmentid', primary_key=True)
    salesorderid = models.IntegerField(blank=True, null=True)
    invoiceid = models.IntegerField(blank=True, null=True)
    contactid = models.IntegerField(blank=True, null=True)
    consignmentdate = models.DateField(blank=True, null=True)
    adjustment = models.DecimalField(max_digits=25, decimal_places=8, blank=True, null=True)
    subtotal = models.DecimalField(max_digits=25, decimal_places=8, blank=True, null=True)
    total = models.DecimalField(max_digits=25, decimal_places=8, blank=True, null=True)
    taxtype = models.CharField(max_length=25, blank=True, null=True)
    discount_percent = models.DecimalField(max_digits=25, decimal_places=8, blank=True, null=True)
    discount_amount = models.DecimalField(max_digits=25, decimal_places=8, blank=True, null=True)
    s_h_amount = models.DecimalField(max_digits=25, decimal_places=8, blank=True, null=True)
    shipping = models.CharField(max_length=100, blank=True, null=True)
    accountid = models.IntegerField(blank=True, null=True)
    sp_consignmentstatus = models.CharField(max_length=200, blank=True, null=True)
    consignment_no = models.CharField(max_length=100, blank=True, null=True)
    currency_id = models.IntegerField()
    conversion_rate = models.DecimalField(max_digits=10, decimal_places=3)
    has_goods_consignment = models.CharField(max_length=3, blank=True, null=True)
    goods_consignment_no = models.IntegerField(blank=True, null=True)
    spcompany = models.CharField(max_length=200, blank=True, null=True)
    pre_tax_total = models.DecimalField(max_digits=25, decimal_places=8, blank=True, null=True)
    s_h_percent = models.IntegerField(blank=True, null=True)
    compound_taxes_info = models.TextField(blank=True, null=True)
    region_id = models.IntegerField(blank=True, null=True)
    tags = models.CharField(max_length=1, blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_sp_consignment'


class JkitepSpConsignmentbillads(models.Model):
    consignmentbilladdressid = models.OneToOneField(JkitepSpConsignment, models.DO_NOTHING, db_column='consignmentbilladdressid', primary_key=True)
    bill_city = models.CharField(max_length=30, blank=True, null=True)
    bill_code = models.CharField(max_length=30, blank=True, null=True)
    bill_country = models.CharField(max_length=30, blank=True, null=True)
    bill_state = models.CharField(max_length=30, blank=True, null=True)
    bill_street = models.CharField(max_length=250, blank=True, null=True)
    bill_pobox = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_sp_consignmentbillads'


class JkitepSpConsignmentcf(models.Model):
    consignmentid = models.OneToOneField(JkitepSpConsignment, models.DO_NOTHING, db_column='consignmentid', primary_key=True)

    class Meta:
        managed = False
        db_table = 'jkitep_sp_consignmentcf'


class JkitepSpConsignmentshipads(models.Model):
    consignmentshipaddressid = models.OneToOneField(JkitepSpConsignment, models.DO_NOTHING, db_column='consignmentshipaddressid', primary_key=True)
    ship_city = models.CharField(max_length=30, blank=True, null=True)
    ship_code = models.CharField(max_length=30, blank=True, null=True)
    ship_country = models.CharField(max_length=30, blank=True, null=True)
    ship_state = models.CharField(max_length=30, blank=True, null=True)
    ship_street = models.CharField(max_length=250, blank=True, null=True)
    ship_pobox = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_sp_consignmentshipads'


class JkitepSpConsignmentstatus(models.Model):
    sp_consignmentstatusid = models.AutoField(primary_key=True)
    sp_consignmentstatus = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_sp_consignmentstatus'


class JkitepSpConsignmentstatusSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_sp_consignmentstatus_seq'


class JkitepSpConsignmentstatushistory(models.Model):
    historyid = models.AutoField(primary_key=True)
    consignmentid = models.ForeignKey(JkitepSpConsignment, models.DO_NOTHING, db_column='consignmentid')
    accountname = models.CharField(max_length=100, blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    sp_consignmentstatus = models.CharField(max_length=200, blank=True, null=True)
    lastmodified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_sp_consignmentstatushistory'


class JkitepSpSocialconnector(models.Model):
    socialconnectorid = models.ForeignKey(JkitepCrmentity, models.DO_NOTHING, db_column='socialconnectorid', blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    vk_status = models.CharField(max_length=255, blank=True, null=True)
    tw_status = models.CharField(max_length=255, blank=True, null=True)
    vk_message_id = models.CharField(max_length=255, blank=True, null=True)
    tw_message_id = models.CharField(max_length=255, blank=True, null=True)
    message_datetime = models.DateTimeField()
    tags = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_sp_socialconnector'


class JkitepSpSocialconnectorProviders(models.Model):
    id = models.IntegerField(primary_key=True)
    provider_name = models.CharField(max_length=45)
    provider_domen = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_sp_socialconnector_providers'


class JkitepSpSocialconnectorSettings(models.Model):
    key = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_sp_socialconnector_settings'


class JkitepSpSocialconnectorcf(models.Model):
    socialconnectorid = models.OneToOneField(JkitepSpSocialconnector, models.DO_NOTHING, db_column='socialconnectorid', primary_key=True)

    class Meta:
        managed = False
        db_table = 'jkitep_sp_socialconnectorcf'


class JkitepSpVoipDefaultProvider(models.Model):
    default_provider = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_sp_voip_default_provider'


class JkitepSpVoipintegrationOptions(models.Model):
    name = models.CharField(unique=True, max_length=255)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_sp_voipintegration_options'


class JkitepSpVoipintegrationSettings(models.Model):
    id = models.IntegerField(blank=True, null=True)
    provider_name = models.CharField(max_length=255, blank=True, null=True)
    field_name = models.CharField(unique=True, max_length=255, blank=True, null=True)
    field_label = models.CharField(max_length=255, blank=True, null=True)
    field_value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_sp_voipintegration_settings'


class JkitepSpcompany(models.Model):
    spcompanyid = models.AutoField(primary_key=True)
    spcompany = models.CharField(unique=True, max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_spcompany'


class JkitepSpcompanySeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_spcompany_seq'


class JkitepSpstatus(models.Model):
    spstatusid = models.AutoField(primary_key=True)
    spstatus = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_spstatus'


class JkitepSpstatusSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_spstatus_seq'


class JkitepSqltimelog(models.Model):
    id = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=10, blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    started = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    ended = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    loggedon = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_sqltimelog'


class JkitepStartHour(models.Model):
    start_hourid = models.AutoField(primary_key=True)
    start_hour = models.CharField(max_length=200)
    sortorderid = models.IntegerField(blank=True, null=True)
    presence = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_start_hour'


class JkitepStartHourSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_start_hour_seq'


class JkitepStatemenStatus(models.Model):
    statemen_statusid = models.AutoField(primary_key=True)
    statemen_status = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_statemen_status'


class JkitepStatemenStatusSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_statemen_status_seq'


class JkitepStatementissuereturntextbooks(models.Model):
    statementissuereturntextbooksid = models.IntegerField(primary_key=True)
    statement_no = models.CharField(max_length=100, blank=True, null=True)
    textbook_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_statementissuereturntextbooks'


class JkitepStatementissuereturntextbooksUserField(models.Model):
    recordid = models.IntegerField()
    userid = models.IntegerField()
    starred = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_statementissuereturntextbooks_user_field'


class JkitepStatementissuereturntextbookscf(models.Model):
    statementissuereturntextbooksid = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'jkitep_statementissuereturntextbookscf'


class JkitepStatementtextbooks(models.Model):
    statementtextbooksid = models.IntegerField(primary_key=True)
    statement_no = models.CharField(max_length=100, blank=True, null=True)
    textbook_id = models.CharField(max_length=100, blank=True, null=True)
    student_id = models.CharField(max_length=100, blank=True, null=True)
    date_issue = models.DateField(blank=True, null=True)
    return_date = models.DateField(blank=True, null=True)
    statemen_status = models.CharField(max_length=300, blank=True, null=True)
    yyyy = models.CharField(max_length=100, blank=True, null=True)
    billed_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_statementtextbooks'


class JkitepStatementtextbooksUserField(models.Model):
    recordid = models.IntegerField()
    userid = models.IntegerField()
    starred = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_statementtextbooks_user_field'


class JkitepStatementtextbookscf(models.Model):
    statementtextbooksid = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'jkitep_statementtextbookscf'


class JkitepStatus(models.Model):
    statusid = models.AutoField(primary_key=True)
    status = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_status'


class JkitepStatusBilled(models.Model):
    status_billedid = models.AutoField(primary_key=True)
    status_billed = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_status_billed'


class JkitepStatusBilledSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_status_billed_seq'


class JkitepStatusJkPur(models.Model):
    status_jk_purid = models.AutoField(primary_key=True)
    status_jk_pur = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_status_jk_pur'


class JkitepStatusJkPurSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_status_jk_pur_seq'


class JkitepStatusJkSo(models.Model):
    status_jk_soid = models.AutoField(primary_key=True)
    status_jk_so = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_status_jk_so'


class JkitepStatusJkSoSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_status_jk_so_seq'


class JkitepStatusRegionPur(models.Model):
    status_region_purid = models.AutoField(primary_key=True)
    status_region_pur = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_status_region_pur'


class JkitepStatusRegionPurSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_status_region_pur_seq'


class JkitepStatusRegionSo(models.Model):
    status_region_soid = models.AutoField(primary_key=True)
    status_region_so = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_status_region_so'


class JkitepStatusRegionSoSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_status_region_so_seq'


class JkitepStatusSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_status_seq'


class JkitepStatusUsers(models.Model):
    status_usersid = models.AutoField(primary_key=True)
    status_users = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_status_users'


class JkitepStatusUsersArea(models.Model):
    status_users_areaid = models.AutoField(primary_key=True)
    status_users_area = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_status_users_area'


class JkitepStatusUsersAreaSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_status_users_area_seq'


class JkitepStatusUsersEmp(models.Model):
    status_users_empid = models.AutoField(primary_key=True)
    status_users_emp = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_status_users_emp'


class JkitepStatusUsersEmpSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_status_users_emp_seq'


class JkitepStatusUsersSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_status_users_seq'


class JkitepStatusUsersVendor(models.Model):
    status_users_vendorid = models.AutoField(primary_key=True)
    status_users_vendor = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_status_users_vendor'


class JkitepStatusUsersVendorSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_status_users_vendor_seq'


class JkitepSupplierStatusPur(models.Model):
    supplier_status_purid = models.AutoField(primary_key=True)
    supplier_status_pur = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_supplier_status_pur'


class JkitepSupplierStatusPurSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_supplier_status_pur_seq'


class JkitepSystems(models.Model):
    id = models.IntegerField(primary_key=True)
    server = models.CharField(max_length=100, blank=True, null=True)
    server_port = models.IntegerField(blank=True, null=True)
    server_username = models.CharField(max_length=100, blank=True, null=True)
    server_password = models.CharField(max_length=100, blank=True, null=True)
    server_type = models.CharField(max_length=20, blank=True, null=True)
    smtp_auth = models.CharField(max_length=5, blank=True, null=True)
    server_path = models.CharField(max_length=256, blank=True, null=True)
    from_email_field = models.CharField(max_length=50, blank=True, null=True)
    server_tls = models.CharField(max_length=20, blank=True, null=True)
    from_name = models.CharField(max_length=200, blank=True, null=True)
    use_sendmail = models.CharField(max_length=5, blank=True, null=True)
    use_mail_account = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_systems'


class JkitepTab(models.Model):
    tabid = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=50)
    presence = models.IntegerField()
    tabsequence = models.IntegerField(blank=True, null=True)
    tablabel = models.CharField(max_length=100, blank=True, null=True)
    modifiedby = models.IntegerField(blank=True, null=True)
    modifiedtime = models.IntegerField(blank=True, null=True)
    customized = models.IntegerField(blank=True, null=True)
    ownedby = models.IntegerField(blank=True, null=True)
    isentitytype = models.IntegerField()
    trial = models.IntegerField()
    version = models.CharField(max_length=10, blank=True, null=True)
    parent = models.CharField(max_length=30, blank=True, null=True)
    source = models.CharField(max_length=255, blank=True, null=True)
    issyncable = models.IntegerField(blank=True, null=True)
    allowduplicates = models.IntegerField(blank=True, null=True)
    sync_action_for_duplicates = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_tab'


class JkitepTabInfo(models.Model):
    tabid = models.ForeignKey(JkitepTab, models.DO_NOTHING, db_column='tabid', blank=True, null=True)
    prefname = models.CharField(max_length=256, blank=True, null=True)
    prefvalue = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_tab_info'


class JkitepTaskpriority(models.Model):
    taskpriorityid = models.AutoField(primary_key=True)
    taskpriority = models.CharField(max_length=200, blank=True, null=True)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_taskpriority'


class JkitepTaskprioritySeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_taskpriority_seq'


class JkitepTaskstatus(models.Model):
    taskstatusid = models.AutoField(primary_key=True)
    taskstatus = models.CharField(max_length=200, blank=True, null=True)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_taskstatus'


class JkitepTaskstatusSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_taskstatus_seq'


class JkitepTaxclass(models.Model):
    taxclassid = models.AutoField(primary_key=True)
    taxclass = models.CharField(unique=True, max_length=200)
    sortorderid = models.IntegerField()
    presence = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_taxclass'


class JkitepTaxclassSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_taxclass_seq'


class JkitepTaxregions(models.Model):
    regionid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'jkitep_taxregions'


class JkitepTenderStatus(models.Model):
    tender_statusid = models.AutoField(primary_key=True)
    tender_status = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_tender_status'


class JkitepTenderStatusSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_tender_status_seq'


class JkitepTextBookName(models.Model):
    text_book_nameid = models.AutoField(primary_key=True)
    text_book_name = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_text_book_name'


class JkitepTextBookNameSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_text_book_name_seq'


class JkitepTextbookLang(models.Model):
    textbook_langid = models.AutoField(primary_key=True)
    textbook_lang = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_textbook_lang'


class JkitepTextbookLangSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_textbook_lang_seq'


class JkitepTextbookState(models.Model):
    textbook_stateid = models.AutoField(primary_key=True)
    textbook_state = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_textbook_state'


class JkitepTextbookStateSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_textbook_state_seq'


class JkitepTextbookapplications(models.Model):
    textbookapplicationsid = models.IntegerField(primary_key=True)
    textbook_application_no = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    service_id = models.CharField(max_length=100, blank=True, null=True)
    quote_id = models.CharField(max_length=100, blank=True, null=True)
    quantity = models.CharField(max_length=100, blank=True, null=True)
    region_id = models.CharField(max_length=100, blank=True, null=True)
    so_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_textbookapplications'


class JkitepTextbookapplicationsUserField(models.Model):
    recordid = models.IntegerField()
    userid = models.IntegerField()
    starred = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_textbookapplications_user_field'


class JkitepTextbookapplicationscf(models.Model):
    textbookapplicationsid = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'jkitep_textbookapplicationscf'


class JkitepTextbookauthor(models.Model):
    textbookauthorid = models.IntegerField(primary_key=True)
    textbook_author_no = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_textbookauthor'


class JkitepTextbookauthorUserField(models.Model):
    recordid = models.IntegerField()
    userid = models.IntegerField()
    starred = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_textbookauthor_user_field'


class JkitepTextbookauthorcf(models.Model):
    textbookauthorid = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'jkitep_textbookauthorcf'


class JkitepTicketcategories(models.Model):
    ticketcategories_id = models.AutoField(primary_key=True)
    ticketcategories = models.CharField(max_length=200, blank=True, null=True)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_ticketcategories'


class JkitepTicketcategoriesSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_ticketcategories_seq'


class JkitepTicketcf(models.Model):
    ticketid = models.OneToOneField('JkitepTroubletickets', models.DO_NOTHING, db_column='ticketid', primary_key=True)
    from_portal = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_ticketcf'


class JkitepTicketcomments(models.Model):
    commentid = models.AutoField(primary_key=True)
    ticketid = models.ForeignKey('JkitepTroubletickets', models.DO_NOTHING, db_column='ticketid', blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    ownerid = models.IntegerField()
    ownertype = models.CharField(max_length=10, blank=True, null=True)
    createdtime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'jkitep_ticketcomments'


class JkitepTicketpriorities(models.Model):
    ticketpriorities_id = models.AutoField(primary_key=True)
    ticketpriorities = models.CharField(max_length=200, blank=True, null=True)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_ticketpriorities'


class JkitepTicketprioritiesSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_ticketpriorities_seq'


class JkitepTicketseverities(models.Model):
    ticketseverities_id = models.AutoField(primary_key=True)
    ticketseverities = models.CharField(max_length=200, blank=True, null=True)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_ticketseverities'


class JkitepTicketseveritiesSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_ticketseverities_seq'


class JkitepTicketstatus(models.Model):
    ticketstatus_id = models.AutoField(primary_key=True)
    ticketstatus = models.CharField(max_length=200, blank=True, null=True)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_ticketstatus'


class JkitepTicketstatusSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_ticketstatus_seq'


class JkitepTimeZone(models.Model):
    time_zoneid = models.AutoField(primary_key=True)
    time_zone = models.CharField(max_length=200)
    sortorderid = models.IntegerField()
    presence = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_time_zone'


class JkitepTimeZoneSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_time_zone_seq'


class JkitepTmpReadGroupRelSharingPer(models.Model):
    userid = models.OneToOneField('JkitepUsers', models.DO_NOTHING, db_column='userid', primary_key=True)
    tabid = models.IntegerField()
    relatedtabid = models.IntegerField()
    sharedgroupid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_tmp_read_group_rel_sharing_per'
        unique_together = (('userid', 'tabid', 'relatedtabid', 'sharedgroupid'),)


class JkitepTmpReadGroupSharingPer(models.Model):
    userid = models.OneToOneField('JkitepUsers', models.DO_NOTHING, db_column='userid', primary_key=True)
    tabid = models.IntegerField()
    sharedgroupid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_tmp_read_group_sharing_per'
        unique_together = (('userid', 'tabid', 'sharedgroupid'),)


class JkitepTmpReadUserRelSharingPer(models.Model):
    userid = models.OneToOneField('JkitepUsers', models.DO_NOTHING, db_column='userid', primary_key=True)
    tabid = models.IntegerField()
    relatedtabid = models.IntegerField()
    shareduserid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_tmp_read_user_rel_sharing_per'
        unique_together = (('userid', 'tabid', 'relatedtabid', 'shareduserid'),)


class JkitepTmpReadUserSharingPer(models.Model):
    userid = models.OneToOneField('JkitepUsers', models.DO_NOTHING, db_column='userid', primary_key=True)
    tabid = models.IntegerField()
    shareduserid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_tmp_read_user_sharing_per'
        unique_together = (('userid', 'tabid', 'shareduserid'),)


class JkitepTmpWriteGroupRelSharingPer(models.Model):
    userid = models.OneToOneField('JkitepUsers', models.DO_NOTHING, db_column='userid', primary_key=True)
    tabid = models.IntegerField()
    relatedtabid = models.IntegerField()
    sharedgroupid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_tmp_write_group_rel_sharing_per'
        unique_together = (('userid', 'tabid', 'relatedtabid', 'sharedgroupid'),)


class JkitepTmpWriteGroupSharingPer(models.Model):
    userid = models.OneToOneField('JkitepUsers', models.DO_NOTHING, db_column='userid', primary_key=True)
    tabid = models.IntegerField()
    sharedgroupid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_tmp_write_group_sharing_per'
        unique_together = (('userid', 'tabid', 'sharedgroupid'),)


class JkitepTmpWriteUserRelSharingPer(models.Model):
    userid = models.OneToOneField('JkitepUsers', models.DO_NOTHING, db_column='userid', primary_key=True)
    tabid = models.IntegerField()
    relatedtabid = models.IntegerField()
    shareduserid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_tmp_write_user_rel_sharing_per'
        unique_together = (('userid', 'tabid', 'relatedtabid', 'shareduserid'),)


class JkitepTmpWriteUserSharingPer(models.Model):
    userid = models.OneToOneField('JkitepUsers', models.DO_NOTHING, db_column='userid', primary_key=True)
    tabid = models.IntegerField()
    shareduserid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_tmp_write_user_sharing_per'
        unique_together = (('userid', 'tabid', 'shareduserid'),)


class JkitepTracker(models.Model):
    user_id = models.CharField(max_length=36, blank=True, null=True)
    module_name = models.CharField(max_length=25, blank=True, null=True)
    item_id = models.CharField(max_length=36, blank=True, null=True)
    item_summary = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_tracker'


class JkitepTrackingUnit(models.Model):
    tracking_unitid = models.AutoField(primary_key=True)
    tracking_unit = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_tracking_unit'


class JkitepTrackingUnitSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_tracking_unit_seq'


class JkitepTransition(models.Model):
    transitionid = models.IntegerField(primary_key=True)
    trn_no = models.CharField(max_length=100, blank=True, null=True)
    student_id = models.CharField(max_length=100, blank=True, null=True)
    school = models.CharField(max_length=100, blank=True, null=True)
    reasontrn = models.CharField(max_length=100, blank=True, null=True)
    yyyy = models.CharField(max_length=100, blank=True, null=True)
    bname = models.CharField(max_length=100, blank=True, null=True)
    pedadvice = models.CharField(max_length=100, blank=True, null=True)
    discount = models.CharField(max_length=100, blank=True, null=True)
    isagreedoc = models.CharField(max_length=100, blank=True, null=True)
    agreedoc = models.CharField(max_length=100, blank=True, null=True)
    class_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_transition'


class JkitepTransitionUserField(models.Model):
    recordid = models.IntegerField()
    userid = models.IntegerField()
    starred = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_transition_user_field'


class JkitepTransitioncf(models.Model):
    transitionid = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'jkitep_transitioncf'


class JkitepTroubletickets(models.Model):
    ticketid = models.OneToOneField(JkitepCrmentity, models.DO_NOTHING, db_column='ticketid', primary_key=True)
    ticket_no = models.CharField(max_length=100)
    groupname = models.CharField(max_length=100, blank=True, null=True)
    parent_id = models.CharField(max_length=100, blank=True, null=True)
    product_id = models.CharField(max_length=100, blank=True, null=True)
    priority = models.CharField(max_length=200, blank=True, null=True)
    severity = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=200, blank=True, null=True)
    category = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=255)
    solution = models.TextField(blank=True, null=True)
    update_log = models.TextField(blank=True, null=True)
    version_id = models.IntegerField(blank=True, null=True)
    hours = models.DecimalField(max_digits=25, decimal_places=8, blank=True, null=True)
    days = models.DecimalField(max_digits=25, decimal_places=8, blank=True, null=True)
    contact_id = models.IntegerField(blank=True, null=True)
    tags = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_troubletickets'


class JkitepTwStatus(models.Model):
    tw_statusid = models.AutoField(primary_key=True)
    tw_status = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_tw_status'


class JkitepTwStatusSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_tw_status_seq'


class JkitepType(models.Model):
    typeid = models.AutoField(primary_key=True)
    type = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_type'


class JkitepTypeOwnership(models.Model):
    type_ownershipid = models.AutoField(primary_key=True)
    type_ownership = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_type_ownership'


class JkitepTypeOwnershipSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_type_ownership_seq'


class JkitepTypePayment(models.Model):
    type_paymentid = models.AutoField(primary_key=True)
    type_payment = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_type_payment'


class JkitepTypePaymentSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_type_payment_seq'


class JkitepTypeSchool(models.Model):
    type_schoolid = models.AutoField(primary_key=True)
    type_school = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_type_school'


class JkitepTypeSchoolSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_type_school_seq'


class JkitepTypeSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_type_seq'


class JkitepUsageunit(models.Model):
    usageunitid = models.AutoField(primary_key=True)
    usageunit = models.CharField(unique=True, max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_usageunit'


class JkitepUsageunitSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_usageunit_seq'


class JkitepUser2Mergefields(models.Model):
    userid = models.IntegerField(blank=True, null=True)
    tabid = models.IntegerField(blank=True, null=True)
    fieldid = models.IntegerField(blank=True, null=True)
    visible = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_user2mergefields'


class JkitepUser2Role(models.Model):
    userid = models.OneToOneField('JkitepUsers', models.DO_NOTHING, db_column='userid', primary_key=True)
    roleid = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'jkitep_user2role'


class JkitepUserModulePreferences(models.Model):
    userid = models.IntegerField(primary_key=True)
    tabid = models.ForeignKey(JkitepTab, models.DO_NOTHING, db_column='tabid')
    default_cvid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_user_module_preferences'
        unique_together = (('userid', 'tabid'),)


class JkitepUserView(models.Model):
    user_viewid = models.AutoField(primary_key=True)
    user_view = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_user_view'


class JkitepUserViewSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_user_view_seq'


class JkitepUsers(models.Model):
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_password = models.CharField(max_length=200, blank=True, null=True)
    user_hash = models.CharField(max_length=32, blank=True, null=True)
    cal_color = models.CharField(max_length=25, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    reports_to_id = models.CharField(max_length=36, blank=True, null=True)
    is_admin = models.CharField(max_length=3, blank=True, null=True)
    currency_id = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    date_entered = models.DateTimeField()
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    department = models.CharField(max_length=50, blank=True, null=True)
    phone_home = models.CharField(max_length=50, blank=True, null=True)
    phone_mobile = models.CharField(max_length=50, blank=True, null=True)
    phone_work = models.CharField(max_length=50, blank=True, null=True)
    phone_other = models.CharField(max_length=50, blank=True, null=True)
    phone_fax = models.CharField(max_length=50, blank=True, null=True)
    email1 = models.CharField(max_length=100, blank=True, null=True)
    email2 = models.CharField(max_length=100, blank=True, null=True)
    secondaryemail = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=25, blank=True, null=True)
    signature = models.TextField(blank=True, null=True)
    address_street = models.CharField(max_length=150, blank=True, null=True)
    address_city = models.CharField(max_length=100, blank=True, null=True)
    address_state = models.CharField(max_length=100, blank=True, null=True)
    address_country = models.CharField(max_length=25, blank=True, null=True)
    address_postalcode = models.CharField(max_length=9, blank=True, null=True)
    user_preferences = models.TextField(blank=True, null=True)
    tz = models.CharField(max_length=30, blank=True, null=True)
    holidays = models.CharField(max_length=60, blank=True, null=True)
    namedays = models.CharField(max_length=60, blank=True, null=True)
    workdays = models.CharField(max_length=30, blank=True, null=True)
    weekstart = models.IntegerField(blank=True, null=True)
    date_format = models.CharField(max_length=200, blank=True, null=True)
    hour_format = models.CharField(max_length=30, blank=True, null=True)
    start_hour = models.CharField(max_length=30, blank=True, null=True)
    end_hour = models.CharField(max_length=30, blank=True, null=True)
    is_owner = models.CharField(max_length=100, blank=True, null=True)
    activity_view = models.CharField(max_length=200, blank=True, null=True)
    lead_view = models.CharField(max_length=200, blank=True, null=True)
    imagename = models.CharField(max_length=250, blank=True, null=True)
    deleted = models.IntegerField()
    confirm_password = models.CharField(max_length=300, blank=True, null=True)
    internal_mailer = models.CharField(max_length=3)
    reminder_interval = models.CharField(max_length=100, blank=True, null=True)
    reminder_next_time = models.CharField(max_length=100, blank=True, null=True)
    crypt_type = models.CharField(max_length=20)
    accesskey = models.CharField(max_length=36, blank=True, null=True)
    theme = models.CharField(max_length=100, blank=True, null=True)
    language = models.CharField(max_length=36, blank=True, null=True)
    time_zone = models.CharField(max_length=200, blank=True, null=True)
    currency_grouping_pattern = models.CharField(max_length=100, blank=True, null=True)
    currency_decimal_separator = models.CharField(max_length=2, blank=True, null=True)
    currency_grouping_separator = models.CharField(max_length=2, blank=True, null=True)
    currency_symbol_placement = models.CharField(max_length=20, blank=True, null=True)
    phone_crm_extension = models.CharField(max_length=100, blank=True, null=True)
    sp_gravitel_id = models.CharField(max_length=255, blank=True, null=True)
    sp_megafon_id = models.CharField(max_length=255, blank=True, null=True)
    sp_zebra_login = models.CharField(max_length=255, blank=True, null=True)
    sp_uiscom_id = models.CharField(max_length=255, blank=True, null=True)
    sp_uiscom_extension = models.CharField(max_length=255, blank=True, null=True)
    sp_telphin_extension = models.CharField(max_length=255, blank=True, null=True)
    sp_zadarma_extension = models.CharField(max_length=255, blank=True, null=True)
    sp_yandex_extension = models.CharField(max_length=255, blank=True, null=True)
    sp_yandex_outgoing_number = models.CharField(max_length=255, blank=True, null=True)
    sp_domru_id = models.CharField(max_length=255, blank=True, null=True)
    sp_westcall_spb_id = models.CharField(max_length=255, blank=True, null=True)
    sp_mcn_extension = models.CharField(max_length=255, blank=True, null=True)
    sp_rostelecom_extension = models.CharField(max_length=255, blank=True, null=True)
    sp_rostelecom_extension_internal = models.CharField(max_length=255, blank=True, null=True)
    sp_rostelecom_extension_sipiru = models.CharField(max_length=255, blank=True, null=True)
    sp_sipuni_extension = models.CharField(max_length=255, blank=True, null=True)
    sp_mango_extension = models.CharField(max_length=255, blank=True, null=True)
    no_of_currency_decimals = models.CharField(max_length=2, blank=True, null=True)
    truncate_trailing_zeros = models.CharField(max_length=3, blank=True, null=True)
    dayoftheweek = models.CharField(max_length=100, blank=True, null=True)
    callduration = models.CharField(max_length=100, blank=True, null=True)
    othereventduration = models.CharField(max_length=100, blank=True, null=True)
    calendarsharedtype = models.CharField(max_length=100, blank=True, null=True)
    default_record_view = models.CharField(max_length=10, blank=True, null=True)
    leftpanelhide = models.CharField(max_length=3, blank=True, null=True)
    rowheight = models.CharField(max_length=10, blank=True, null=True)
    defaulteventstatus = models.CharField(max_length=50, blank=True, null=True)
    defaultactivitytype = models.CharField(max_length=50, blank=True, null=True)
    hidecompletedevents = models.IntegerField(blank=True, null=True)
    defaultcalendarview = models.CharField(max_length=100, blank=True, null=True)
    parent_user_id = models.CharField(max_length=100, blank=True, null=True)
    parent_user_region_id = models.CharField(max_length=100, blank=True, null=True)
    user_view = models.CharField(max_length=100, blank=True, null=True)
    position_user_employee = models.CharField(max_length=100, blank=True, null=True)
    last_updated_pass = models.DateField()
    parent_regions_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_users'


class JkitepUsers2Group(models.Model):
    groupid = models.IntegerField(primary_key=True)
    userid = models.ForeignKey(JkitepUsers, models.DO_NOTHING, db_column='userid')

    class Meta:
        managed = False
        db_table = 'jkitep_users2group'
        unique_together = (('groupid', 'userid'),)


class JkitepUsersLastImport(models.Model):
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    bean_type = models.CharField(max_length=36, blank=True, null=True)
    bean_id = models.CharField(max_length=36, blank=True, null=True)
    deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_users_last_import'


class JkitepUsersSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_users_seq'


class JkitepUsestate(models.Model):
    usestateid = models.AutoField(primary_key=True)
    usestate = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_usestate'


class JkitepUsestateSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_usestate_seq'


class JkitepVendor(models.Model):
    vendorid = models.OneToOneField(JkitepCrmentity, models.DO_NOTHING, db_column='vendorid', primary_key=True)
    vendor_no = models.CharField(max_length=100)
    vendorname = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    website = models.CharField(max_length=100, blank=True, null=True)
    glacct = models.CharField(max_length=200, blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    street = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    state = models.CharField(max_length=30, blank=True, null=True)
    pobox = models.CharField(max_length=30, blank=True, null=True)
    postalcode = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    tags = models.CharField(max_length=1, blank=True, null=True)
    full_name_director = models.CharField(max_length=100, blank=True, null=True)
    inn_ven = models.IntegerField(blank=True, null=True)
    okpo_ven = models.IntegerField(blank=True, null=True)
    bank_name = models.CharField(max_length=100, blank=True, null=True)
    checking_acc = models.CharField(max_length=100, blank=True, null=True)
    bik_ven = models.CharField(max_length=100, blank=True, null=True)
    leg_address = models.CharField(max_length=300, blank=True, null=True)
    act_address = models.CharField(max_length=300, blank=True, null=True)
    lawtype = models.CharField(max_length=100, blank=True, null=True)
    fax = models.CharField(max_length=100, blank=True, null=True)
    venderrepres = models.CharField(max_length=100, blank=True, null=True)
    represmob = models.CharField(max_length=100, blank=True, null=True)
    ustav = models.CharField(max_length=100, blank=True, null=True)
    svidet = models.CharField(max_length=100, blank=True, null=True)
    dotype = models.CharField(max_length=100, blank=True, null=True)
    phonev = models.CharField(max_length=100, blank=True, null=True)
    employees_id_user = models.CharField(max_length=100, blank=True, null=True)
    pin_con = models.CharField(max_length=100, blank=True, null=True)
    status_users_vendor = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_vendor'


class JkitepVendorcf(models.Model):
    vendorid = models.OneToOneField(JkitepVendor, models.DO_NOTHING, db_column='vendorid', primary_key=True)

    class Meta:
        managed = False
        db_table = 'jkitep_vendorcf'


class JkitepVendorcontactrel(models.Model):
    vendorid = models.OneToOneField(JkitepVendor, models.DO_NOTHING, db_column='vendorid', primary_key=True)
    contactid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_vendorcontactrel'
        unique_together = (('vendorid', 'contactid'),)


class JkitepVersion(models.Model):
    old_version = models.CharField(max_length=30, blank=True, null=True)
    current_version = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_version'


class JkitepVersionSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_version_seq'


class JkitepVisibility(models.Model):
    visibilityid = models.AutoField(primary_key=True)
    visibility = models.CharField(unique=True, max_length=200)
    sortorderid = models.IntegerField()
    presence = models.IntegerField()
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_visibility'


class JkitepVisibilitySeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_visibility_seq'


class JkitepVkStatus(models.Model):
    vk_statusid = models.AutoField(primary_key=True)
    vk_status = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_vk_status'


class JkitepVkStatusSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_vk_status_seq'


class JkitepWebformFileFields(models.Model):
    webformid = models.ForeignKey('JkitepWebforms', models.DO_NOTHING, db_column='webformid')
    fieldname = models.CharField(max_length=100)
    fieldlabel = models.CharField(max_length=100)
    required = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_webform_file_fields'


class JkitepWebforms(models.Model):
    name = models.CharField(unique=True, max_length=100)
    publicid = models.CharField(max_length=100)
    enabled = models.IntegerField()
    targetmodule = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    ownerid = models.IntegerField()
    returnurl = models.CharField(max_length=250, blank=True, null=True)
    captcha = models.IntegerField()
    roundrobin = models.IntegerField()
    roundrobin_userid = models.CharField(max_length=256, blank=True, null=True)
    roundrobin_logic = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_webforms'


class JkitepWebformsField(models.Model):
    webformid = models.ForeignKey(JkitepWebforms, models.DO_NOTHING, db_column='webformid')
    fieldname = models.ForeignKey(JkitepField, models.DO_NOTHING, db_column='fieldname')
    neutralizedfield = models.CharField(max_length=50)
    defaultvalue = models.TextField(blank=True, null=True)
    required = models.IntegerField()
    sequence = models.IntegerField(blank=True, null=True)
    hidden = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_webforms_field'


class JkitepWordtemplates(models.Model):
    templateid = models.IntegerField(primary_key=True)
    filename = models.CharField(max_length=100)
    module = models.CharField(max_length=30)
    date_entered = models.DateTimeField()
    parent_type = models.CharField(max_length=50)
    data = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    filesize = models.CharField(max_length=50)
    filetype = models.CharField(max_length=20)
    deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_wordtemplates'


class JkitepWsEntity(models.Model):
    name = models.CharField(max_length=25)
    handler_path = models.CharField(max_length=255)
    handler_class = models.CharField(max_length=64)
    ismodule = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_ws_entity'


class JkitepWsEntityFieldtype(models.Model):
    fieldtypeid = models.AutoField(primary_key=True)
    table_name = models.CharField(max_length=50)
    field_name = models.CharField(max_length=50)
    fieldtype = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'jkitep_ws_entity_fieldtype'
        unique_together = (('table_name', 'field_name'),)


class JkitepWsEntityFieldtypeSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_ws_entity_fieldtype_seq'


class JkitepWsEntityName(models.Model):
    entity_id = models.IntegerField(primary_key=True)
    name_fields = models.CharField(max_length=50)
    index_field = models.CharField(max_length=50)
    table_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'jkitep_ws_entity_name'


class JkitepWsEntityReferencetype(models.Model):
    fieldtypeid = models.OneToOneField(JkitepWsEntityFieldtype, models.DO_NOTHING, db_column='fieldtypeid', primary_key=True)
    type = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'jkitep_ws_entity_referencetype'
        unique_together = (('fieldtypeid', 'type'),)


class JkitepWsEntitySeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_ws_entity_seq'


class JkitepWsEntityTables(models.Model):
    webservice_entity = models.OneToOneField(JkitepWsEntity, models.DO_NOTHING, primary_key=True)
    table_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'jkitep_ws_entity_tables'
        unique_together = (('webservice_entity', 'table_name'),)


class JkitepWsFieldinfo(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    property_name = models.CharField(max_length=32, blank=True, null=True)
    property_value = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_ws_fieldinfo'


class JkitepWsFieldtype(models.Model):
    fieldtypeid = models.AutoField(primary_key=True)
    uitype = models.CharField(unique=True, max_length=30)
    fieldtype = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'jkitep_ws_fieldtype'


class JkitepWsOperation(models.Model):
    operationid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    handler_path = models.CharField(max_length=255)
    handler_method = models.CharField(max_length=64)
    type = models.CharField(max_length=8)
    prelogin = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_ws_operation'


class JkitepWsOperationParameters(models.Model):
    operationid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    type = models.CharField(max_length=64)
    sequence = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_ws_operation_parameters'
        unique_together = (('operationid', 'name'),)


class JkitepWsOperationSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_ws_operation_seq'


class JkitepWsReferencetype(models.Model):
    fieldtypeid = models.OneToOneField(JkitepWsFieldtype, models.DO_NOTHING, db_column='fieldtypeid', primary_key=True)
    type = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'jkitep_ws_referencetype'
        unique_together = (('fieldtypeid', 'type'),)


class JkitepWsUserauthtoken(models.Model):
    userid = models.IntegerField(primary_key=True)
    token = models.CharField(max_length=36)
    expiretime = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_ws_userauthtoken'
        unique_together = (('userid', 'expiretime'),)


class JkitepWsapp(models.Model):
    appid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    appkey = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_wsapp'


class JkitepWsappHandlerdetails(models.Model):
    type = models.CharField(max_length=200)
    handlerclass = models.CharField(max_length=100, blank=True, null=True)
    handlerpath = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_wsapp_handlerdetails'


class JkitepWsappLogsBasic(models.Model):
    extensiontabid = models.IntegerField(blank=True, null=True)
    module = models.CharField(max_length=50)
    sync_datetime = models.DateTimeField()
    app_create_count = models.IntegerField(blank=True, null=True)
    app_update_count = models.IntegerField(blank=True, null=True)
    app_delete_count = models.IntegerField(blank=True, null=True)
    app_skip_count = models.IntegerField(blank=True, null=True)
    vt_create_count = models.IntegerField(blank=True, null=True)
    vt_update_count = models.IntegerField(blank=True, null=True)
    vt_delete_count = models.IntegerField(blank=True, null=True)
    vt_skip_count = models.IntegerField(blank=True, null=True)
    userid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_wsapp_logs_basic'


class JkitepWsappLogsDetails(models.Model):
    id = models.ForeignKey(JkitepWsappLogsBasic, models.DO_NOTHING, db_column='id')
    app_create_ids = models.TextField(blank=True, null=True)
    app_update_ids = models.TextField(blank=True, null=True)
    app_delete_ids = models.TextField(blank=True, null=True)
    app_skip_info = models.TextField(blank=True, null=True)
    vt_create_ids = models.TextField(blank=True, null=True)
    vt_update_ids = models.TextField(blank=True, null=True)
    vt_delete_ids = models.TextField(blank=True, null=True)
    vt_skip_info = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_wsapp_logs_details'


class JkitepWsappQueuerecords(models.Model):
    syncserverid = models.IntegerField(blank=True, null=True)
    details = models.CharField(max_length=300, blank=True, null=True)
    flag = models.CharField(max_length=100, blank=True, null=True)
    appid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_wsapp_queuerecords'


class JkitepWsappRecordmapping(models.Model):
    serverid = models.CharField(max_length=10, blank=True, null=True)
    clientid = models.CharField(max_length=255, blank=True, null=True)
    clientmodifiedtime = models.DateTimeField(blank=True, null=True)
    appid = models.IntegerField(blank=True, null=True)
    servermodifiedtime = models.DateTimeField(blank=True, null=True)
    serverappid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_wsapp_recordmapping'


class JkitepWsappSyncState(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    stateencodedvalues = models.CharField(max_length=300)
    userid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_wsapp_sync_state'


class JkitepYearPublishPart(models.Model):
    year_publish_partid = models.AutoField(primary_key=True)
    year_publish_part = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_year_publish_part'


class JkitepYearPublishPartSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_year_publish_part_seq'


class JkitepYyyy(models.Model):
    yyyyid = models.AutoField(primary_key=True)
    yyyy = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    sortorderid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_yyyy'


class JkitepYyyySeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jkitep_yyyy_seq'


class Pins(models.Model):
    full_name = models.CharField(max_length=255, blank=True, null=True)
    birth_day = models.DateField(blank=True, null=True)
    inn = models.CharField(db_column='INN', max_length=14)  # Field name made lowercase.
    inn_mark = models.IntegerField(db_column='INN_mark')  # Field name made lowercase.
    valid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pins'


class PinsEmployee(models.Model):
    full_name = models.CharField(max_length=255, blank=True, null=True)
    birth_day = models.DateField(blank=True, null=True)
    inn = models.CharField(db_column='INN', max_length=14)  # Field name made lowercase.
    inn_mark = models.IntegerField(db_column='INN_mark')  # Field name made lowercase.
    valid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pins_employee'


class ServiceHistory(models.Model):
    service_id = models.IntegerField(blank=True, null=True)
    so_id = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    quote_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'service_history'


class SpCmlSiteSettings(models.Model):
    setting_type = models.CharField(max_length=255, blank=True, null=True)
    key = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sp_cml_site_settings'


class SpCommercetranzaction(models.Model):
    date = models.DateTimeField()
    type = models.CharField(max_length=32)
    status = models.IntegerField(blank=True, null=True)
    direction = models.CharField(max_length=16, blank=True, null=True)
    error = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sp_commercetranzaction'


class SpCustomReports(models.Model):
    reporttype = models.CharField(primary_key=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'sp_custom_reports'


class SpPayments(models.Model):
    payid = models.OneToOneField(JkitepCrmentity, models.DO_NOTHING, db_column='payid', primary_key=True)
    pay_no = models.CharField(max_length=100)
    pay_date = models.DateField()
    pay_details = models.CharField(max_length=255, blank=True, null=True)
    pay_type = models.CharField(max_length=100, blank=True, null=True)
    payer = models.IntegerField()
    doc_no = models.IntegerField(blank=True, null=True)
    related_to = models.IntegerField()
    type_payment = models.CharField(max_length=100, blank=True, null=True)
    amount = models.DecimalField(max_digits=25, decimal_places=8, blank=True, null=True)
    spstatus = models.CharField(max_length=200, blank=True, null=True)
    debit = models.CharField(max_length=100, blank=True, null=True)
    coracc_subacc = models.CharField(max_length=100, blank=True, null=True)
    analytics_code = models.CharField(max_length=100, blank=True, null=True)
    target_code = models.CharField(max_length=100, blank=True, null=True)
    spcompany = models.CharField(max_length=200, blank=True, null=True)
    tags = models.CharField(max_length=1, blank=True, null=True)
    academic_year_pay = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sp_payments'


class SpPaymentscf(models.Model):
    payid = models.OneToOneField(SpPayments, models.DO_NOTHING, db_column='payid', primary_key=True)

    class Meta:
        managed = False
        db_table = 'sp_paymentscf'


class SpTemplates(models.Model):
    templateid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    module = models.CharField(max_length=64, blank=True, null=True)
    template = models.TextField(blank=True, null=True)
    header_size = models.IntegerField(blank=True, null=True)
    footer_size = models.IntegerField(blank=True, null=True)
    page_orientation = models.CharField(max_length=1, blank=True, null=True)
    spcompany = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'sp_templates'


class SpTemplatesSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sp_templates_seq'


class SpTipsDependentFields(models.Model):
    field_id = models.AutoField(primary_key=True)
    jkitep_fieldname = models.CharField(max_length=127, blank=True, null=True)
    provider_fieldname = models.CharField(max_length=127, blank=True, null=True)
    rule = models.ForeignKey('SpTipsModuleRules', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sp_tips_dependent_fields'


class SpTipsDependentFieldsSeq(models.Model):
    id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sp_tips_dependent_fields_seq'


class SpTipsModuleRules(models.Model):
    rule_id = models.AutoField(primary_key=True)
    module = models.CharField(max_length=127, blank=True, null=True)
    field = models.CharField(max_length=127, blank=True, null=True)
    provider = models.ForeignKey('SpTipsProviders', models.DO_NOTHING, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sp_tips_module_rules'


class SpTipsModuleRulesSeq(models.Model):
    id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sp_tips_module_rules_seq'


class SpTipsProviders(models.Model):
    provider_id = models.AutoField(primary_key=True)
    provider_name = models.CharField(max_length=255, blank=True, null=True)
    settings = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sp_tips_providers'


class SpUnits(models.Model):
    unitid = models.OneToOneField(JkitepCrmentity, models.DO_NOTHING, db_column='unitid', primary_key=True)
    unit_no = models.CharField(max_length=100)
    unitname = models.CharField(max_length=200)
    usageunit = models.CharField(max_length=200, blank=True, null=True)
    unit_code = models.CharField(max_length=200, blank=True, null=True)
    tags = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sp_units'


class SpUnitscf(models.Model):
    unitid = models.OneToOneField(SpUnits, models.DO_NOTHING, db_column='unitid', primary_key=True)

    class Meta:
        managed = False
        db_table = 'sp_unitscf'
