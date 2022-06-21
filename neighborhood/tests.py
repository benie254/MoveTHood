from django.test import TestCase
from neighborhood.models import UserHood,MyUser,UserProfile,Location,UserPost,Business,PoliceDept,HealthDept


# Create your tests here.
class UserHoodTestClass(TestCase):
	def setUp(self):
		# create new user & save
		self.benie = MyUser(email='benie@g.com',username='benie',first_name='Benson',last_name='Langat')
		self.benie.save()

		self.new_hood = UserHood(name='mbagathi',user=self.benie)
		self.new_hood.save()

	# test instance
	def test_instance(self):
		self.assertTrue(isinstance(self.new_hood,UserHood))

	def tearDown(self):
		UserHood.objects.filter(name=self.id).delete()

	def test_update_hood(self):
		self.updated_hood = UserHood.objects.filter(name='Nalumbi').update(name='kericho')

	def test_get_by_id(self):
		get_by_id = UserHood.objects.filter(name=self)
		return get_by_id


class UserProfileTestClass(TestCase):
	def setUp(self):
		# create new user & save
		self.benie = MyUser(email='benie@g.com', username='benie', first_name='Benson', last_name='Langat')
		self.benie.save()

		self.new_profile = UserProfile(bio='Aloha', user=self.benie)
		self.new_profile.save()

	# test instance
	def test_instance(self):
		self.assertTrue(isinstance(self.new_profile, UserProfile))

	def tearDown(self):
		UserProfile.objects.filter(bio=self.id).delete()

	def test_update_occupant(self):
		self.updated_occupant = UserProfile.objects.filter(bio='Aloha').update(bio='ah, yes!')


class LocationTestClass(TestCase):
	def setUp(self):
		# create new user & save
		self.benie = MyUser(email='benie@g.com', username='benie', first_name='Benson', last_name='Langat')
		self.benie.save()

		self.new_location = Location(address='Nairobi', user=self.benie)
		self.new_location.save()

	# test instance
	def test_instance(self):
		self.assertTrue(isinstance(self.new_location, Location))

	def tearDown(self):
		Location.objects.filter(address=self.id).delete()


class UserPostTestClass(TestCase):
	def setUp(self):
		# create new user & save
		self.benie = MyUser(email='benie@g.com', username='benie', first_name='Benson', last_name='Langat')
		self.benie.save()

		self.new_post = UserPost(title='The post of the year',description='NObody could believe ANybody', author=self.benie)
		self.new_post.save()

	# test instance
	def test_instance(self):
		self.assertTrue(isinstance(self.new_post, UserPost))

	def tearDown(self):
		UserPost.objects.filter(title=self.id).delete()


class BusinessTestClass(TestCase):
	def setUp(self):
		# create new user & save
		self.benie = MyUser(email='benie@g.com', username='benie', first_name='Benson', last_name='Langat')
		self.benie.save()

		self.new_hood = UserHood(name='mbagathi',user=self.benie)
		self.new_hood.save()

		self.new_business = Business(name='The Kazi People',description='WHo chapa kazi',hood_name='mbagathi',email='tkp@g.com',phone=25473272,hood=self.new_hood,user=self.benie)
		self.new_business.save()

	# test instance
	def test_instance(self):
		self.assertTrue(isinstance(self.new_business, Business))

	def tearDown(self):
		Business.objects.filter(name=self.id).delete()

	def test_update_business(self):
		self.updated_business = Business.objects.filter(name=self.id).update(name='The July People',description='WHo chapaap kazi',hood_name='mbagathi-way',email='tkpa@g.com',phone=254713272)

	def test_get_by_location(self):
		get_by_location = Business.objects.filter(hood_name__icontains=self)
		return get_by_location

	def test_get_by_id(self):
		get_by_id = Business.objects.filter(hood_name=self)
		return get_by_id


class PoliceDeptTestClass(TestCase):
	def setUp(self):
		self.new_dept = PoliceDept(name='TheSafetyNet PD',email='tsn@g.com',phone=25472828,address='Nairobi',hood='Langata',police_chief='Michael')
		self.new_dept.save()

	# test instance
	def test_instance(self):
		self.assertTrue(isinstance(self.new_dept, PoliceDept))

	def tearDown(self):
		PoliceDept.objects.filter(name=self.id).delete()


class HealthDeptTestClass(TestCase):
	def setUp(self):
		self.new_health_dept = HealthDept(name='DoctorsTouch',email='dt@g.com',phone=25432111,address='Kisumu',hood='Omsomplace')
		self.new_health_dept.save()

	# test instance
	def test_instance(self):
		self.assertTrue(isinstance(self.new_health_dept, HealthDept))

	def tearDown(self):
		HealthDept.objects.filter(name=self.id).delete()