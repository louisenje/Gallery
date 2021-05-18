from django.test import TestCase
from .models import image,location,category
import datetime as dt
# Create your tests here.

class imageTestClass(TestCase):
    def setUp(self):
        self.location=location(location_name='nairobi')
        self.location.save_location()
        self.category=category(id=1,category_name='Beauty')
        self.category.save_category()
        self.image=image(id=1,image='articles/smiley-4832482_1920.png',image_name='smiley-4832482_1920.png',image_description="Good picture",
                        pub_date='2020-05-19 12:20:58.843802+03',location=self.location,category_id=self.category)
 
    def tearDown(self):
        location.objects.all().delete()
        category.objects.all().delete()
        image.objects.all().delete()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.image,image))