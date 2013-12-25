# -*- coding: utf-8 -*-
import dbsettings
from dbsettings import values


class Exchange1c(dbsettings.Group):
    export_index = values.IntegerValue(u'1c �������: ����� ���������� ���������', default=0)
    exported = values.DateTimeValue(u'1� �������: ���� ���������� ��������',
                                    required=False, default='')
    exported_new = values.DateTimeValue(u'1� �������: ���� ���������� ��������. ����� ��������',
                                        required=False, default='')

    import_index = values.IntegerValue(u'1c ������: ����� ���������� ���������', default=0)
    imported = values.DateTimeValue(u'1� ������: ���� ���������� �������',
                                    required=False, default='')

exchange_1c = Exchange1c(u'����� � 1�')

