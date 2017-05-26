# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'BaoXiaoTable.have_payed'
        db.add_column('statistic_baoxiaotable', 'have_payed',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'BaoXiaoTable.have_payed'
        db.delete_column('statistic_baoxiaotable', 'have_payed')


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
        'statistic.baoxiaotable': {
            'Meta': {'object_name': 'BaoXiaoTable'},
            'base_management': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'base_management_set'", 'to': "orm['statistic.DetailMoney']"}),
            'book': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'book_set'", 'to': "orm['statistic.DetailMoney']"}),
            'conference': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'conference_set'", 'to': "orm['statistic.DetailMoney']"}),
            'cooperation': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cooperation_set'", 'to': "orm['statistic.DetailMoney']"}),
            'date': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'handling_charge': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'handling_set'", 'to': "orm['statistic.DetailMoney']"}),
            'have_payed': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'hotel': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'hotel_set'", 'to': "orm['statistic.DetailMoney']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internet': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'internet_set'", 'to': "orm['statistic.DetailMoney']"}),
            'maintenance': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'maintenance_set'", 'to': "orm['statistic.DetailMoney']"}),
            'material': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'material_set'", 'to': "orm['statistic.DetailMoney']"}),
            'office_supplies': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'office_supplies_set'", 'to': "orm['statistic.DetailMoney']"}),
            'other': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'other_set'", 'to': "orm['statistic.DetailMoney']"}),
            'phone': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'phone_set'", 'to': "orm['statistic.DetailMoney']"}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'post_set'", 'to': "orm['statistic.DetailMoney']"}),
            'printing': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'printing_set'", 'to': "orm['statistic.DetailMoney']"}),
            'rent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rent_set'", 'to': "orm['statistic.DetailMoney']"}),
            'school_management': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'school_management_set'", 'to': "orm['statistic.DetailMoney']"}),
            'software': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'software_set'", 'to': "orm['statistic.DetailMoney']"}),
            'specific_facility': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'specific_facility_set'", 'to': "orm['statistic.DetailMoney']"}),
            'thirdpart': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'thirdpart_set'", 'to': "orm['statistic.DetailMoney']"}),
            'total_bills': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'total_money': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'traffic': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'traffic_set'", 'to': "orm['statistic.DetailMoney']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'water_electric': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'water_electric_set'", 'to': "orm['statistic.DetailMoney']"})
        },
        'statistic.detailmoney': {
            'Meta': {'object_name': 'DetailMoney'},
            'bill_amount': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keyword': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'money': ('django.db.models.fields.FloatField', [], {'default': '0'})
        }
    }

    complete_apps = ['statistic']