# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field mengajar on 'Guru'
        m2m_table_name = db.shorten_name(u'akademik_guru_mengajar')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('guru', models.ForeignKey(orm[u'akademik.guru'], null=False)),
            ('matapelajaran', models.ForeignKey(orm[u'akademik.matapelajaran'], null=False))
        ))
        db.create_unique(m2m_table_name, ['guru_id', 'matapelajaran_id'])


    def backwards(self, orm):
        # Removing M2M table for field mengajar on 'Guru'
        db.delete_table(db.shorten_name(u'akademik_guru_mengajar'))


    models = {
        u'akademik.guru': {
            'Meta': {'object_name': 'Guru'},
            'agama': ('django.db.models.fields.SmallIntegerField', [], {}),
            'aktif': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'alamat': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jenis_kelamin': ('django.db.models.fields.SmallIntegerField', [], {}),
            'keterangan': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'mengajar': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['akademik.MataPelajaran']", 'symmetrical': 'False'}),
            'nama': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'nik': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'nomor_telepon': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'tanggal_lahir': ('django.db.models.fields.DateField', [], {})
        },
        u'akademik.jadwal': {
            'Meta': {'object_name': 'Jadwal'},
            'hari': ('django.db.models.fields.SmallIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mulai': ('django.db.models.fields.TimeField', [], {}),
            'pengajaran': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['akademik.Pengajaran']"}),
            'selesai': ('django.db.models.fields.TimeField', [], {})
        },
        u'akademik.jenisagenda': {
            'Meta': {'object_name': 'JenisAgenda'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nama': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'akademik.jurusan': {
            'Meta': {'object_name': 'Jurusan'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nama': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'akademik.kalenderakademik': {
            'Meta': {'ordering': "['-mulai', '-akhir']", 'object_name': 'KalenderAkademik'},
            'akhir': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jenis_agenda': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['akademik.JenisAgenda']"}),
            'keterangan': ('django.db.models.fields.TextField', [], {}),
            'mulai': ('django.db.models.fields.DateTimeField', [], {}),
            'nama': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'akademik.kelas': {
            'Meta': {'object_name': 'Kelas'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jurusan': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['akademik.Jurusan']"}),
            'nama': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'wali': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['akademik.Guru']"})
        },
        u'akademik.matapelajaran': {
            'Meta': {'object_name': 'MataPelajaran'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jurusan': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['akademik.Jurusan']", 'symmetrical': 'False'}),
            'nama': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'akademik.pengajaran': {
            'Meta': {'object_name': 'Pengajaran'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kelas': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['akademik.Kelas']"}),
            'mata_pelajaran': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['akademik.MataPelajaran']"}),
            'pengajar': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['akademik.Guru']"})
        },
        u'akademik.siswa': {
            'Meta': {'object_name': 'Siswa'},
            'agama': ('django.db.models.fields.SmallIntegerField', [], {}),
            'aktif': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'alamat': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jenis_kelamin': ('django.db.models.fields.SmallIntegerField', [], {}),
            'kelas': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['akademik.Kelas']"}),
            'keterangan': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'nama': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'nis': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'nomor_telepon': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'tanggal_lahir': ('django.db.models.fields.DateField', [], {})
        }
    }

    complete_apps = ['akademik']