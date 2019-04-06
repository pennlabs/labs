import datetime

import pytz
from django.contrib.auth import get_user_model
from django.test import TestCase

from accounts.models import Student
from accounts.serializers import StudentSerializer


class StudentSerializerTestCase(TestCase):
    def setUp(self):
        self.date = pytz.timezone('America/New_York').localize(datetime.datetime(2019, 1, 1))
        self.user = get_user_model().objects.create_user(
            username='student',
            password='secret',
            uuid='00000000000000000000000000000000'
        )
        Student.objects.create(user=self.user)
        self.user.student.name = 'Student'
        self.user.student.major = 'Major'
        self.user.student.school = 'School'
        self.serializer = StudentSerializer(self.user.student)

    def test_str(self):
        sample_response = {'major': 'Major', 'school': 'School', 'uuid': '00000000000000000000000000000000',
                           'affiliation': [], 'product_permissions': []}
        self.assertEqual(self.serializer.data, sample_response)
