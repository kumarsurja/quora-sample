from .test_setup import TestSetUp
from ..models import User


class TestViews(TestSetUp):
    def test_user_cannot_register_with_no_data(self):        
        res = self.client.post(self.register_url)
        self.assertEqual(res.status_code, 400)
        print("User Can't be added with NO details:: Passed")

    def test_user_can_register_correctly(self):
        res = self.client.post(self.register_url, self.user_data, format="json")
        self.assertEqual(res.data['data']['email'], self.user_data['email'])
        self.assertEqual(res.data['data']['first_name'], self.user_data['first_name'])
        self.assertEqual(res.data['data']['last_name'], self.user_data['last_name'])
        self.assertEqual(res.status_code, 200)
        print("User Registration Successful:: Passed")          

    def test_inactive_user_can_not_login(self):
        self.client.post(self.register_url, self.user_data, format="json")        
        res = self.client.post(self.login_url, self.user_data, format="json")
        self.assertEqual(res.status_code, 400)       

    def test_user_can_login_after_activation(self):
        response = self.client.post(
            self.register_url, self.user_data, format="json")
        email = self.user_data['email']
        user = User.objects.get(email=email)
        user.is_active = True
        user.save()
        res = self.client.post(self.login_url, self.user_data, format="json")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data['data']['email'], self.user_data['email'])
        print("Only Active user can login:: Passed")
        

    def test_unauthorised_user_can_not_get_user_list(self):
        res = self.client.post(self.user_list, format="json")        
        self.assertEqual(res.status_code, 401)
        print("Authorization Token needed for user list:: Passed")   


