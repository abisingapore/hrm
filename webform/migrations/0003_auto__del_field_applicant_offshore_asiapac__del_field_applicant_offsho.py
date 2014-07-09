# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Applicant.offshore_asiapac'
        db.delete_column(u'webform_applicant', 'offshore_asiapac')

        # Deleting field 'Applicant.offshore_europeusa'
        db.delete_column(u'webform_applicant', 'offshore_europeusa')

        # Deleting field 'Applicant.offshore_singapore'
        db.delete_column(u'webform_applicant', 'offshore_singapore')

        # Deleting field 'Applicant.onshore_europeusa'
        db.delete_column(u'webform_applicant', 'onshore_europeusa')

        # Deleting field 'Applicant.offshore_mideast'
        db.delete_column(u'webform_applicant', 'offshore_mideast')

        # Deleting field 'Applicant.onshore_mideast'
        db.delete_column(u'webform_applicant', 'onshore_mideast')

        # Deleting field 'Applicant.onshore_singapore'
        db.delete_column(u'webform_applicant', 'onshore_singapore')

        # Deleting field 'Applicant.onshore_asiapac'
        db.delete_column(u'webform_applicant', 'onshore_asiapac')

        # Deleting field 'Applicant.offshore_africa'
        db.delete_column(u'webform_applicant', 'offshore_africa')

        # Deleting field 'Applicant.onshore_africa'
        db.delete_column(u'webform_applicant', 'onshore_africa')

        # Adding field 'Applicant.add_nationality'
        db.add_column(u'webform_applicant', 'add_nationality',
                      self.gf('django_countries.fields.CountryField')(max_length=2, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Applicant.add_nat_status'
        db.add_column(u'webform_applicant', 'add_nat_status',
                      self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True),
                      keep_default=False)

        # Adding field 'EmploymentHistory.company_name'
        db.add_column(u'webform_employmenthistory', 'company_name',
                      self.gf('django.db.models.fields.CharField')(default='Company', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Applicant.offshore_asiapac'
        db.add_column(u'webform_applicant', 'offshore_asiapac',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Applicant.offshore_europeusa'
        db.add_column(u'webform_applicant', 'offshore_europeusa',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Applicant.offshore_singapore'
        db.add_column(u'webform_applicant', 'offshore_singapore',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Applicant.onshore_europeusa'
        db.add_column(u'webform_applicant', 'onshore_europeusa',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Applicant.offshore_mideast'
        db.add_column(u'webform_applicant', 'offshore_mideast',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Applicant.onshore_mideast'
        db.add_column(u'webform_applicant', 'onshore_mideast',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Applicant.onshore_singapore'
        db.add_column(u'webform_applicant', 'onshore_singapore',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Applicant.onshore_asiapac'
        db.add_column(u'webform_applicant', 'onshore_asiapac',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Applicant.offshore_africa'
        db.add_column(u'webform_applicant', 'offshore_africa',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Applicant.onshore_africa'
        db.add_column(u'webform_applicant', 'onshore_africa',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Applicant.add_nationality'
        db.delete_column(u'webform_applicant', 'add_nationality')

        # Deleting field 'Applicant.add_nat_status'
        db.delete_column(u'webform_applicant', 'add_nat_status')

        # Deleting field 'EmploymentHistory.company_name'
        db.delete_column(u'webform_employmenthistory', 'company_name')


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