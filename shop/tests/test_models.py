from django.test import TestCase
from shop.models import Product, Purchase, Promocode
from datetime import datetime

class ProductTestCase(TestCase):
    def setUp(self):
        self.prom1 = Promocode.objects.create(number="1", date_end=datetime.fromisoformat('2025-03-29T04:38:47'))
        self.prom2 = Promocode.objects.create(number="2", date_end=datetime.fromisoformat('2025-04-29T04:38:47'))
        Product.objects.create(name="book", price="740", promid=self.prom1)
        Product.objects.create(name="pencil", price="50", promid=self.prom2)

    def test_correctness_types(self):                   
        self.assertIsInstance(Product.objects.get(name="book").name, str)
        self.assertIsInstance(Product.objects.get(name="book").price, int)
        self.assertIsInstance(Product.objects.get(name="book").promid, Promocode)
        self.assertIsInstance(Product.objects.get(name="pencil").name, str)
        self.assertIsInstance(Product.objects.get(name="pencil").price, int)
        self.assertIsInstance(Product.objects.get(name="pencil").promid, Promocode)

    def test_correctness_data(self):
        self.assertTrue(Product.objects.get(name="book").price == 740)
        self.assertTrue(Product.objects.get(name="book").promid == self.prom1)
        self.assertTrue(Product.objects.get(name="pencil").price == 50)
        self.assertTrue(Product.objects.get(name="pencil").promid == self.prom2)

class PurchaseTestCase(TestCase):
    def setUp(self):
        self.product_book = Product.objects.create(name="book", price="740")
        self.datetime = datetime.now()
        Purchase.objects.create(product=self.product_book,
                                person="Ivanov",
                                address="Svetlaya St.")

    def test_correctness_types(self):
        self.assertIsInstance(Purchase.objects.get(product=self.product_book).person, str)
        self.assertIsInstance(Purchase.objects.get(product=self.product_book).address, str)
        self.assertIsInstance(Purchase.objects.get(product=self.product_book).date, datetime)

    def test_correctness_data(self):
        self.assertTrue(Purchase.objects.get(product=self.product_book).person == "Ivanov")
        self.assertTrue(Purchase.objects.get(product=self.product_book).address == "Svetlaya St.")
        self.assertTrue(Purchase.objects.get(product=self.product_book).date.replace(microsecond=0) == \
            self.datetime.replace(microsecond=0))

class PromocodeTestCase(TestCase):
    def setUp(self):
        self.promo_number = "1";
        self.promo_date = datetime.now()
        Promocode.objects.create(number = self.promo_number,
                                 date_end = self.promo_date)
        
    def test_correctness_types(self):
        self.assertIsInstance(Promocode.objects.get(number=self.promo_number).number, str)
        self.assertIsInstance(Promocode.objects.get(number=self.promo_number).date_end, datetime)
    
    def test_correctness_data(self):
        self.assertTrue(Promocode.objects.get(number=self.promo_number).number == "1")
        self.assertTrue(Promocode.objects.get(number=self.promo_number).date_end.replace(microsecond=0) == self.promo_date.replace(microsecond=0))