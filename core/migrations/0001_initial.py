# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Morsel'
        db.create_table(u'core_morsel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'core', ['Morsel'])

        # Adding model 'ReminderSchedule'
        db.create_table(u'core_reminderschedule', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'core', ['ReminderSchedule'])

        # Adding model 'ReminderTask'
        db.create_table(u'core_remindertask', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('delay', self.gf('django.db.models.fields.IntegerField')()),
            ('repeating', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('schedule', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.ReminderSchedule'])),
        ))
        db.send_create_signal(u'core', ['ReminderTask'])

        # Adding model 'MorselEventType'
        db.create_table(u'core_morseleventtype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'core', ['MorselEventType'])

        # Adding model 'MorselEvent'
        db.create_table(u'core_morselevent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('morsel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Morsel'])),
            ('event_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.MorselEventType'])),
            ('event_datetime', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['MorselEvent'])


    def backwards(self, orm):
        # Deleting model 'Morsel'
        db.delete_table(u'core_morsel')

        # Deleting model 'ReminderSchedule'
        db.delete_table(u'core_reminderschedule')

        # Deleting model 'ReminderTask'
        db.delete_table(u'core_remindertask')

        # Deleting model 'MorselEventType'
        db.delete_table(u'core_morseleventtype')

        # Deleting model 'MorselEvent'
        db.delete_table(u'core_morselevent')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.morsel': {
            'Meta': {'ordering': "['-created']", 'object_name': 'Morsel'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'core.morselevent': {
            'Meta': {'object_name': 'MorselEvent'},
            'event_datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'event_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.MorselEventType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'morsel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Morsel']"})
        },
        u'core.morseleventtype': {
            'Meta': {'object_name': 'MorselEventType'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'core.reminderschedule': {
            'Meta': {'object_name': 'ReminderSchedule'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'core.remindertask': {
            'Meta': {'ordering': "['delay']", 'object_name': 'ReminderTask'},
            'delay': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'repeating': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'schedule': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.ReminderSchedule']"})
        }
    }

    complete_apps = ['core']