from models.item import ItemModel
from tests.integration.integration_base_test import BaseTest
from models.store import StoreModel

class ItemTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            StoreModel('test').save_to_db()
            item = ItemModel('test', 19.99, 1)

            # save an item
            # make sure the item doesn't exist
            self.assertIsNone(ItemModel.find_by_name('test'),
                              f'Found an item with name {item.name} but expected not to.')

            item.save_to_db()

            # the item was saved, we have an item now
            self.assertIsNotNone(ItemModel.find_by_name('test'))

            # delete an item
            item.delete_from_db()
            self.assertIsNone(ItemModel.find_by_name('test'))

    def test_store_relationship(self):
        with self.app_context():
            store = StoreModel('test_store')
            item = ItemModel('test', 19.99, 1)

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(item.store.name, 'test_store')
