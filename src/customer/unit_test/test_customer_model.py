import pytest
from customer.models import Customer
from user.models import CustomUser


@pytest.mark.django_db
def test_create_customer():
    # create a sales contact user for the customer
    sales_contact = CustomUser.objects.create_user(email='p.laroche@example.com',
                                                   first_name='Paul',
                                                   last_name='Laroche',
                                                   role='sale',
                                                   password='test_password')

    # create a customer
    customer = Customer.objects.create(
        first_name='Pascal',
        last_name='Martin',
        email='p.martin@intel.com',
        phone='1234567890',
        mobile='0987654321',
        company_name='Intel',
        sales_contact=sales_contact
    )

    # check if the customer was created with the correct attributes
    assert customer.first_name == 'Pascal'
    assert customer.last_name == 'Martin'
    assert customer.email == 'p.martin@intel.com'
    assert customer.phone == '1234567890'
    assert customer.mobile == '0987654321'
    assert customer.company_name == 'Intel'
    assert customer.sales_contact == sales_contact
