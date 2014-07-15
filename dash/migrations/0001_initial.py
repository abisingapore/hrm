# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Action'
        db.create_table(u'dash_action', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('action', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'dash', ['Action'])

        # Adding model 'RequestsAndProposals'
        db.create_table(u'dash_requestsandproposals', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('requested_for', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('request', self.gf('django.db.models.fields.TextField')()),
            ('duration', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('poc', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('interview_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'dash', ['RequestsAndProposals'])

        # Adding M2M table for field to_propose on 'RequestsAndProposals'
        m2m_table_name = db.shorten_name(u'dash_requestsandproposals_to_propose')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('requestsandproposals', models.ForeignKey(orm[u'dash.requestsandproposals'], null=False)),
            ('applicant', models.ForeignKey(orm[u'webform.applicant'], null=False))
        ))
        db.create_unique(m2m_table_name, ['requestsandproposals_id', 'applicant_id'])

        # Adding M2M table for field action_required on 'RequestsAndProposals'
        m2m_table_name = db.shorten_name(u'dash_requestsandproposals_action_required')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('requestsandproposals', models.ForeignKey(orm[u'dash.requestsandproposals'], null=False)),
            ('action', models.ForeignKey(orm[u'dash.action'], null=False))
        ))
        db.create_unique(m2m_table_name, ['requestsandproposals_id', 'action_id'])


    def backwards(self, orm):
        # Deleting model 'Action'
        db.delete_table(u'dash_action')

        # Deleting model 'RequestsAndProposals'
        db.delete_table(u'dash_requestsandproposals')

        # Removing M2M table for field to_propose on 'RequestsAndProposals'
        db.delete_table(db.shorten_name(u'dash_requestsandproposals_to_propose'))

        # Removing M2M table for field action_required on 'RequestsAndProposals'
        db.delete_table(db.shorten_name(u'dash_requestsandproposals_action_required'))


    models = {
        u'dash.action': {
            'Meta': {'object_name': 'Action'},
            'action': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'dash.requestsandproposals': {
            'Meta': {'ordering': "['-date_created']", 'object_name': 'RequestsAndProposals'},
            'action_required': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['dash.Action']", 'null': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'duration': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interview_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'poc': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'request': ('django.db.models.fields.TextField', [], {}),
            'requested_for': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'to_propose': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['webform.Applicant']", 'null': 'True', 'blank': 'True'})
        },
        u'webform.applicant': {
            'Meta': {'ordering': "['first_name']", 'object_name': 'Applicant'},
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
            'contact_home': ('phonenumber_field.modelfields.PhoneNumberField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'contact_mobile': ('phonenumber_field.modelfields.PhoneNumberField', [], {'max_length': '128'}),
            'country': ('django_countries.fields.CountryField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'current_pos': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'current_salary': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'cv': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'declaration': ('django.db.models.fields.BooleanField', [], {}),
            'describe_self': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
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
            'proposed_specialization': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'signup_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'spec_summary': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['webform.Specialization']", 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'tos': ('django.db.models.fields.BooleanField', [], {}),
            'whereabouts': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'webform.specialization': {
            'Meta': {'ordering': "['name']", 'object_name': 'Specialization'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['dash']