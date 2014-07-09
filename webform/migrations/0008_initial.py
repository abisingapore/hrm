# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Specialization'
        db.create_table(u'webform_specialization', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'webform', ['Specialization'])

        # Adding model 'CertNames'
        db.create_table(u'webform_certnames', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'webform', ['CertNames'])

        # Adding model 'Applicant'
        db.create_table(u'webform_applicant', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('known_as', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('signup_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('nationality', self.gf('django_countries.fields.CountryField')(max_length=2, null=True, blank=True)),
            ('add_nationality', self.gf('django_countries.fields.CountryField')(max_length=2, null=True, blank=True)),
            ('add_nat_status', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True)),
            ('date_of_birth', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('confirm_email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('contact_home', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('contact_mobile', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('marital_status', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('address_line_1', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('address_line_2', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('postal_code', self.gf('django.db.models.fields.IntegerField')(max_length=100, null=True, blank=True)),
            ('country', self.gf('django_countries.fields.CountryField')(max_length=2, null=True, blank=True)),
            ('abi_summary', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('language_proficiency', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('computer_literacy', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('current_salary', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('notice_period', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('current_pos', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('whereabouts', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('offshore', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True)),
            ('preferred_places', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('describe_self', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('cv', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('blacklist', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('blacklist_reason', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('declaration', self.gf('django.db.models.fields.BooleanField')()),
            ('tos', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'webform', ['Applicant'])

        # Adding M2M table for field spec_summary on 'Applicant'
        m2m_table_name = db.shorten_name(u'webform_applicant_spec_summary')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('applicant', models.ForeignKey(orm[u'webform.applicant'], null=False)),
            ('specialization', models.ForeignKey(orm[u'webform.specialization'], null=False))
        ))
        db.create_unique(m2m_table_name, ['applicant_id', 'specialization_id'])

        # Adding model 'Certification'
        db.create_table(u'webform_certification', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['webform.CertNames'], null=True, blank=True)),
            ('registration_number', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('expiry_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('valid', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('applicant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['webform.Applicant'], null=True, blank=True)),
        ))
        db.send_create_signal(u'webform', ['Certification'])

        # Adding model 'GeneratedCV'
        db.create_table(u'webform_generatedcv', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('applicant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['webform.Applicant'], null=True, blank=True)),
            ('latest', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'webform', ['GeneratedCV'])

        # Adding model 'Discipline'
        db.create_table(u'webform_discipline', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'webform', ['Discipline'])

        # Adding model 'Professional'
        db.create_table(u'webform_professional', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('qualification', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('discipline', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['webform.Discipline'], null=True, blank=True)),
            ('university', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('year_of_completion', self.gf('django.db.models.fields.IntegerField')(max_length=10, null=True, blank=True)),
            ('applicant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['webform.Applicant'])),
        ))
        db.send_create_signal(u'webform', ['Professional'])

        # Adding model 'EmploymentHistory'
        db.create_table(u'webform_employmenthistory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
            ('company_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('project_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('position_held', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('responsibilities', self.gf('django.db.models.fields.TextField')()),
            ('applicant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['webform.Applicant'])),
        ))
        db.send_create_signal(u'webform', ['EmploymentHistory'])

        # Adding model 'Contract'
        db.create_table(u'webform_contract', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['webform.Applicant'])),
            ('project_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'webform', ['Contract'])


    def backwards(self, orm):
        # Deleting model 'Specialization'
        db.delete_table(u'webform_specialization')

        # Deleting model 'CertNames'
        db.delete_table(u'webform_certnames')

        # Deleting model 'Applicant'
        db.delete_table(u'webform_applicant')

        # Removing M2M table for field spec_summary on 'Applicant'
        db.delete_table(db.shorten_name(u'webform_applicant_spec_summary'))

        # Deleting model 'Certification'
        db.delete_table(u'webform_certification')

        # Deleting model 'GeneratedCV'
        db.delete_table(u'webform_generatedcv')

        # Deleting model 'Discipline'
        db.delete_table(u'webform_discipline')

        # Deleting model 'Professional'
        db.delete_table(u'webform_professional')

        # Deleting model 'EmploymentHistory'
        db.delete_table(u'webform_employmenthistory')

        # Deleting model 'Contract'
        db.delete_table(u'webform_contract')


    models = {
        u'webform.applicant': {
            'Meta': {'object_name': 'Applicant'},
            'abi_summary': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'add_nat_status': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'add_nationality': ('django_countries.fields.CountryField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'address_line_1': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'address_line_2': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'blacklist': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'blacklist_reason': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'computer_literacy': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'confirm_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'contact_home': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'contact_mobile': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'country': ('django_countries.fields.CountryField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'current_pos': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'current_salary': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'cv': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'declaration': ('django.db.models.fields.BooleanField', [], {}),
            'describe_self': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'known_as': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'language_proficiency': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'marital_status': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'nationality': ('django_countries.fields.CountryField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'notice_period': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'offshore': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'postal_code': ('django.db.models.fields.IntegerField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'preferred_places': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'signup_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'spec_summary': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['webform.Specialization']", 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'tos': ('django.db.models.fields.BooleanField', [], {}),
            'whereabouts': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'webform.certification': {
            'Meta': {'object_name': 'Certification'},
            'applicant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['webform.Applicant']", 'null': 'True', 'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['webform.CertNames']", 'null': 'True', 'blank': 'True'}),
            'registration_number': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'valid': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'webform.certnames': {
            'Meta': {'ordering': "['name']", 'object_name': 'CertNames'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'webform.contract': {
            'Meta': {'object_name': 'Contract'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['webform.Applicant']"}),
            'project_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'webform.discipline': {
            'Meta': {'object_name': 'Discipline'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'webform.employmenthistory': {
            'Meta': {'object_name': 'EmploymentHistory'},
            'applicant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['webform.Applicant']"}),
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position_held': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'project_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'responsibilities': ('django.db.models.fields.TextField', [], {}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        u'webform.generatedcv': {
            'Meta': {'object_name': 'GeneratedCV'},
            'applicant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['webform.Applicant']", 'null': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latest': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'webform.professional': {
            'Meta': {'object_name': 'Professional'},
            'applicant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['webform.Applicant']"}),
            'discipline': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['webform.Discipline']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'qualification': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'university': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'year_of_completion': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        },
        u'webform.specialization': {
            'Meta': {'ordering': "['name']", 'object_name': 'Specialization'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['webform']