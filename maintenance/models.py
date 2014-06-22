# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _, pgettext_lazy


class Maintenance(models.Model):
    """
    Maintenance scheduling
    """
    enabled = models.BooleanField(default=True, null=False, verbose_name=pgettext_lazy('maintenance', u"Enabled"))
    start_time = models.DateTimeField(blank=False, null=False, verbose_name=_(u"Start time"))
    end_time = models.DateTimeField(blank=False, null=False, verbose_name=_(u"End time"))
    description = models.TextField(verbose_name=_(u"Description"))
    
    def __unicode__(self):
        return self.start_time.isoformat()
        
    class Meta:
        verbose_name = _(u"maintenance schedule")
        verbose_name_plural = _(u"maintenance schedules")


class MaintenanceFilter(models.Model):
    """
    Filter maintenance schedule py path
    """
    maintenance = models.ForeignKey('maintenance.Maintenance')
    path = models.CharField(max_length=128, blank=False, verbose_name=pgettext_lazy('url', u"Path"))

    class Meta:
        verbose_name = _(u"maintenance filter")
        verbose_name_plural = _(u"maintenance filtering")
