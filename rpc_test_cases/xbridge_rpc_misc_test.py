import unittest
import xbridge_logger
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import random

from utils import xbridge_custom_exceptions
from interface import xbridge_rpc
from utils import xbridge_utils

subTest_count = 10

class Misc_UnitTest(unittest.TestCase):
    def setUp(self):
        xbridge_utils.generate_new_set_of_data(data_nature=xbridge_utils.INVALID_DATA, char_min_size=1, char_max_size=10000)

    def test_getinfo(self):
        try:
            log_json = ""
            xbridge_utils.generate_new_set_of_data(data_nature=xbridge_utils.VALID_DATA)            
            self.assertIsInstance(xbridge_rpc.rpc_connection.getinfo(), dict)
            log_json = {"group": "test_getinfo", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_getinfo", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except JSONRPCException as json_excpt:
            log_json = {"group": "test_getinfo", "success": 0, "failure": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
        
        
    # signmessage "blocknetdxaddress" "message"
    # Please enter the wallet passphrase with walletpassphrase first.
    # TODO: valid test
    def test_signmessage_invalid(self):
        for i in range(subTest_count):
            log_json = ""
            with self.subTest("test_signmessage_invalid"):
                try:
                    invalid_blocknet_address = random.choice(xbridge_utils.set_of_invalid_parameters)
                    message = random.choice(xbridge_utils.set_of_invalid_parameters)
                    self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.sign_message, invalid_blocknet_address, message)
                    log_json = {"group": "test_signmessage_invalid", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_signmessage_invalid", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_signmessage_invalid unit test FAILED: %s' % ass_err)
                    xbridge_logger.logger.info('invalid_blocknet_address: %s \n' % invalid_blocknet_address)
                    xbridge_logger.logger.info('message: %s \n' % message)
                except JSONRPCException as json_excpt:
                    log_json = {"group": "test_signmessage_invalid", "success": 0, "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_signmessage_invalid unit test ERROR: %s' % json_excpt)
                    xbridge_logger.logger.info('invalid_blocknet_address: %s \n' % invalid_blocknet_address)
                    xbridge_logger.logger.info('message: %s \n' % message)

    # autocombinerewards <true/false> threshold
    def test_autocombinerewards_valid(self):
        try:
            log_json = ""
            success_str = "Auto Combine Rewards Threshold Set"
            xbridge_utils.generate_new_set_of_data(data_nature=xbridge_utils.VALID_DATA)            
            self.assertEqual(xbridge_rpc.rpc_connection.autocombinerewards(False), success_str)
            self.assertEqual(xbridge_rpc.rpc_connection.autocombinerewards(False, -99999999999999), success_str)
            self.assertEqual(xbridge_rpc.rpc_connection.autocombinerewards(True, 0), success_str)
            self.assertEqual(xbridge_rpc.rpc_connection.autocombinerewards(True, xbridge_utils.valid_random_positive_int), success_str)
            self.assertEqual(xbridge_rpc.rpc_connection.autocombinerewards(True, -xbridge_utils.valid_random_positive_int), success_str)
            log_json = {"group": "test_autocombinerewards_valid", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_autocombinerewards_valid", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_autocombinerewards_valid FAILED: %s' % ass_err)
            xbridge_logger.logger.info('fixed_positive_int: %s \n' % xbridge_utils.fixed_positive_int)
            xbridge_logger.logger.info('fixed_negative_int: %s \n' % xbridge_utils.fixed_negative_int)
            xbridge_logger.logger.info('valid_random_positive_int: %s \n' % xbridge_utils.valid_random_positive_int)
        except JSONRPCException as json_excpt:
            log_json = {"group": "test_autocombinerewards_valid", "success": 0, "failure": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_autocombinerewards_valid ERROR: %s' % json_excpt)

    # autocombinerewards <true/false> threshold
    def test_autocombinerewards_invalid(self):
        for i in range(subTest_count):
            log_json = ""
            with self.subTest("autocombinerewards combinations"):
                try:      
                    modified_set = [x for x in xbridge_utils.set_of_invalid_parameters if not isinstance(x, bool)]
                    true_false = random.choice(modified_set)
                    threshold = random.choice(xbridge_utils.set_of_invalid_parameters)
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.autocombinerewards, true_false, threshold)
                    log_json = {"group": "test_autocombinerewards_invalid", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_autocombinerewards_invalid", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_autocombinerewards_invalid FAILED: %s' % ass_err)

    # move "fromaccount" "toaccount" amount ( minconf "comment" )
    def test_move_invalid(self):
        log_json = ""
        for i in range(subTest_count):
            log_json = ""
            with self.subTest("move combinations"):
                try:      
                    fromAccount = random.choice(xbridge_utils.set_of_invalid_parameters)
                    toaccount = random.choice(xbridge_utils.set_of_invalid_parameters)
                    amount = random.choice(xbridge_utils.set_of_invalid_parameters)
                    if random.choice(["", xbridge_utils.set_of_invalid_parameters]) == "":
                        optional_minconf = None
                    else:
                        optional_minconf = random.choice(xbridge_utils.set_of_invalid_parameters)
                    if random.choice(["", xbridge_utils.set_of_invalid_parameters]) == "":
                        optional_comment = None
                    else:
                        optional_comment = random.choice(xbridge_utils.set_of_invalid_parameters)
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.move, fromAccount, toaccount, amount, optional_minconf, optional_comment)
                    log_json = {"group": "test_move_invalid", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_move_invalid", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_move_invalid FAILED: %s' % ass_err)
                    
    # lockunspent unlock [{"txid":"txid","vout":n},...]
    def test_lockunspent_invalid(self):
        log_json = ""
        for i in range(subTest_count):
            log_json = ""
            with self.subTest("lockunspent combinations"):
                try:      
                    unlock_param = random.choice(xbridge_utils.set_of_invalid_parameters)
                    transactions = random.choice(xbridge_utils.set_of_invalid_parameters)
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.lockunspent, unlock_param, transactions)
                    log_json = {"group": "test_lockunspent_invalid", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_lockunspent_invalid", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_lockunspent_invalid FAILED: %s' % ass_err)

# unittest.main()

"""
suite = unittest.TestSuite()
# suite.addTest(Misc_UnitTest("test_autocombinerewards_valid"))
suite.addTest(Misc_UnitTest("test_signmessage_invalid"))
runner = unittest.TextTestRunner()
runner.run(suite)
"""
