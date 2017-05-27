# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'CommonUser.id'
        db.delete_column('registration_commonuser', 'id')


        # Changing field 'CommonUser.student_number'
        db.alter_column('registration_commonuser', 'student_number', self.gf('django.db.models.fields.IntegerField')(primary_key=True))
        # Adding unique constraint on 'CommonUser', fields ['student_number']
        db.create_unique('registration_commonuser', ['student_number'])

        # Deleting field 'Administrator.id'
        db.delete_column('registration_administrator', 'id')


        # Changing field 'Administrator.student_number'
        db.alter_column('registration_administrator', 'student_number', self.gf('django.db.models.fields.IntegerField')(primary_key=True))
        # Adding unique constraint on 'Administrator', fields ['student_number']
        db.create_unique('registration_administrator', ['student_number'])


    def backwards(self, orm):
        # Removing unique constraint on 'Administrator', fields ['student_number']
        db.delete_unique('registration_administrator', ['student_number'])

        # Removing unique constraint on 'CommonUser', fields ['student_number']
        db.delete_unique('registration_commonuser', ['student_number'])

        # Adding field 'CommonUser.id'
        db.add_column('registration_commonuser', 'id',
                      self.gf('django.db.models.fields.AutoField')(default=1, primary_key=True),
                      keep_default=False)


        # Changing field 'CommonUser.student_number'
        db.alter_column('registration_commonuser', 'student_number', self.gf('django.db.models.fields.IntegerField')())
        # Adding field 'Administrator.id'
        db.add_column('registration_administrator', 'id',
                      self.gf('django.db.models.fields.AutoField')(default=1, primary_key=True),
                      keep_default=False)


        # Changing field 'Administrator.student_number'
        db.alter_column('registration_administrator', 'student_number', self.gf('django.db.models.fields.IntegerField')())

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'registration.administrator': {
            'Meta': {'object_name': 'Administrator'},
            'student_number': ('django.db.models.fields.IntegerField', [], {'default': '0', 'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'registration.commonuser': {
            'Meta': {'object_name': 'CommonUser'},
            'student_number': ('django.db.models.fields.IntegerField', [], {'default': '0', 'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['registration']